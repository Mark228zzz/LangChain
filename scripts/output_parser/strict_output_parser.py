from langchain_core.output_parsers import BaseOutputParser
from langchain_core.outputs import Generation # Generation is used to simulate LLM output
import re
from typing import Dict
import json # For JSON visualization


class ExerciseOutputParser(BaseOutputParser):
    """A strict output parser that only accepts a specific format of exercise."""

    def parse(self, text: str) -> Dict[str, object]:
        # Regular expressions for matching expected fields
        exercise_match = re.search(r"exercise\s*[:\-]?\s*(.*)", text, re.IGNORECASE)
        difficulty_match = re.search(r"difficulty\s*[:\-]?\s*(\d{1,2})", text, re.IGNORECASE)
        description_match = re.search(r"description\s*[:\-]?\s*(.*)", text, re.IGNORECASE)

        # Extract or default
        exercise = exercise_match.group(1).strip() if exercise_match else ""
        difficulty = int(difficulty_match.group(1)) if difficulty_match else 0
        description = description_match.group(1).strip() if description_match else ""

        # Enforce difficulty bounds
        difficulty = max(1, min(difficulty, 10))

        return {
            "exercise": exercise,
            "difficulty": difficulty,
            "description": description
        }


def main():
    parser = ExerciseOutputParser()

    # Example 1 usage of the parser
    llm_output1 = Generation(text="""
        Exercise: Build a binary classifier using PyTorch.\nDifficulty: 7\nDescription: The task involves creating a simple neural network to classify MNIST digits.
    """)

    # Example 2 usage of the parser (with some formatting issues)
    llm_output2 = Generation(text="""
        Exercise: Implement a sorting algorithm.
                             Difficulty: 132  DescriptionWrite a function that sorts an array of integers using quicksort.
    """)

    # Parse the outputs
    parsed = parser.parse(llm_output1.text)
    print("Parsed Output Example 1:\n{}".format(json.dumps(parsed, indent=2)))

    print('\n')

    parsed = parser.parse(llm_output2.text)
    print("Parsed Output Example 2:\n{}".format(json.dumps(parsed, indent=2)))

if __name__ == "__main__":
    main()

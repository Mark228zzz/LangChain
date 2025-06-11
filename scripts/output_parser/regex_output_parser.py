from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel


# Define a schema
class TaskModel(BaseModel):
    task: str
    due_date: str
    priority: str
    interest: int


def main():
    # Create the parser
    task_parser = PydanticOutputParser(pydantic_object=TaskModel)

    # Example raw output
    raw_output = '{"task": "learn Python", "due_date": "2025-01-10", "priority": "high", "interest": 1000}'

    # Parse the raw output
    parsed_output = task_parser.parse(raw_output)

    print(f'Parsed Data: {parsed_output}')

if __name__ == '__main__':
    main()

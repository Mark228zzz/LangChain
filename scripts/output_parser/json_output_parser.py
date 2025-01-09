from langchain.schema import StrOutputParser
import json
from typing import Dict, Any


# Create a basic string output parser
class JSONOutputParser(StrOutputParser):
    def parse(self, text: str) -> Dict[Any, Any]:
        return json.loads(text)


def main():
    # Create the JSONParser
    parser = JSONOutputParser()

    # Example of data
    raw_output = '{"task": "Learn Python", "deadline": "2025-01-20", "priority": "high", "interest": 1000}'

    # Parse the JSON string
    parsed_data = parser.parse(raw_output)

    print(f'Raw data: {raw_output}\n') # Type: str
    print(f'Parsed data: {parsed_data}') # Type: dict

if __name__ == '__main__':
    main()

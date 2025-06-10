from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.outputs import Generation

def main():
    # Define the response schemas for the book information
    # Each schema corresponds to a field we expect in the LLM output
    # This parser will enforce a specific structure for the output
    response_schemas = [
        ResponseSchema(name='title', description='The title of the book'),
        ResponseSchema(name='author', description='The author of the book'),
        ResponseSchema(name='publication_year', description='The year the book was published'),
        ResponseSchema(name='genre', description='The genre of the book'),
        ResponseSchema(name='summary', description='A brief summary of the book')
    ]

    parser = StructuredOutputParser.from_response_schemas(response_schemas)

    # Print the format instructions for the parser
    print(parser.get_format_instructions())

    llm_output = Generation(text="""
                    Title: 1984
                    Author: George Orwell
                    Publication Year: 1949
                    Genre: Dystopian
                    Summary: A novel about a totalitarian regime that uses surveillance and propaganda to control its citizens.
    """)

    print(llm_output.text)

if __name__ == "__main__":
    main()

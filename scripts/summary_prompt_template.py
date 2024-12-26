from langchain_core.prompts import PromptTemplate  # For creating custom prompt templates
from langchain_openai import ChatOpenAI  # For interacting with OpenAI's API
from dotenv import load_dotenv
from colorama import Fore  # For colored output in the terminal

# Information about Mark Zuckerberg
information = """
Mark Elliot Zuckerberg (born May 14, 1984) is an American businessman who co-founded the social media service Facebook and its parent company Meta Platforms, of which he is the chairman, chief executive officer, and controlling shareholder. Zuckerberg has been the subject of multiple lawsuits regarding the creation and ownership of the website as well as issues such as user privacy.
Zuckerberg briefly attended Harvard College, where he launched Facebook in February 2004 with his roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz and Chris Hughes. Zuckerberg took the company public in May 2012 with majority shares. He became the world's youngest self-made billionaire[a] in 2008, at age 23, and has consistently ranked among the world's wealthiest individuals. He has also used his funds to organize multiple donations, including the establishment of the Chan Zuckerberg Initiative.
A film depicting Zuckerberg's early career, legal troubles and initial success with Facebook, The Social Network, was released in 2010 and won multiple Academy Awards. His prominence and fast rise in the technology industry has prompted political and legal attention.
Early life and education
Mark Elliot Zuckerberg was born on May 14, 1984, in White Plains, New York to psychiatrist Karen (née Kempner) and dentist Edward Zuckerberg.[2][3] He and his three sisters (Arielle, Randi, and Donna) were raised in a Reform Jewish household[4] in Dobbs Ferry, New York.[5] His great-grandparents were emigrants from Austria, Germany, and Poland.[6] Zuckerberg initially attended Ardsley High School before transferring to Phillips Exeter Academy. He was captain of the fencing team.[7][8]
Software development
Early years
Zuckerberg learned computer programming in his childhood. At about the age of eleven, he created "ZuckNet", a program that allowed computers at the family home and his father's dental office to communicate with each other.[9] During Zuckerberg's high-school years, he worked to build a music player called the Synapse Media Player. The device used machine learning to learn the user's listening habits, which was posted to Slashdot[10] and received a rating of 3 out of 5 from PC Magazine.[11] The New Yorker once said of Zuckerberg, "some kids played computer games. Mark created them."[5] While still in high school, he attended Mercy College taking a graduate computer course on Thursday evenings.[5]
College years
The New Yorker noted that by the time Zuckerberg began classes at Harvard in 2002, he had already achieved a "reputation as a programming prodigy".[5] He studied psychology and computer science,[12] resided in Kirkland House,[13] and belonged to Alpha Epsilon Pi.[5] In his second year, he wrote a program that he called CourseMatch, which allowed users to make class selection decisions based on the choices of other students and help them form study groups.[14] Later, he created a different program he initially called Facemash that let students select the best-looking person from a choice of photos. Arie Hasit, Zuckerberg's roommate at the time, explained:
    We had books called "Face Books", which included the names and pictures of everyone who lived in the student dorms. At first, he built a site and placed two pictures or pictures of two males and two females. Visitors to the site had to choose who was "hotter" and according to the votes there would be a ranking.[15]
The site went up over a weekend, but by Monday morning, the college shut it down, because its popularity had overwhelmed one of Harvard's network switches preventing students from accessing the Internet.[16] In addition, many students complained that their photos were being used without permission. Zuckerberg apologized publicly, and the student paper ran articles stating that his site was "completely improper".[15]
"""

def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Create a prompt template that takes 'information' as input
    summary_template = """
    Given the information {information} about a person from I want you to create a summary in these steps:
    1. Year of birth and year of death (ONLY if this person died).
    2. A SHORT summary.
    3. A few interesting facts about that person. Short version
    """

    # Create a prompt template object that will format the template
    summary_prompt_template = PromptTemplate(input_variables=['information'], template=summary_template)

    # Initialize the LLM (Language Model) from OpenAI (using GPT-4)
    llm = ChatOpenAI(temperature=0.0, model='gpt-4o')

    # Create a pipeline combining the prompt template and LLM
    chain = summary_prompt_template | llm

    # Run the chain to get a response by passing the information
    response = chain.invoke(input={'information': information})

    # Print the response from the model in colored text
    print(f'{Fore.LIGHTGREEN_EX}ChatGPT:\n{Fore.LIGHTBLUE_EX}{response.content}')

if __name__ == '__main__':
    main()

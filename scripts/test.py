import requests
from bs4 import BeautifulSoup

def internet_search(query: str) -> str:
    search_url = f"https://duckduckgo.com/html/?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    search_response = requests.get(search_url, headers=headers)
    
    if search_response.status_code != 200:
        return "Error fetching search results. Status code: " + str(search_response.status_code)
    
    search_soup = BeautifulSoup(search_response.text, 'html.parser')
    results = search_soup.find_all('a', class_='result__a')
    
    if not results:
        return "No results found or structure changed."
    
    first_link = results[0]['href']
    print(f"First link found: {first_link}")
    return first_link

# Test the function
query = "LangChain Python"
first_link = internet_search(query)
print(first_link)

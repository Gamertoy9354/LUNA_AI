import requests
from googlesearch import search
from bs4 import BeautifulSoup


def search_wikipedia(query):
    # Perform Google search and filter results for Wikipedia pages
    wikipedia_urls = [url for url in search(query, num=10, stop=10) if "https://en.wikipedia.org/wiki/" in url]
    return wikipedia_urls[0] if wikipedia_urls else None

# Example usage
query = input("Enter your search query: ")
wikipedia_result = search_wikipedia(query)

if wikipedia_result:
    
    # URL of the webpage you want to scrape
    url = wikipedia_result

# Send a GET request to the URL
    response = requests.get(url)

# Check if the request was successful
    if response.status_code == 200:
    # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, "html.parser")
    
        div_element = soup.find("div", id="mw-content-text")
        if div_element:
            div2_lement = div_element.find("div")
            print("found DIV 2!")
            if div2_lement:
                p_tags = div2_lement.find_all("p")
                print("Text content of the first three <p> tags within <div id='mp-tfa'>:")
                for p_tag in p_tags[:3]:
                    print(p_tag.text.strip())
            else:
                print("NO <p> tag sorry for inconvinience")
        else:
            print("no <div> tag found sorry for the inconvinience")
    else:
        print("Failed to retrieve webpage.")

else:
    print("No Wikipedia page found for the given query.")
import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = "https://en.wikipedia.org/wiki/Main_Page"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the <h2> element with id "mp-tfa-h2"
    h2_element = soup.find("h2", id="mp-tfa-h2")
    # Check if the element was found
    if h2_element:
        print(h2_element.text.strip())  # Print the text content of the element
    else:
        print("No <h2> element with id 'mp-tfa-h2' found.")

    print("")

    div_element = soup.find("div", id="mp-tfa")
    if div_element:
        p_tag = div_element.find("p")


        if p_tag:
            print(p_tag.text.strip())
        else:
            print("NO <p> tag sorry for inconvinience")
    else:
        print("no <div> tag found sorry for the inconvinience")

else:
    print("Failed to retrieve webpage.")

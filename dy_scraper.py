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
    
    # Find the <div> element with id "mp-tfa"
    div_element = soup.find("div", id="mp-dyk")
    
    # Check if the element was found
    if div_element:
        # Find the <ul> element within the <div> element
        ul_element = div_element.find("ul")
        
        # Check if the <ul> element was found
        if ul_element:
            # Find all <li> tags within the <ul> element
            li_tags = ul_element.find_all("li")
            
            # Print the text content of the first three <li> tags
            print("Text content of the first three <li> tags within <ul>:")
            for li_tag in li_tags[:7]:
                print(li_tag.text.strip())
        else:
            print("No <ul> element found within <div id='mp-tfa'>.")
    else:
        print("No <div> element with id 'mp-tfa' found.")
else:
    print("Failed to retrieve webpage.")

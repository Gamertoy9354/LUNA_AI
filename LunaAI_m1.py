import requests
import time
from googlesearch import search
from bs4 import BeautifulSoup


name = str(input("Hello This i an Internet accessed AI Made By Shis Maheta please Enter your name to continue: "))
main_page = "https://en.wikipedia.org/wiki/Main_Page"
if len(name)>0:
    print(name,"Thank you for continuing ")
    time.sleep(2)
    print("This AI is currently Beta stage")
    time.sleep(2)
    cnti = "yes"
    while cnti == "yes":
        ch1 = str(input('If you want to learn more about this AI type "info" and if you want to use this AI type "use":'))
        if ch1 == "info":
            print("This i an AI that has access to Internet and can give result based on the information available online")
            time.sleep(2)
            print("Please keep this in mind that this AI takes information from directly wikipedia and shows it to you")
            time.sleep(1)
            print("Please keep this in mind that this AI is currently in it's BETA Stage so there might be some bug")
            time.sleep(2)
            print("Keep in mind that this as this AI needs internet Access you need to be connected to a WIFI to use this!")
        elif ch1 =="use":
            print("There are currently five services that this AI offer you can select any one of them from choosing their corresponding integer!")
            time.sleep(3)
            print("1.Today's Article!, 2.Today's Fact!, 3.Custom Search!, 4.Today's News!, 5.What happend today in past!")
            choice = str(input("Please Enter your Choice: "))

            if choice == "1": #toady's Article

                response = requests.get(main_page)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    h21_element = soup.find("h2", id="mp-tfa-h2")
                    if h21_element:
                        print(h21_element.text.strip())  
                    else:
                        print("No <h2> element with id 'mp-tfa-h2' found.")

                    print("")

                    div1_element = soup.find("div", id="mp-tfa")
                    if div1_element:
                        p1_tag = div1_element.find("p")
                    if p1_tag:
                        print(p1_tag.text.strip())

            elif choice == "2": #Today's Fact

                response = requests.get(main_page)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    divf_element = soup.find("div", id="mp-dyk")
                    if divf_element:
                        ulf_element = divf_element.find("ul")
                    if ulf_element:
                        lif_tags = ulf_element.find_all("li")
                        print("Text content of the first three <li> tags within <ul>:")
                        for lif_tag in lif_tags[:7]:
                            print(lif_tag.text.strip())

                else:
                    print("Failed to retrieve webpage.")

            elif choice == "3": #custom query
                def search_wikipedia(query):
                    wikipedia_urls = [url for url in search(query, num=10, stop=10) if "https://en.wikipedia.org/wiki/" in url]
                    return wikipedia_urls[0] if wikipedia_urls else None
                query = input("Enter your search query: ")
                wikipedia_result = search_wikipedia(query)
                if wikipedia_result:
                    url = wikipedia_result
                    response = requests.get(url)
                    if response.status_code == 200:
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
                        print("Failed to retrieve webpage.")

            elif choice == "4": #today's news
                response = requests.get(main_page)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    divn_element = soup.find("div", id="mp-itn")
                    if divn_element:
                        uln_element = divn_element.find("ul")
                    if uln_element:
                        lin_tags = uln_element.find_all("li")
                        for lin_tag in lin_tags[:3]:
                            print(lin_tag.text.strip())

            elif choice == "5": #on this day

                response = requests.get(main_page)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    divd_element = soup.find("div", id="mp-otd")
                    if divd_element:
                        uld_element = divd_element.find("ul")
                    if uld_element:
                        lid_tags = uld_element.find_all("li")
                        for lid_tag in lid_tags[:5]:
                            print(lid_tag.text.strip())
            else:
                print("Please chose a correct option")

        cnti = str(input("do you want to continue using this AI? yes/no: "))
print("Bye! Thanks for using this AI!")
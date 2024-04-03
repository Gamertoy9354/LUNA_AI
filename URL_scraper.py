from googlesearch import search

def search_wikipedia(query):
    # Perform Google search and filter results for Wikipedia pages
    wikipedia_urls = [url for url in search(query, num=10, stop=10) if "https://en.wikipedia.org/wiki/" in url]
    return wikipedia_urls[0] if wikipedia_urls else None

# Example usage
query = input("Enter your search query: ")
wikipedia_result = search_wikipedia(query)

if wikipedia_result:
    print("Wikipedia URL:")
    print(wikipedia_result)
else:
    print("No Wikipedia page found for the given query.")
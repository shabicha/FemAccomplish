import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

#returns dictionary
def get_forbes_data(query, num_pages=3):
    base_url = f"https://www.forbes.com/search/?sort=score&q={query}&sh=4ca208c3279f"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    all_data = []

    try:
        for page in range(1, num_pages + 1):
            page_url = f"{base_url}&page={page}"

            response = requests.get(page_url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract links from search results
            links = [a['href'] for a in soup.find_all('a', {'class': 'stream-item__title'})]

            # For each link, make a new request and scrape the title
            for link in links:
                article_response = requests.get(link, headers=headers)
                article_response.raise_for_status()

                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                # Extract the title from the linked page
                title_element = article_soup.find('h1', {'class': 'fs-headline'})
                title = title_element.text.strip() if title_element is not None else None

                # Store the link and title in a dictionary, only if title is not None
                if title is not None:
                    article_data = {'link': link, 'title': title}
                    all_data.append(article_data)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return all_data

# Example usage
search_query = "women"
num_pages_to_fetch = 3
forbes_data = get_forbes_data(search_query, num_pages_to_fetch)
print(forbes_data)

#function that takes both funcs above and creates dictionary 


#FUTURE PLANS
#clean code 
#automate posts every day 
#more efficent article title to article link matching system
#create code to work for all html websites/customizable using methods 
#forbes was chosen due to overall positive sentiment analysis, if implementing bot to other websites incorporate sentiment analysis tool to asses whether tweet should be made
#make sure no repeat tweets -> tweets should be sceduled every week to account for new articles, but no article should be tweeted twice





# imports
import requests
from bs4 import BeautifulSoup


'''
read websites robots.txt before web-scrapping the whole website
'''
file_location = "profile_resources/Important/"
file = 'collected_words.txt'
target_file = file_location + file

def scrapping_words(url):

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve page {url}: {e}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # Try to find the parent element that contains the word list
    parent_element = soup.find('div', class_='dDeYl3zUalQgXsSgFtAi')
    if not parent_element:
        print(f"\nParent element not found on page {url}\n")
        return []
    
    # Try to find the class name dynamically
    word_elements = parent_element.find_all('a')
    if not word_elements:
        print(f"No word elements found within parent on page {url}\n")
        return []
    
    # Extract words from the word elements
    words = []

    for word_elem in word_elements:
        # Split the text content by whitespace to separate individual words
        words.extend(word_elem.get_text().split())

    # words = [word_elem.text for word_elem in parent_element]
    
    return words

# Base URL for the pages to scrape
letters = "abcdefghijklmnopqrstuvwxyz"
base_url = "https://www.dictionary.com/list/"

all_words = []
limit_dict = {}

disallowed_paths = [
    '/5480.iac.', '/go/', '/audio.html/', '/houseads/', 
    '/askhome/', '/23219321/iac.', '/*,*', '/browse-2/'
]

for letter in letters:
    page_number = 1
    base_url_letter = base_url + letter + "/"

    while True:
        # Construct the URL for the current page
        url = f"{base_url_letter}{page_number}"
        
        # Check if the URL matches any disallowed paths
        if any(path in url for path in disallowed_paths):
            print(f"Skipping disallowed path: {url}")
            page_number += 1
            continue

        print(f"Processing page: {url}")
        words = scrapping_words(url)
        
        # If no words are found, we've reached the last page
        if not words:
            print(f"No words found on page {page_number}. Ending scrape.\n")
            limit_dict[letter] = (page_number - 1)
            break
        
        # Add the words to the list of all words
        all_words.extend(words)
        print(f"Page {page_number}: Found {len(words)} words.\n")
        
        # Move to the next page
        page_number += 1

# Join all words into a single string with each word on a new line
all_words_string = '\n'.join(all_words)

# Save the collected words to a text file
with open(target_file, 'w', encoding='utf-8', errors='ignore') as file:
    file.write(all_words_string)

print("\nAll words collected:")
print(f"Total Number of Collected : {len(all_words)}")
print(f"This is how many pages that existed for each letter on {base_url}.\n\n{limit_dict}")
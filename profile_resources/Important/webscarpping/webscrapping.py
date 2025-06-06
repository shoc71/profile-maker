# imports
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

'''
read websites robots.txt before web-scrapping the whole website
'''
file_location = "profile_resources/Important/webscrapping/"
file = 'collected_words.txt'
target_file = file_location + file

def scrapping_words(url):

    try:
        response = requests.get(url)
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve page {url}: {e} 1")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # Try to find the parent element that contains the word list
    parent_element = soup.find('div', class_='section_content') # Inspect element and find the correct class, to make this work
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
        # Get text of the element and clean it
        words.extend(word_elem.get_text().split())

    # words = [word_elem.text for word_elem in parent_element]
    
    return words

def get_disallowed_paths(base_url):
    robots_url = urljoin(base_url, '/robots.txt')

    try:
        response = requests.get(robots_url)
        response.raise_for_status()
        robots_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {robots_url}: {e} 2")
        return []

    # Parse robots.txt content to find disallowed paths
    disallowed_paths = []
    lines = robots_content.splitlines()

    for line in lines:
        if line.strip().lower().startswith('disallow:'):
            path = line.strip().split(':', 1)[1].strip()
            disallowed_paths.append(path)

    return disallowed_paths

def are_words_same(prev_words, curr_words):
    """Function to check if two lists of words are identical."""
    return prev_words == curr_words

# Base URL for the pages to scrape
letters = "abcdefghijklmnopqrstuvwxyz"
# letters = "a"
# base_url = "https://www.dictionary.com/list/"
# base_url = 'https://www.merriam-webster.com/browse/dictionary/'
# base_url = 'https://www.merriam-webster.com/wordfinder/classic/any-order/all/-1/'
# base_url = 'https://www.thefreedictionary.com/words-containing-'
# base_url = 'https://scrabble.merriam.com/words/with/'
base_url = 'https://www.baseball-reference.com/players/'

all_words = []
limit_dict = {}
prev_words = None

# From https://www.merriam-webster.com/robots.txt
disallowed_paths = get_disallowed_paths(base_url)

for letter in letters:
    page_number = 1
    base_url_letter = base_url + letter + "/"

    while True:
        # Construct the URL for the current page
        # url = f"{base_url_letter}{page_number}"
        url = f"{base_url_letter}"
        # url = f"{base_url}geo/{page_number}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            if response.status_code == 429:  # Too Many Requests
                retry_after = int(response.headers.get('Retry-After', 5))  # Default retry after 5 seconds
                print(f"Rate limited. Retrying after {retry_after} seconds...")
                time.sleep(retry_after)
                continue
            
            print(f"Failed to retrieve page {url}: {e} 3")
            break
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Check for specific content that indicates end of pagination (preventing any repeats)
        if "No more results" in soup.get_text():
            print(f"No more results for letter {letter}. Ending scrape.\n")
            limit_dict[letter] = page_number - 1
            break

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
        
        # Check if words from current page are the same as previous page
        if prev_words and are_words_same(prev_words, words):
            print(f"Words on page {page_number} are identical to previous page. Ending scrape for letter {letter}.\n")
            break
        
        # Move to the next page
        prev_words = words  # Update previous words with current words
        page_number += 1
        
    # Move to the next letter in the alphabet
    print(f"Completed scraping for letter '{letter}'. Moving to the next letter.\n")
    prev_words = None  # Reset prev_words for the next letter

# Join all words into a single string with each word on a new line
all_words_string = '\n'.join(all_words).replace(",","\n").replace("ˌ","\n").replace(".","\n")

# Save the collected words to a text file
with open(target_file, 'w', encoding='utf-8', errors='ignore') as file:
    file.write(all_words_string)

print("\nAll words collected:")
print(f"Total Number of Collected : {len(all_words)}")
print(f"This is how many pages that existed for each letter on {base_url}.\n\n{limit_dict}")

'''
for mariam word lookup
{'a': 398, 'b': 105, 'c': 227, 'd': 179, 'e': 461, 'f': 62, 'g': 140, 'h': 155, 'i': 409, 'j': 11, 'k': 53, 'l': 271, 'm': 173, 'n': 329, 'o': 336, 'p': 175, 'q': 10, 'r': 356, 's': 405, 't': 331, 'u': 183, 'v': 51, 'w': 41, 'x': 20, 'y': 104, 'z': 30}


'''
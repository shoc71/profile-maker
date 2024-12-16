# imports
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging
import time

'''
read websites robots.txt before web-scraping the whole website
'''

# Configure logging for errors
logging.basicConfig(filename='scraping_errors.log', level=logging.ERROR)

file_location = "profile_resources/Important/webscrapping/"
file = 'collected_words.txt'
target_file = os.path.join(file_location, file)

# Ensure the directory for the output file exists
os.makedirs(file_location, exist_ok=True)

# Create a requests session for persistent connections
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
})

def scrapping_words(url):
    """Scrape words from the given URL."""
    try:
        response = session.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve page {url}: {e}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # Try to find the parent element that contains the word list
    parent_element = soup.find('div', class_='section_content')  # Replace with the correct class name for your use case
    if not parent_element:
        print(f"\nParent element not found on page {url}\n")
        return []
    
    # Find all word elements within the parent element
    word_elements = parent_element.find_all('a')
    if not word_elements:
        print(f"No word elements found within parent on page {url}\n")
        return []
    
    # Extract words from the word elements
    words = []
    for word_elem in word_elements:
        words.extend(word_elem.get_text().split())
    
    return words

def get_disallowed_paths(base_url):
    """Retrieve and parse the robots.txt file for disallowed paths."""
    robots_url = urljoin(base_url, '/robots.txt')
    try:
        response = session.get(robots_url)
        response.raise_for_status()
        robots_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {robots_url}: {e}")
        return []

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
base_url = 'https://www.baseball-reference.com/players/'

all_words = []
limit_dict = {}
prev_words = None

# Check for disallowed paths
disallowed_paths = get_disallowed_paths(base_url)

for letter in letters:
    page_number = 1
    base_url_letter = base_url + letter + "/"

    while True:
        url = f"{base_url_letter}"

        # Skip disallowed paths
        if any(disallowed_path in url for disallowed_path in disallowed_paths):
            print(f"Skipping disallowed URL: {url}")
            break

        try:
            response = session.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:  # Too Many Requests
                retry_after = int(response.headers.get('Retry-After', 5))  # Default retry after 5 seconds
                print(f"Rate limited. Retrying after {retry_after} seconds...")
                time.sleep(retry_after)
                continue
            else:
                logging.error(f"Failed to retrieve page {url}: {e}")
                break
        
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check for specific content that indicates end of pagination
        if "No more results" in soup.get_text():
            print(f"No more results for letter {letter}. Ending scrape.")
            limit_dict[letter] = page_number - 1
            break

        print(f"Processing page: {url}")
        words = scrapping_words(url)
        time.sleep(2)  # Add delay between requests

        if not words:
            print(f"No words found on page {page_number}. Ending scrape.")
            limit_dict[letter] = (page_number - 1)
            break

        if prev_words and are_words_same(prev_words, words):
            print(f"Words on page {page_number} are identical to previous page. Ending scrape for letter {letter}.")
            break

        # Write words to the file
        with open(target_file, 'a', encoding='utf-8', errors='ignore') as file:
            file.write('\n'.join(words) + '\n')

        all_words.extend(words)
        prev_words = words
        page_number += 1

    print(f"Completed scraping for letter '{letter}'. Moving to the next letter.")
    prev_words = None

# Print summary
print("\nAll words collected:")
print(f"Total Number of Words Collected: {len(all_words)}")
print(f"Pages scraped per letter: {limit_dict}")

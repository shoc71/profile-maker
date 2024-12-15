import requests
from bs4 import BeautifulSoup
import string
import time

file_location = "profile_resources/Important/webscrapping/"
file = 'collected_words.txt'
target_file = file_location + file

# Function to scrape words for a given letter
def scrape_words_with_letter(letter):
    # base_url = f"https://scrabble.merriam.com/words/with/{letter}"
    base_url = f"https://word.tips/words-with/{letter}/"
    words = []

    # Make a request to the URL for the current letter
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to access {base_url} for letter '{letter}'")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the word sections (adjust selector if page structure changes)
    word_sections = soup.find_all("div", class_="")  # Specific class for words
    for word_tag in word_sections:
        words.append(word_tag.text.strip())

    return words

# Main function to iterate through all letters from A to Z
def scrape_words_a_to_z():
    all_words = {}

    # Iterate through all letters in the alphabet
    for letter in string.ascii_lowercase:
        print(f"Scraping words with the letter '{letter}'...")
        words = scrape_words_with_letter(letter)
        all_words[letter] = words
        print(f"Found {len(words)} words for letter '{letter}'.")
        time.sleep(1)  # Rate limiting to avoid overloading the server

    return all_words

# Run the scraper
if __name__ == "__main__":
    words_a_to_z = scrape_words_a_to_z()

    # Save results to a file or display them
    with open(target_file, "w") as file:
        for letter, words in words_a_to_z.items():
            file.write(f"Words with '{letter}':\n")
            file.write("\n".join(words) + "\n\n")

    print("Scraping completed. Results saved to 'words_with_a_to_z.txt'.")

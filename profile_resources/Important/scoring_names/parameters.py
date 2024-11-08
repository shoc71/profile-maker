# Imports
import string
from collections import Counter

# Filepath for resources
FILEPATH = 'profile_resources/Important/scoring_names/'

# Define constants for vowels, consonants, numbers, etc.
VOWELS = "AEIOUaeiou"
CONSONANTS = ''.join([letter for letter in string.ascii_letters if letter not in VOWELS])
NUMBERS = string.digits
SEMI_VOWELS = 'YyLlSs'

# Define letter scores
LETTER_SCORES = {
    'E': 10, 'A': 10, 'I': 10, 'L': 10, 'N': 10, 'O': 10, 'R': 10, 'S': 10, 'T': 10, 'U': 10, 
    'D': 9, 'G': 9, 
    'B': 8, 'C': 8, 'M': 8, 'P': 8, 
    'F': 7, 'H': 7, 'V': 7, 'W': 7, 'Y': 7, 
    'K': 6, 
    'Q': 1, 'Z': 1
}

# Load dictionary words, prefixes, and suffixes
with open(FILEPATH + 'dictionary_words.txt', 'r', encoding='utf-8', errors='ignore') as file:
    DICTIONARY_WORDS = [line.strip() for line in file.readlines()]

with open(FILEPATH + 'prefix.txt', 'r', encoding='utf-8', errors='ignore') as file:
    PREFIXES = [line.strip() for line in file.readlines()]

with open(FILEPATH + 'suffix.txt', 'r', encoding='utf-8', errors='ignore') as file:
    SUFFIXES = [line.strip() for line in file.readlines()]

class Parameters:

    # Function to check the number of consecutive consonants
    # @staticmethod
    def check_consonant_streak(name, max_streak=4):
        consonant_count = 0
        for char in name:
            if char in CONSONANTS:
                consonant_count += 1
                if consonant_count >= max_streak:
                    return False
            else:
                consonant_count = 0
        return True
    
    # Function to count vowels in the name
    def count_vowels(name):
        return sum(1 for char in name if char in VOWELS)

    # Function to check if the name has a vowel every 2-3 consonants
    def check_vowel_spacing(name, min_spacing=2, max_spacing=3):
        consonant_count = 0
        vowel_count = 0  # Track the number of vowels found

        for char in name:
            if char in CONSONANTS:
                consonant_count += 1
            elif char in VOWELS:
                vowel_count += 1
                
                # Check if the consonant count violates the spacing rule
                if consonant_count > max_spacing:
                    return False  # Too many consonants before this vowel
                
                # Reset consonant count after finding a vowel
                consonant_count = 0

        # After the loop, check if there were any vowels found
        if vowel_count == 0:
            return False  # No vowels found

        # If there are consonants left at the end, check their count
        if consonant_count > max_spacing:
            return False  # Too many consecutive consonants at the end

        # Check that there are vowels sufficiently spaced
        if vowel_count > 0:
            # Check if the total consonants (counted through the name) divide evenly into the spacing
            total_consonants = sum(1 for char in name if char in CONSONANTS)
            if total_consonants > (vowel_count * max_spacing):
                return False  # More consonants than the allowed spacing with the given vowels

        return True

    # Function to check if the first three letters are consonants
    def check_first_three_consonants(name):
        if len(name) >= 3 and all(char in CONSONANTS for char in name[:3]):
            return True
        return False

    # Function to check if the first three letters contain two or more vowels
    def check_first_three_vowels(name):
        if len(name) >= 3:
            # Get the first three letters
            first_three = name[:3]

            # Find positions of vowels in the first three letters
            vowels_positions = [i for i, char in enumerate(first_three) if char in VOWELS]
            
            # If there are two or more vowels, check their positions
            if len(vowels_positions) >= 2:
                # If vowels are adjacent, apply the rule (no consonant between them)
                if vowels_positions[1] - vowels_positions[0] == 1:
                    return True
                # If there is a consonant between the vowels, allow exception
                elif vowels_positions[1] - vowels_positions[0] == 2:
                    return False  # Exception: two vowels with one consonant in between
        return False

    # Function to check if the name has more than two characters
    def check_name_length(name):
        return len(name) > 3

    # Function to check if the last three letters are consonants
    def check_last_three_consonants(name):
        if len(name) >= 3 and all(char in CONSONANTS for char in name[-3:]):
            return True
        return False

    # Function to check if the word qualifies for the "Skyllr" exception
    def dictionary_word_exception(name):

        # Check if the name exactly matches any word in the dictionary
        for word in DICTIONARY_WORDS:
            if name.strip().lower() == word.strip().lower(): # Ensure case-insensitive exact match
                return True, word # Return True and the exact matching word
        return False, None # No exact match found

    # Function to check if there are 4 or more consecutive letters in alphabetical sequence
    def check_alphabetical_sequence(name, sequence_length=4):
        # Convert the name to lowercase to make it case-insensitive
        name = name.lower()

        # Iterate through the name and check for alphabetical sequences
        for i in range(len(name) - sequence_length + 1):
            # Check if the next `sequence_length` characters are in alphabetical order
            is_alphabetical = True
            for j in range(sequence_length - 1):
                if ord(name[i + j]) + 1 != ord(name[i + j + 1]):
                    is_alphabetical = False
                    break
            if is_alphabetical:
                return True
        return False

    # Function to check for 4 or more consecutive vowels
    def check_consecutive_vowels(name, max_vowel_streak=4):
        vowel_count = 0
        for char in name:
            if char in VOWELS:
                vowel_count += 1
                if vowel_count >= max_vowel_streak:
                    return True  # 4 or more consecutive vowels found
            else:
                vowel_count = 0  # Reset if a consonant is found
        return False  # No 4+ consecutive vowels found

    # Function to check for semi-vowels in the name
    def check_semi_vowels(name):
        # Check if the name contains any vowels
        has_vowels = any(char in VOWELS for char in name)
        
        # If no vowels are present, apply 5 points for semi-vowels
        if not has_vowels:
            return 5  # Apply 5 points when no vowels are present
        
        # If vowels are present, apply 1 point for semi-vowels
        return 1 if any(char in SEMI_VOWELS for char in name) else 0

    def check_prefix(name):
        # Check if the name starts with any of the prefixes
        for prefix in PREFIXES:
            if name.lower().startswith(prefix):
                return True, prefix  # Return True and the matching prefix
        return False, None  # No matching prefix found

    def check_suffix(name):
        # Check if the name ends with any of the suffixes
        for suffix in SUFFIXES:
            if name.lower().endswith(suffix):
                return True, suffix  # Return True and the matching suffix
        return False, None  # No matching suffix found

    def get_letter_frequency_score(name):
        # Convert name to uppercase to match the dictionary keys
        name = name.upper()

        # Create a counter for letter frequencies in the name
        letter_freq = Counter(char for char in name if char in LETTER_SCORES)

        # Calculate the score based on the most frequent letters
        most_frequent_letters = letter_freq.most_common(3)
        
        # Calculate the score of the top 3 frequent letters
        freq_score = sum(LETTER_SCORES[letter] for letter, _ in most_frequent_letters)

        # Calculate the score of the top 3 highest-scoring letters in the name
        high_score_letters = sorted(letter_freq.keys(), key=lambda x: LETTER_SCORES[x], reverse=True)[:3]
        high_score = sum(LETTER_SCORES[letter] for letter in high_score_letters)

        # Return the higher of the two scores
        return max(freq_score, high_score)

    # Function to compute the scramble score
    def scramble_score(name, multiplier=0.5):
        # Convert name to uppercase for consistency
        name = name.upper()

        # Get the lowest possible score (sum of the lowest scoring letters in LETTER_SCORES)
        lowest_possible_score = sum(LETTER_SCORES[letter] for letter in name if letter in LETTER_SCORES)
        
        # The absolute minimum score for any word is the sum of the lowest scoring letters in the dictionary
        absolute_minimum_score = sum(min(LETTER_SCORES.values()) for _ in name if name)

        # Calculate how close the actual score is to the minimum score
        score_difference = lowest_possible_score - absolute_minimum_score

        # Apply the multiplier: The closer to the minimum, the more points deducted
        deduction = score_difference * multiplier

        return max(0, lowest_possible_score - deduction)  # Ensure score doesn't go below 0
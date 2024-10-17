# Imports
import string
from collections import Counter

# Define vowels and consonants
VOWELS = "AEIOUaeiou"
CONSONANTS = ''.join([letter for letter in string.ascii_letters if letter not in VOWELS])
NUMBERS = string.digits
SEMI_VOWELS = 'YyLlSs'
FILEPATH = 'profile_resources/Important/scoring_names/'
LETTER_SCORES = {
    'E': 10, 'A': 10, 'I': 10, 'L': 10, 'N': 10, 'O': 10, 'R': 10, 'S': 10, 'T': 10, 'U': 10, 
    'D': 9, 'G': 9, 
    'B': 8, 'C': 8, 'M': 8, 'P': 8, 
    'F': 7, 'H': 7, 'V': 7, 'W': 7, 'Y': 7, 
    'K': 6, 
    'Q': 1, 'Z': 1
}



# List of basic words for the Skyllr exception
with open (FILEPATH + 'dictionary_words.txt', 'r', encoding='utf-8', errors='ignore') as file:
    DICTIONARY_WORDS = [line.strip() for line in file.readlines()]

with open (FILEPATH + 'prefix.txt', 'r', encoding='utf-8', errors='ignore') as file:
    PREFIXES = [line.strip() for line in file.readlines()]

with open (FILEPATH + 'suffix.txt', 'r', encoding='utf-8', errors='ignore') as file:
    SUFFIXES = [line.strip() for line in file.readlines()]

names_of_interest = []
names_to_remove = []

# Function to check the number of consecutive consonants
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

# Function to score the name based on the parameters and return deductions
def score_name(name):
    score = 100
    deductions = []
    
    # Parameter 1: Names can not shorter than two characters
    if not check_name_length(name):
        score -= 50  # Penalty for too short
        deductions.append("1. <= 3 characters Rule")
    
    # Parameter 2: No more than 5 consecutive consonants
    if not check_consonant_streak(name):
        score -= 100  # Penalty for having more than 5 consecutive consonants
        deductions.append("2. 4+ Consecutive Consonants Rule")
    
    # Parameter 3: Vowel every 2-3 consonants
    if not check_vowel_spacing(name):
        score -= 50  # Penalty for improper vowel spacing
        deductions.append("3. Vowel spacing Rule")

    # Parameter 4: First three consonants
    if check_first_three_consonants(name):
        score -= 50  # Deduct 50 points
        deductions.append("4. First Three Consonants Rule")

    # Parameter 5: First three consonants
    if check_last_three_consonants(name):
        score -= 30  # Deduct 50 points
        deductions.append("5. Last Three Consonants Rule")

    # Parameter 6: First three letters have two or more vowels
    if check_first_three_vowels(name):
        score -= 25  # Deduct 25 points
        deductions.append("6. First Three Vowels Rule")

    # Parameter 7: Basic words Exception
    exception_status, exception_word = dictionary_word_exception(name)
    if exception_status:
        score += 190  # Add points for exception
        deductions.append(f"7. Dictionary Word Exception: '{exception_word}'")

    # Parameter 8: Check for Alphabetical Sequence
    if check_alphabetical_sequence(name):
        score -= 15
        deductions.append("8. Alphabetical Sequence Rule")

    # Parameter 9: 4+ vowels consecutive check
    if check_consecutive_vowels(name):
        score -= 30  # Deduct points
        deductions.append("9. 4+ Consecutive Vowels Rule")

    # Parameter 10: Semi-vowel check
    semi_vowel_score = check_semi_vowels(name)
    if semi_vowel_score > 0:
        score += semi_vowel_score
        deductions.append(f"10. Semi-Vowel Rule: +{semi_vowel_score} points")

    # Parameter 11: Prefix Rule
    prefix_status, prefix = check_prefix(name)
    if prefix_status:
        score += 20  # Deduct points for matching prefix
        deductions.append(f"11. Prefix Rule: '{prefix}'")

    # Parameter 12: Suffix Rule
    suffix_status, suffix = check_suffix(name)
    if suffix_status:
        score += 20  # Deduct points for matching suffix
        deductions.append(f"12. Suffix Rule: '{suffix}'")

    # Parameter 13: Inverse Scramble Rule
    scramble_score = get_letter_frequency_score(name)
    score += scramble_score
    deductions.append(f"13. Inverse Scramble Rule: +{scramble_score} points")
    
    # Cap the score at 100
    score = min(score, 100)

    return max(score, 0), deductions  # Ensure score is not below 0

# Function to score a list of names
def score_names(names_list):
    results = {}
    for names in names_list:
        score, deductions = score_name(names)
        results[names] = {"score": score, "deductions": deductions}
    return results

# Define a custom function to extract the score for sorting
def get_score(item):
    name, details = item # technically a tuple (name, detail)
    return details['score']

# Function to print the names sorted by their score
def print_sorted_names_by_score(scored_names):
    sorted_names = sorted(scored_names.items(), key=get_score, reverse=True)

    for name, details in sorted_names:
        print(f"Name: {name}, Score: {details['score']}, Deductions: {details['deductions']}")

        if details['score'] != 0:
            names_of_interest.append(name)
        else:
            names_to_remove.append(name)

names = []

test_names = '''
Anoprw
Dgimxz
Bfhimq
Ehpqvz
Lwa
afjmrw
gnorvx
Dfgmps
bghlsw
Abejns
ahoprx
pfjpvy
Befmoq
Cimoqw
Aegkop
Hituyz
Abdlnt
Hkqruz
Lmtuwy
lmnop
Adhlsy
Aefruv
Abklor
Celqvy
Bcilwz
Bgknrw
Efijpu
Bgortu
Aegiuv
Mprtwx
Cgnouy
Cdfiju
hinpvz
Bimqux
Bcdgwy
Bdhpqy
cfkpqv
Degknt
Apsuwz
Bdmrux
dgmqxt
'''

test = test_names.split('\n')
for t in test:
    names.append(t.title())

# Output the results
print_sorted_names_by_score(score_names(names))
print(f"Good to use-ish : {names_of_interest}")
print(f"Names to remove : {names_to_remove}")

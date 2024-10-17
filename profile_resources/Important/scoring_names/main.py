# Imports
import string

# Define vowels and consonants
VOWELS = "AEIOUaeiou"
CONSONANTS = ''.join([letter for letter in string.ascii_letters if letter not in VOWELS])
NUMBERS = string.digits
SEMI_VOWELS = 'YyLlSs'

# List of basic words for the Skyllr exception
EXCEPTION_WORDS = ["sky", "star", "moon"]  # Add more words as needed
EXCEPTION_WORDS += ['Rhythm', 'Dry',
'Cry',
'Cyst',
'Gym', 
'Try',
'Spy',
'Hymn',
'Tryst']

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
def basic_word_exception(name):
    # Convert the name to lowercase for case-insensitive matching
    name_lower = name.lower()
    
    # Check if any basic word from exception_words is in the name
    for word in EXCEPTION_WORDS:
        if word in name_lower:
            return True
    return False

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
    for char in name:
        if char in SEMI_VOWELS:
            return True  # Semi-vowel found
    return False  # No semi-vowels found

# Function to score the name based on the parameters and return deductions
def score_name(name):
    score = 100
    deductions = []
    
    # Parameter 1: Names can not shorter than two characters
    if not check_name_length(name):
        score -= 50  # Penalty for too short
        deductions.append("<= 3 characters Rule")
    
    # Parameter 2: No more than 5 consecutive consonants
    if not check_consonant_streak(name):
        score -= 100  # Penalty for having more than 5 consecutive consonants
        deductions.append("4+ Consecutive Consonants Rule")
    
    # Parameter 3: Vowel every 2-3 consonants
    if not check_vowel_spacing(name):
        score -= 50  # Penalty for improper vowel spacing
        deductions.append("Vowel spacing Rule")

    # Parameter 4: First three consonants
    if check_first_three_consonants(name):
        score -= 50  # Deduct 50 points
        deductions.append("First Three Consonants Rule")

    # Parameter 5: First three consonants
    if check_last_three_consonants(name):
        score -= 30  # Deduct 50 points
        deductions.append("Last Three Consonants Rule")

    # Parameter 6: First three letters have two or more vowels
    if check_first_three_vowels(name):
        score -= 25  # Deduct 25 points
        deductions.append("First Three Vowels Rule")

    # Parameter 7: Basic words Exception
    if basic_word_exception(name):
        score += 190  # Add points for exception
        deductions.append("Basic Word Exception")

    # Parameter 8: Check for Alphabetical Sequence
    if check_alphabetical_sequence(name):
        score -= 15
        deductions.append("Alphabetical Sequence Rule")

    # Parameter 9: 4+ vowels consecutive check
    if check_consecutive_vowels(name):
        score -= 30  # Deduct points
        deductions.append("4+ Consecutive Vowels Rule")

    # Parameter 10: Semi-vowel check
    if check_semi_vowels(name):
        score += 2  # Deduct points for having semi-vowels
        deductions.append("Semi-Vowel Rule")
    
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
shh
psst
hmm
boat
nth
north
south
east
aorta
biology
diagram
Euouae
eon
geology
iodine
koala
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
aidi
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

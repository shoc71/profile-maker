# import
import string

LOWERCASE_LETTERS = list(string.ascii_lowercase)
UPPERCASE_LETTERS = list(string.ascii_uppercase)
three_letter_combo = []
first_letter_pos = 0
second_letter_pos = 0
third_letter_pos = 0

while True:

    word = UPPERCASE_LETTERS[first_letter_pos] + \
    LOWERCASE_LETTERS[second_letter_pos] + \
    LOWERCASE_LETTERS[third_letter_pos]

    three_letter_combo.append(word)
    third_letter_pos += 1

    if (first_letter_pos >= (len(LOWERCASE_LETTERS) - 1)) and \
    (second_letter_pos >= (len(LOWERCASE_LETTERS) - 1)) and \
    (third_letter_pos >= (len(LOWERCASE_LETTERS) - 1)):
        
        three_letter_combo.append("Zzz")
        print("all words have been added\n"
              f"{len(three_letter_combo)} words exist.")
        break
    
    if (second_letter_pos >= (len(LOWERCASE_LETTERS) - 1)) and \
    (third_letter_pos > (len(LOWERCASE_LETTERS) - 1)):
        
        # three_letter_combo.append(word)
        third_letter_pos = 0
        second_letter_pos = 0
        first_letter_pos += 1
    
    if third_letter_pos > (len(LOWERCASE_LETTERS) - 1):
        # three_letter_combo.append(word)
        third_letter_pos = 0
        second_letter_pos += 1

# print(three_combo_list)
filepath = "profile_resources/Important/collected_words.txt"
with open(file=filepath, mode='w', encoding='utf-8', errors='ignore') as f:
    three_string_combo = '\n'.join(three_letter_combo)
    f.write(three_string_combo)
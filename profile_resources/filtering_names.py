import string

# global variables
num = 0
pos = 0
count = 0
eng_count = 0
nonsense_count = 0
non_english_words = []
correct_words = []

# target file
filepath_for_names = 'profile_resources/names.txt'

english_characters = list(string.ascii_letters)
additional_characters = ["\'", "-", ".", "…"]
number_characters = list(string.digits)
# additional_characters = ["-"]
total_characters = english_characters + additional_characters + number_characters

with open(filepath_for_names, mode='r', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()

# Main Loop
while num < len(lines):

    # name = target word
    name = lines[num].rstrip("\n")

    # overwrite string out of index error
    while pos < len(name):
    
        # If there is an english character in the correct position of the name
        if (name[pos]) in total_characters:
            # print("Confirmed Hit")
            pos += 1
            eng_count += 1

            # If no english character is found in this position
            if pos >= len(name):
                correct_words.append(name)
                pos = 0
                count += 1
                break

        # If there is no english character in the word of the name of the current position
        elif (name[pos]) not in total_characters:
            non_english_words.append(name)
            nonsense_count += 1
            # print("Found non ascii_letter character")
            count += 1
            pos = 0
            break

    num += 1
    pos = 0

    if count >= len(lines):  # Exit condition for the main loop
        print("Gone through the specified number of iterations.\nEnd of Program.\n")
        break

print(f"Words in accepted list : {len(correct_words)}",
      f"\n\nWords not in accepted list : {non_english_words}\n\n",
      f"Non-English Character Count : {nonsense_count}\n",
      f"English Character Count : {eng_count}\n",
      f"Number of times loop has run : {count}")
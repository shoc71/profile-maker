#imports
import string

try:
    from profile_resources.Important.special_characters import special_list_all
except:
    from special_characters import special_list_all

# global variables
name_position = 0
char_position = 0
loop_count = 0
english_count = 0
nonsense_count = 0
non_english_words = {}
correct_words = []

# target file
filepath_for_names = 'profile_resources/names.txt'

english_characters = list(string.ascii_letters)
additional_characters = [".", "…"] # ("-", "\'") was taken out
number_characters = list(string.digits)
total_characters = english_characters + additional_characters + number_characters + special_list_all

with open(filepath_for_names, mode='r', encoding='utf-8', errors='ignore') as file:
    notepad_lines = file.readlines()

# Main Loop
while name_position < len(notepad_lines):

    # name = target word
    name = notepad_lines[name_position].rstrip("\n")

    # overwrite string out of index error
    while char_position < len(name):
    
        # If there is an english character in the correct position of the name
        if (name[char_position]) in total_characters:
            # print("Confirmed Hit")
            char_position += 1
            english_count += 1

            # If no english character is found in this position
            if char_position >= len(name):
                correct_words.extend(name)
                char_position = 0
                loop_count += 1
                break

        # If there is no english character in the word of the name of the current position
        elif (name[char_position]) not in total_characters:
            non_english_words[name_position - 1] = name
            nonsense_count += 1
            # print("Found non ascii_letter character")
            loop_count += 1
            char_position = 0
            break

    name_position += 1
    char_position = 0

    if loop_count >= len(notepad_lines):  # Exit condition for the main loop
        print("Gone through the specified number of iterations.\nEnd of Program.\n")
        break

print(f"Words in accepted list : {len(correct_words)}",
      f"\n\nWords not in accepted list : {non_english_words}\n\n",
      f"Non-English Character Count : {nonsense_count}\n",
      f"English Character Count : {english_count}\n",
      f"Number of times loop has run : {loop_count}")
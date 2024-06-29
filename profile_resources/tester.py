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

with open(filepath_for_names, mode='r', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()

# Main Loop
while num < len(lines):
    name = lines[num].rstrip("\n")

    while pos < len(name):
        if name[pos] in english_characters:
            pos += 1
            eng_count += 1

            if pos >= len(name):
                correct_words.append(name)
                pos = 0
                count += 1
                break

        else:
            non_english_words.append(name)
            nonsense_count += 1
            pos = 0
            count += 1
            break

    num += 1
    pos = 0

    if count >= 30:  # Exit condition for the main loop
        print("Gone through the specified number of iterations.\nEnd of Program.\n")
        break

print(f"Words in accepted list: {correct_words}\n",
      f"\n\nWords not in accepted list: {non_english_words}\n\n",
      f"Non-English Character Count: {nonsense_count}\n",
      f"English Character Count: {eng_count}\n",
      f"Number of times loop has run: {count}")

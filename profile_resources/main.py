import random
from Important.remove_tabs_n_spaces import *
'''
After crossing 100_000 unique names, the program began to slow down SIGNIFICANTLY.
I wanted to quickly input the random names/words into the list and check if there were
unique cases of it or not.
'''
filepath_for_names = 'profile_resources/names.txt'
filepath_for_test = 'profile_resources/input.txt'

while True:
    with open (filepath_for_test, 'r', encoding='utf-8') as f:
        test_list = f.readlines()

    with open (filepath_for_names, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"Number of contents in names.txt before -{len(lines)}-")
        string_lines = ','.join(lines).title()
        line = list(set(string_lines.split(',') + test_list))
        shuffled_list = random.sample(line, len(line))

    with open (filepath_for_names, 'w', encoding='utf-8') as f:
        print(f"Number of contents in names.txt after -{len(shuffled_list)}-")
        writing_string_line = ''.join(shuffled_list).title()
        f.write(writing_string_line)

    with open (filepath_for_test, 'w', encoding='utf-8') as f:
        f.write('')

    if len(shuffled_list) != len(lines):
        print(f"Difference of -[{(len(shuffled_list) - len(lines))}]- words.\n")
    else:
        print("No Change! :)")
        break
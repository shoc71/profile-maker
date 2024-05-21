# Imports
import random
from Important.remove_tabs_n_spaces import *
'''
After crossing 100_000 unique names, the program began to slow down SIGNIFICANTLY.
I wanted to quickly input the random names/words into the list and check if there were
unique cases of it or not.
'''
# Filepaths and Files
filepath_for_names = 'profile_resources/names.txt'
filepath_for_input = 'profile_resources/input.txt'

# Loop until All Instances of That Case Are Removed
while True:
    
    #  Opening and Reading Input File
    with open (filepath_for_input, 'r', encoding='utf-8') as f:
        input_list = f.readlines()
        
    # Opening and Reading Names File
    with open (filepath_for_names, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"Number of contents in names.txt before input -{len(lines)}-")
        string_lines = ','.join(lines).title()
        
        # Removing any duplicates when merging New Inputs and Current Names List
        line = list(set(string_lines.split(',') + input_list))
        
        # Shuffling the List for Variance
        shuffled_list = random.sample(line, len(line))

    # Opening and Writing Names List
    with open (filepath_for_names, 'w', encoding='utf-8') as f:
        print(f"Number of contents in names.txt after input -{len(shuffled_list)}-\n")
        writing_string_line = ''.join(shuffled_list).title()
        f.write(writing_string_line)

    # Emptying the Input List
    with open (filepath_for_input, 'w', encoding='utf-8') as f:
        f.write('')

    # UI - difference in list size until they equal the same 
    if len(shuffled_list) != len(lines):
        print(f"Difference of -[{(len(shuffled_list) - len(lines))}]- words bewteen Old and New Names.txt file(s).\n")
    else:
        
        # Break the loop when no more duplicates are found
        print("Input.txt has been cleared and ready to use.")
        print("End of Program. No Changes to Report :)\n")
        break
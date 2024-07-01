# Imports
import random
from Important.remove_tabs_n_spaces import *
from Important import tracker

# Docstring
'''
After crossing 100_000 unique names, the program began to slow down SIGNIFICANTLY.
I wanted to quickly input the random names/words into the list and check if there were
unique cases of it or not.
'''
# Filepaths and Files
# filepath_for_names = 'profile_resources/temp.txt'
filepath_for_names = 'profile_resources/names.txt'
filepath_for_input = 'profile_resources/input.txt'
filepath_for_tracker = 'profile_resources/Important/tracker.txt'

# Loop until All Instances of That Case Are Removed
while True:
    
    #  Opening and Reading Input File
    with open (filepath_for_input, 'r', encoding='utf-8', errors='ignore') as f:
        input_list = f.readlines()
        
    # Opening and Reading Names File
    with open (filepath_for_names, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        lines_list_counted = len(lines)
        print(f"Number of contents in names.txt before input -{lines_list_counted}-")

        string_lines = ','.join(lines).title()
        
        # Removing any duplicates when merging New Inputs and Current Names List
        line = list(set(string_lines.split(',')))
        line = list(set(line + input_list))
        
        # Shuffling the List for Variance
        shuffled_list = random.sample(line, len(line))
        shuffled_list_counted = len(shuffled_list)

    # if there's nothing in the text_file then break loop
        if (lines_list_counted <= 0) and (shuffled_list_counted <=0):
            print("Add some random stuff to the input.txt file.")
            break

    # Opening and Writing Names List
    with open (filepath_for_names, 'w', encoding='utf-8', errors='ignore') as f:
        print(f"Number of contents in names.txt after input -{shuffled_list_counted}-\n")
        writing_string_line = ''.join(shuffled_list).title()
        f.write(writing_string_line)

    # Emptying the Input List
    with open (filepath_for_input, 'w', encoding='utf-8', errors='ignore') as f:
        f.write('')

    # UI - difference in list size until they equal the same 
    if shuffled_list_counted != lines_list_counted:
        print(f"Difference of -[{shuffled_list_counted - lines_list_counted}]- words bewteen Old and New Names.txt file(s).\n")
    else:
        
        # Break the loop when no more duplicates are found
        format_possibilities = '{:0.3e}'.format(lines_list_counted ** 2) # underrated way to round big numbers
        print("Input.txt has been cleared and ready to use.")
        print(f"There are now -{format_possibilities}- number of possibilities,\
 (Assuming a First and Last name only.)")
        print("End of Program. No Changes to Report :)\n")
        
        # Keeping Track of all the instances this program has been run (for fun from now on.)
        tracker.track_program_runs(filepath_for_tracker)
        break
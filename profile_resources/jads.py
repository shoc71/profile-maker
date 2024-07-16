# Imports
import random
import time
import os

start_time = time.time()
# from Important.remove_tabs_n_spaces import *
# from Important import program_tracker

# Docstring
'''
After crossing 1_000_000 unique names, I could no longer open up the text files normally.
I wanted to quickly input the random names/words into the list and check if there were
unique cases of it or not and split them up so they are always random and unqiue.

All the names have been split among all the other notepads with each one containing 
100_000, with exception to the last one. 
'''
# Filepaths and Files
# filepath_for_names = 'profile_resources/temp.txt'
# filepath_for_names = 'profile_resources/names_list/names.txt'
filepath_for_input = 'profile_resources/input.txt'
filepath_for_tracker = 'profile_resources/Important/tracker.txt'
list_dir_of_names = 'profile_resources/names_list/'
names_list=[]
names_of_name = []

def read_notepad(file):
    """
    Opening up a notepad to read the contents inside, while removing the redundancy 
    of opening the file over and over again.

    Arguments:
    file = filename and filepath
    
    RETURNS:
        A list of strings split on spaces
    """
    with open(file=file, mode='r', encoding='utf-8', errors='ignore') as file:
        lines = file.read().splitlines()
    return lines

# while True:
files = os.listdir(list_dir_of_names)

for file in files:
    names_list.append(list_dir_of_names + file)

for names in names_list:
    names_of_name += read_notepad(file=names)

names_of_name += read_notepad(file=filepath_for_input)
name_of_names_count = len(names_of_name)

combined_names = list(set(names_of_name))
random.shuffle(combined_names)
combined_names_count = len(combined_names)

if (combined_names_count <= 0) and (name_of_names_count <= 0):
    print("Add some content in any of the files.")
    # break

if (combined_names_count) != (name_of_names_count):
    print(f"Difference of -[{combined_names_count - name_of_names_count}]- words bewteen Old and New Names.txt file(s).\n")

if (combined_names_count) == (name_of_names_count):
    pass

'''
# Loop until All Instances of That Case Are Removed
while True:
    
    #  Opening and Reading Input File
    with open (filepath_for_input, 'r', encoding='utf-8', errors='ignore') as f:
        input_list = f.read().splitlines() # Read lines and remove newline characters
        
    # Opening and Reading Names File
    with open (filepath_for_names, 'r', encoding='utf-8', errors='ignore') as f:
        current_names = f.read().splitlines() # Read lines and remove newline characters
        
    current_names_count = len(current_names)
    print(f"Number of contents in names.txt before input: {current_names_count}")

    string_lines = ','.join(current_names).title()
    
    # Removing any duplicates when merging New Inputs and Current Names List
    line = list(set(string_lines.split(',')))
    line = list(set(line + input_list))
    
    combined_names = list(set(current_names + input_list))
    random.shuffle(combined_names)
    combined_names_count = len(combined_names)

    # if there's nothing in the text_file then break loop
    if (current_names_count <= 0) and (combined_names_count <=0):
        print("Add some random stuff to the input.txt file.")
        break

    # Opening and Writing Names List
    with open (filepath_for_names, 'w', encoding='utf-8', errors='ignore') as f:
        print(f"Number of contents in names.txt after input: {combined_names_count}\n")
        writing_string_line = '\n'.join(combined_names) # Join list into a string with newlines and write to file
        f.write(writing_string_line)

    # Emptying the Input List
    with open (filepath_for_input, 'w', encoding='utf-8', errors='ignore') as f:
        f.write('')

    # UI - difference in list size until they equal the same 
    if combined_names_count != current_names_count:
        print(f"Difference of -[{combined_names_count - current_names_count}]- words bewteen Old and New Names.txt file(s).\n")
        
    else:
        
        # Break the loop when no more duplicates are found
        end_time = time.time()
        total_run_time = program_tracker.formatted_runtime(start_time=start_time, end_time=end_time)
        format_possibilities = '{:0.3e}'.format(current_names_count ** 2) # underrated way to round big numbers
        print(f"Input.txt has been cleared and is ready to use.\n"
              f"There are now -{format_possibilities}- number of possibilities, "
              f"(Assuming a First and Last name only).\n"
              f"Elapsed time: {total_run_time} to run.\n"
              f"End of Program. No Changes to Report :)\n")
              
        # Keeping Track of all the instances this program has been run (for fun from now on.)
        program_tracker.track_program_runs(filepath_for_tracker, combined_names_count)
        break
'''
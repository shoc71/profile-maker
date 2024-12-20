# Imports
import random
import time
import os

start_time = time.time()
from Important.remove_tabs_n_spaces import *
from Important.tracker import program_tracker
from Important import notepad

# Docstring
'''
After crossing 1_000_000 unique names, I could no longer open up the text files normally.
I wanted to quickly input the random names/words into the list and check if there were
unique cases of it or not and split them up so they are always random and unqiue.

All the names have been split among all the other notepads with each one containing 
100_000, with exception to the last one. 
'''
# Filepaths and Files
filepath_for_input = 'profile_resources/input.txt'
filepath_for_tracker = 'profile_resources/Important/tracker/tracker.txt'
list_dir_of_names = 'profile_resources/names_list/'
divisible_count = 100_000

while True:
    names_list = []
    current_names = []

    files = os.listdir(list_dir_of_names)

    for file in files:
        names_list.append(list_dir_of_names + file)

    for names in names_list:
        current_names += notepad.notepad_function(file=names, mode='r')

    string_lines = ','.join(current_names).title()

    input_list = notepad.notepad_function(file=filepath_for_input, mode='r')
    line = list(set(string_lines.split(',')))

    combined_names = list(set(line + input_list))
    random.shuffle(combined_names)

    current_names_count = len(current_names)
    combined_names_count = len(combined_names)

    print(f"Before run: {current_names_count}\nAfter run: {combined_names_count}\n")
    notepad_count = int(round((combined_names_count / 100_000), 0)) # rounding up

    print(f"Number of list names: {notepad_count}\n")

    for i in range(1, notepad_count + 1):
        if i <= 999:
            file_name = f"{list_dir_of_names}names_{i:03d}.txt" # game breaking
            combined_names = notepad.writing_into_file(total_list=combined_names, file_name=file_name, divisible_count=divisible_count)

    combined_names = []

    if (combined_names_count <= 0) and (current_names_count <= 0):
        print("Add some content in any of the files.")
        break

    elif (combined_names_count) != (current_names_count):
        print(f"Difference of -[ {combined_names_count - current_names_count} ]- words bewteen Old and New Names.txt file(s).\n")

    elif (combined_names_count) == (current_names_count): 
        end_time = time.time()
        total_run_time = program_tracker.formatted_runtime(start_time=start_time, end_time=end_time)
        format_possibilities = '{:0.3e}'.format(current_names_count ** 2) # underrated way to round big numbers
        print(f"Input.txt has been cleared and is ready to use.\n"
                f"There are now -{format_possibilities}- number of possibilities, ", end=""
                f"(Assuming a First and Last name only).\n"
                f"Elapsed time: {total_run_time}.\n"
                f"End of Program. No Changes to Report :)\n")
                
        # Keeping Track of all the instances this program has been run (for fun from now on.)
        program_tracker.track_program_runs(filepath_for_tracker, combined_names_count, total_run_time)
        break
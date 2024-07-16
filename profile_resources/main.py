# Imports
import random
import time
import os

start_time = time.time()
from Important.remove_tabs_n_spaces import *
from Important import program_tracker
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
filepath_for_tracker = 'profile_resources/Important/tracker.txt'
list_dir_of_names = 'profile_resources/names_list/'
names_list = []
names_of_name = []
divisible_count = 100_000

while True:
    files = os.listdir(list_dir_of_names)

    for file in files:
        names_list.append(list_dir_of_names + file)

    for names in names_list:
        names_of_name += notepad.notepad_function(file=names, mode='r')

    names_of_name += notepad.notepad_function(file=filepath_for_input, mode='r')
    name_of_names_count = len(names_of_name)

    combined_names = list(set(names_of_name))
    random.shuffle(combined_names)
    combined_names_count = len(combined_names)

    print(f"Before run: {name_of_names_count}\nAfter run: {combined_names_count}\n")
    notepad_count = int(round((combined_names_count / 100_000), 0) + 1) # rounding up

    print(f"Number of list names: {notepad_count}\n")

    if (combined_names_count <= 0) and (name_of_names_count <= 0):
        print("Add some content in any of the files.")
        break

    if (combined_names_count) != (name_of_names_count):
        print(f"Difference of -[{combined_names_count - name_of_names_count}]- words bewteen Old and New Names.txt file(s).\n")
    
    else: 
        for i in range(1, notepad_count + 1): # ranges end 1 before, so the +1 is to make up for it
            if i <= 9:
                file_name = (f"{list_dir_of_names}names_000{i}.txt")
                combined_names = notepad.writing_into_file(total_list=combined_names, file_name=file_name, divisible_count=divisible_count)

            elif (i > 9) and (i <= 99):
                file_name = (f"{list_dir_of_names}names_00{i}.txt")
                combined_names = notepad.writing_into_file(total_list=combined_names, file_name=file_name, divisible_count=divisible_count)

            elif (i > 99) and (i <= 1000):
                file_name = (f"{list_dir_of_names}names_0{i}.txt")
                combined_names = notepad.writing_into_file(total_list=combined_names, file_name=file_name, divisible_count=divisible_count)

        # Break the loop when no more duplicates are found
        end_time = time.time()
        total_run_time = program_tracker.formatted_runtime(start_time=start_time, end_time=end_time)
        format_possibilities = '{:0.3e}'.format(name_of_names_count ** 2) # underrated way to round big numbers
        print(f"Input.txt has been cleared and is ready to use.\n"
                f"There are now -{format_possibilities}- number of possibilities, "
                f"(Assuming a First and Last name only).\n"
                f"Elapsed time: {total_run_time}.\n"
                f"End of Program. No Changes to Report :)\n")
                
        # Keeping Track of all the instances this program has been run (for fun from now on.)
        program_tracker.track_program_runs(filepath_for_tracker, combined_names_count, total_run_time)
        break
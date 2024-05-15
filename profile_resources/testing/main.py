from profile_resources.testing.remove_tabs_n_spaces import *

filename_test = 'test.txt'
filename_adding_on = 'profile_resources/names.txt'
empty_string = ''

# def read_notepad(notepad_name):
#     with open (notepad_name, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#     f.close()
#     return lines

def write_notepad(notepad_name, string):
    with open(notepad_name, 'w', encoding='utf-8') as file:
        file.write(string)
    file.close()

with open (filename_test, 'r', encoding='utf-8') as f:
    lines = f.readlines()
f.close()

with open (filename_adding_on, 'r+', encoding='utf-8') as file:
    more_lines = file.readlines()
    mf_lines = more_lines + lines
    merging_string = '\n'.join(mf_lines)
f.close()

# read_notepad(filename_test)
# read_notepad(filename_adding_on)
write_notepad(filename_test, empty_string)
write_notepad(filename_adding_on, merging_string)

from profile_resources.testing.fast_unique_name_check import *

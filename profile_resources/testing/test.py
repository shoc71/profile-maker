# imports
import random
from remove_tabs_n_spaces import *

# filenames and their paths
filename_test = 'profile_resources/testing/test.txt'
filename_names = 'profile_resources/names.txt'
empty_string = ''
list_prime = []

# Log function
def log(message):
    print(message)

def list_to_str_conversion(list_prime):
    """Convert a list of strings to a single string with each word in title case."""
    string_prime = ''.join(list_prime).title()
    return string_prime

def shuffle_and_remove_duplicates(lines):
    """Shuffle the list of strings and remove duplicates."""
    lines_of_strings = list_to_str_conversion(lines)
    list_line = list(set(lines_of_strings.split(',')))
    shuffled_list = random.sample(list_line, len(list_line))
    return shuffled_list

# Reading Notepad Function
def readnote(filename_and_path):
    try:
        with open(filename_and_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            sum_fap = len(lines)
            log(f"Amount of content in this txt is {sum_fap}.")
            return lines
    except FileNotFoundError:
        log(f"File {filename_and_path} not found.")
        return []

# Writing Notepad Function
def writenote(filename_and_path, content, method, shuffle=False):
    if shuffle:
        content = shuffle_and_remove_duplicates(content)
    
    contents = list_to_str_conversion(content)
    sum_con = len(contents)
    
    try:
        if method == "write":
            with open(filename_and_path, 'w', encoding='utf-8') as f:
                f.write(contents)
                log(f"'{sum_con}' Contents have been written to '{filename_and_path}' successfully.")
        elif method == "append":
            with open(filename_and_path, 'a', encoding='utf-8') as f:
                f.write(contents)
                log(f"'{sum_con}' Contents have been appended to '{filename_and_path}' successfully.")
    except Exception as e:
        log(f"An error occurred: {e}")

# Main Logic
formatted_data = readnote(filename_test)
existing_data = readnote(filename_names)
if formatted_data:
    list_prime.extend(existing_data)
    list_prime.extend(formatted_data)
    string_prime = shuffle_and_remove_duplicates(list_prime)
    writenote(filename_names, content=string_prime, method="write")
    writenote(filename_test, empty_string, method="write")
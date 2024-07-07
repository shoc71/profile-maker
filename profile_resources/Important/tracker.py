import re
import time

def track_program_runs(notepad_file):

    with open (notepad_file, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.read().split("\n")

    for line in lines:
        track_program_run_count(line)

    with open (notepad_file, 'w', encoding='utf-8', errors='ignore') as file:
        file.write(lines)

def track_program_run_count(string: str) -> str:
    all_numbers_found_in_txt = re.findall(r'[0-9]', string)
    check = re.search(r"^Number.run :[0-9]$", string)
    if check:
        print("match")
        print(check)

    print(all_numbers_found_in_txt)
    string_number = ''.join(all_numbers_found_in_txt)

    if all_numbers_found_in_txt:
        formatted_int_numbers = int(string_number)
        # print(f"Before adding up the count : {formatted_int_numbers}")

        string = string.replace(string_number, str(formatted_int_numbers + 1))
        
        return string

    else:
        print("No number was found!")



def track_program_last_run(string):
    pass

file = 'profile_resources/Important/tracker.txt'
print(track_program_runs(file))
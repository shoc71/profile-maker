import re

# file = 'tracker.txt'

def track_program_runs(notepad_file):

    with open (notepad_file, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.read()

    all_numbers_found_in_txt = re.findall(r'[0-9]', lines)
    string_number = ''.join(all_numbers_found_in_txt)

    if all_numbers_found_in_txt:
        formatted_int_numbers = int(string_number)
        # print(f"Before adding up the count : {formatted_int_numbers}")

    else:
        print("No number was found!")

    lines = lines.replace(string_number, str(formatted_int_numbers + 1))

    with open (notepad_file, 'w', encoding='utf-8', errors='ignore') as file:
        file.write(lines)
    

# print(track_program_runs(file))
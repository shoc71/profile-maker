import re
import time
import os

'''
total count and last runtime
'''

def track_program_runs(notepad_file, total_name_count, runtime):

    with open (notepad_file, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.read()
    
    lines = notepad_count_tracker(lines)
    lines = track_program_last_run(lines)
    lines = track_program_run_count(lines)
    lines = notepad_word_count(lines, total_name_count)
    lines = program_runtime(lines, runtime)

    with open (notepad_file, 'w', encoding='utf-8', errors='ignore') as file:
        file.write(lines)

def track_program_run_count(string: str) -> str:
    def replacement(match):
        number = int(match.group(1))
        return f"Number of times this code has been run : {number + 1}"
    string = re.sub(r"^Number of times this code has been run : (\d+)$", replacement, string, flags=re.MULTILINE)
    return string    

def track_program_last_run(string: str) -> str:
    current_time = time.strftime("%d/%b/%Y on %H:%M:%S")
    string = re.sub(r"^Code was last run on .*", f"Code was last run on {current_time}", string, flags=re.MULTILINE)
    return string

def notepad_count_tracker(string: str) -> str:
    path_to_dir = 'profile_resources/names_list/'
    files = os.listdir(path_to_dir)
    count = len(files)
    string = re.sub(r"^Number of notepad containing all the names: \d+$", f"Number of notepad containing all the names: {count}", string, flags=re.MULTILINE)
    return string

def notepad_word_count(string: str, count: int) -> str:
    string = re.sub(r"^Total Number of Names: \d+$", f"Total Number of Names: {count}", string, flags=re.MULTILINE)
    return string

def program_runtime(string: str, runtime):
    string = re.sub(r"^Last run_time of the program was:.*$", f"Last run_time of the program was: {runtime}", string, flags=re.MULTILINE)
    return string

def formatted_runtime(start_time, end_time):
    total_seconds = end_time - start_time

    days, remainder = divmod(total_seconds, 86_400)
    hours, remainder = divmod(remainder, 3_600)
    minutes, remainder = divmod(remainder, 60)
    seconds, milliseconds = divmod(remainder, 1)

    # Convert milliseconds to integer and format it to three decimal places
    milliseconds = int(milliseconds * 1000)

    formatted_time=''
    if days > 0:
        formatted_time += f"{days} days"
    if hours > 0:
        formatted_time += f"{hours} hours"
    if minutes > 0:
        formatted_time += f"{minutes} minutes"
    if seconds > 0 or milliseconds > 0:
        formatted_time += f"{seconds}{milliseconds:03} seconds" #rounded to 3 decimals places

    return formatted_time
    # reason for if - every condition should be evaluated
    # elif - implies the rest should not be evaluated if one of the many conditions, ring true
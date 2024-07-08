import re
import time

def track_program_runs(notepad_file):

    with open (notepad_file, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.read()

    lines = track_program_last_run(lines)
    lines = track_program_run_count(lines)

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

# file = 'profile_resources/Important/tracker.txt'
# print(track_program_runs(file))
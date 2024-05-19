# imports
import random, time, datetime
from tqdm import tqdm
# pip install keyboard (if necessary)
import keyboard  # To detect key presses

# variable names
start_time = time.time()
filename = 'profile_resources/names.txt'
new_list = []
dup_list = []

# reading names.txt file
with open (filename, mode='r', encoding='utf-8') as f:
    line = f.readlines()

# making everything the same and then putting it back into a list for it to be checked
lines = ','.join(line).title() # <-- converting to title case is important here
line = lines.split(',') # converting into a list, set makes things weird

# printing start of program
print(f"\nThis program has started on {datetime.datetime.now()}\n")
print(f"Processing file \'{filename}\' that contains -{len(line)}- different names")

# progress bar for the illusion of the program completing itself
with tqdm(total=len(line), dynamic_ncols=True) as pbar:    
    for i in line:
        if keyboard.is_pressed('esc'):
            print("\nEscape key pressed. Terminating the loop.")
            break
        if i not in new_list:
            new_list.append(i)
        else:
            dup_list.append(i)
        pbar.update(1)
        remaining = len(line) - pbar.n  # Calculate the remaining iterations
        eta_seconds = remaining * (time.time() - start_time) / pbar.n if pbar.n > 0 else 0
        eta_str = time.strftime("%H:%M:%S", time.gmtime(eta_seconds))
        pbar.set_description(f"ETA: {eta_str}")

# putting a list into a string -- very necessary step for formatting
if new_list:
    new_list = random.sample(new_list, len(new_list))
    new_list = ''.join(new_list).title()  # Consistency for title case

# statistics calculations and rounding
seconds = (time.time() - start_time)
minutes = seconds / 60
calc_percent = len(dup_list) / len(line)
seconds = round(seconds, 3)
minutes = round(minutes, 2)
calc_percent = round((calc_percent * 100), 4)

# printing the end of the program
if dup_list:
    print(f"List of duplicates: {dup_list} \n")
    print(f"List before program is <{len(line)}> and new list count now <{len(line) - len(dup_list)}>")
    print(f"This is the number of duplicates you have: {len(dup_list)} - {calc_percent}% list reduction \n")
    print(f"This code took --- {seconds} seconds --- to run")
    print(f"This code took --- {minutes} minutes --- to finish \n")
    print(f"Program has been finished on {datetime.datetime.now()}")

    # rewriting the actual file
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(new_list)
        
else:
    print("No changes. Program was terminated early")
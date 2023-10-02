'''
set is faster but I like the dup_list better despite the longer time it takes but this works too...
'''

# imports
import random, time, datetime
from tqdm import tqdm
# from alive_progress import alive_bar

# variable names
start_time = time.time()
filename = "names.txt"
# list1 = []
new_list = []
dup_list = []

# reading names.txt file
with open (filename, mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    # line = str(line).title()
    # line = list(list)
    # list1.append(line)

# making everything the same and then putting it back into a list for it to be checked
prev = len(lines)
l = set(lines)
lines = ''.join(l).title()
new = len(lines)
print(lines)

print(f"list reduction of {prev} to {new} with a difference of {new - prev}")

import random
'''
After crossing 100_000 unique names, the program began to slow down SIGNIFICANTLY.
I wanted to quickly input the random names/words into the list and check if there were
unique cases of it or not.
'''
filepath = 'profile_resources/names.txt'

with open (filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(len(lines))
    string_lines = ','.join(lines).title()
    line = list(set(string_lines.split(',')))
    shuffled_list = random.sample(line, len(line))
f.close()

with open (filepath, 'w', encoding='utf-8') as f:
    print(len(shuffled_list))
    writing_string_line = ''.join(shuffled_list).title()
    f.write(writing_string_line)
f.close()

if len(shuffled_list) != len(lines):
    print(f"Difference of -{(len(lines) - len(shuffled_list))}- words.")
else:
    print("No Change! :)")
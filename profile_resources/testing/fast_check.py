import os
'''
After crossing 100_000 unique names, the program began to slow down SIGNIFICANTLY.
I wanted to quickly input the random names/words into the list and check if there were
unique cases of it or not.
'''
# filepath = 'test.txt'
filepath = r'C:\\Users\\Sonu\\Documents\\GitHub\\profile-maker\\profile_resources\\testing\\test.txt'

with open (filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
print(len(lines))
string_lines = ','.join(lines).title()
line = string_lines.split(',')
print(type(line))
churning = set(string_lines)
print(len(churning))
    
print(churning)
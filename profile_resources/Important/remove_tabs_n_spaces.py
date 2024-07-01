# imports
try: 
    from Important.add_on_list import char_list, indent_list, extras_list, space_dash_list, brands_list
except:
    from add_on_list import char_list, indent_list, extras_list, space_dash_list, brands_list

# Filepath and File
filepath = 'profile_resources/input.txt'
new_list = []

# Formating any mentioned characters
def formatting_string(list_of_str: str, replace: str) -> str:
    global linestr
    linestr = str(linestr)

    for line in range(len(list_of_str)):
        linestr = linestr.replace(list_of_str[line], replace)
    return linestr

# Removing any extras space
def remove_extras(string: str) -> str:
    lirt = str(string).split("\n")
    n_list = list(dict.fromkeys(lirt))
    lirt_str = '\n'.join(n_list)
    return lirt_str

# Splitting Title Case Words
def split_title_case(string: str) -> str:
    newstring = ''
    skip_processing = False
    
    for letter in string:
        if letter == '-':
            skip_processing = True
            newstring += letter
        elif skip_processing:
            if letter == '\n':  # Remove newline after dash
                continue
            else:
                skip_processing = False
                newstring += letter.upper()  # Convert to uppercase after dash
        elif letter == letter.upper() and letter.isalpha():
            newstring += '\n' + letter
        else:
            newstring += letter
    
    return newstring

# Fixing apostrophe
def remove_extreme_apostrophe(name: str) -> str:

    # Remove leading/trailing whitespace and newlines
    name = name.strip()

    # Remove apostrophe at the start
    if name.startswith("'"):
        name = name[1:]

    # Remove apostrophe at the end
    if name.endswith("'"):
        name = name[:-1]

    # Ensure apostrophe is followed by a lowercase letter
    parts = name.split("'")
    for i in range(1, len(parts)):
        if parts[i] and (parts[i][0].isupper() and not parts[i][0].isdigit()):
            parts[i] = parts[i][0].lower() + parts[i][1:]
    name = "'".join(parts)

    return name

# Opening and Reading Input File
with open (filepath, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
    linestr = ''.join(lines)
    linestr_list = linestr.strip().split("\n")

    for line in linestr_list:
        fixed_linestr = remove_extreme_apostrophe(line)
        # print(f"Original: {line} => Fixed: {fixed_linestr}")
        new_list.append(fixed_linestr)

    linestr = '\n'.join(new_list)
    linestr = split_title_case(linestr)
    linestr = formatting_string(space_dash_list, "\n")
    linestr = formatting_string(indent_list, '\n')
    linestr = formatting_string(char_list, '\n')
    linestr = formatting_string(extras_list, '\n')
    linestr = formatting_string(brands_list, '\n')
    linestr = remove_extras(linestr)#.replace("	","")
    # print(linestr)

# Writing on File and UI of the Number of Contents in Input.txt
with open(filepath, 'w', encoding='utf-8', errors="ignore") as f:
    f.write(linestr)
    print("\nProgram remove_tabs_n_spaces.py has run succesfully.")
    print(f"The number of contents in input.txt is -{len(lines)}-\n")
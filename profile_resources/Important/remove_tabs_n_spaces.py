# imports
try: 
    from character_filter.formatting_list_contents import indent_list
    from character_filter.brands import brands_list
    from character_filter.extras_and_emojis import extras_list
    from character_filter.character_list import char_list
    from character_filter.special_characters import special_list_all
except:
    from Important.character_filter.formatting_list_contents import indent_list
    from Important.character_filter.brands import brands_list
    from Important.character_filter.extras_and_emojis import extras_list
    from Important.character_filter.character_list import char_list
    from Important.character_filter.special_characters import special_list_all

# Filepath and File
filepath = 'profile_resources/input.txt'
space_list = [' ', '–', "−"]

# there are special characters like emojis and different_spaces that I don't want included in the names list
LIST_FILTERING = indent_list + brands_list + extras_list + char_list + special_list_all + space_list

# Formating any mentioned characters
def formatting_string(list_of_str, replace) -> str:
    global linestr
    linestr = str(linestr)
    for line in range(len(list_of_str)):
        linestr = linestr.replace(list_of_str[line], replace)
    return linestr

# Removing any extras space
def remove_extras(string : str) -> str:
    lirt = str(string).split("\n")
    n_list = list(dict.fromkeys(lirt))
    lirt_str = '\n'.join(n_list)
    return lirt_str

# Splitting Title Case Words
def split_title_case(string : str) -> str:
    newstring = ''
    for letter in string:
        # Check if character is uppercase and a letter
        if letter == letter.upper() and letter.isalpha():
            newstring += '\n' + letter
        else:
            newstring += letter
    return newstring


# Fixing apostrophe
def fixing_apostrophe(name : str) -> str:
    # Ensure apostrophe is followed by a lowercase letter
    parts = name.split("'")
    if len(parts) > 1:
        for i in range(1, len(parts)):
            if parts[i] and parts[i][0].isupper():
                parts[i] = parts[i][0].lower() + parts[i][1:]
        name = "'".join(parts)
    return name

# Remove '-' at the end
def dash_end_removal(name : str) -> str:
    if len(name) < 1:
        return ''
    
    if ("'" in name[-1]):
        print(name)
        return name[:-1]
    return name

# Opening and Reading Input File
with open (filepath, 'r', encoding='utf-8') as f:
    current_names = f.readlines()
    names_refreshed = [dash_end_removal(names) for names in current_names]
    linestr = ''.join(names_refreshed)
    linestr = split_title_case(linestr)
    linestr = formatting_string(LIST_FILTERING, '\n')
    linestr = fixing_apostrophe(linestr)
    # linestr = dash_end_removal(linestr)
    linestr = remove_extras(linestr).title()

# Writing on File and UI of the Number of Contents in Input.txt
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(linestr)
    print("\nProgram remove_tabs_n_spaces.py has run succesfully.")
    print(f"The number of contents in input.txt is -{len(current_names)}-\n")
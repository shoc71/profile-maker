# imports
try: 
    from Important.formatting_list_contents import indent_list, space_dash_list
    from Important.brands import brands_list
    from Important.extras_and_emojis import extras_list
    from Important.character_list import char_list
except:
    from formatting_list_contents import indent_list, space_dash_list
    from brands import brands_list
    from extras_and_emojis import extras_list
    from character_list import char_list

# Filepath and File
filepath = 'profile_resources/input.txt'

# List of Characters that need to be Removed
char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(' ,')' ,  '=', "+", "·", '›',
             '"', "?", ":", ";", "”", "“", "[", "]", "|", "}", "{", "\\", "•", "<", ">", "ʿ",
             "\"", "!", "@", "#", "$", "%", "^", "&", "*", "~", "`", "§", "®", "»", "«",
             '©', '™', "’", "‘"] #, "\'", '—'] 

indent_list = ['/', '\t', ',', '.'] #, ".", '-']

extras_list = ['©', '🍓', '🔥', '🏆', '🦸', '🍑', '�', '💚', '🕊', '🌳', '🌙',
              '🐅', '🏔', '🎨', '💙', '🧚', '💸', '⭐', '☀', '❄', '🌊', '\\u200e',
              '🌐', '💀', '😍', '👌', '👍', '🚀', '📈', '🤖', '☆', "‎", 
              "▾", "🏔️", "✅", "👋", "🎤"]

space_list = [' ', '–', "−"]

brands_list = ["Discord", "Twitter", "Instagram", "YouTube", "News", "PayPal", "Patreon", "Ko-fi"]

example = 'https://updater.com/moving-tips/first-apartment-checklist'

# Formating any mentioned characters
def formatting_string(list_of_str, replace) -> str:
    global linestr
    linestr = str(linestr)
    for line in range(len(list_of_str)):
        linestr = linestr.replace(list_of_str[line], replace)
    return linestr

# Removing any extras space
def remove_extras(string) -> str:
    lirt = str(string).split("\n")
    n_list = list(dict.fromkeys(lirt))
    lirt_str = '\n'.join(n_list)
    return lirt_str

# Splitting Title Case Words
def split_title_case(string) -> str:
    newstring = ''
    for letter in string:
        # Check if character is uppercase and a letter
        if letter == letter.upper() and letter.isalpha():
            newstring += '\n' + letter
        else:
            newstring += letter
    return newstring


# Fixing apostrophe
def fixing_apostrophe(name: str) -> str:
    # Ensure apostrophe is followed by a lowercase letter
    parts = name.split("'")
    if len(parts) > 1:
        for i in range(1, len(parts)):
            if parts[i] and parts[i][0].isupper():
                parts[i] = parts[i][0].lower() + parts[i][1:]
        name = "'".join(parts)
    return name


# Opening and Reading Input File
with open (filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    linestr = ''.join(lines)
    linestr = split_title_case(linestr)
    linestr = formatting_string(space_list, "-")
    linestr = formatting_string(indent_list, '\n')
    linestr = formatting_string(char_list, '\n')
    linestr = formatting_string(extras_list, '\n')
    linestr = formatting_string(brands_list, '\n')
    linestr = fixing_apostrophe(linestr)
    linestr = remove_extras(linestr).title()

# Writing on File and UI of the Number of Contents in Input.txt
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(linestr)
    print("\nProgram remove_tabs_n_spaces.py has run succesfully.")
    print(f"The number of contents in test.txt is -{len(lines)}-\n")
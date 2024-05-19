filepath = 'profile_resources/testing/test.txt'
char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(' ,')' ,  '=', "+", "·", '›',
             '"', "?", ":", ";", "”", "“", "[", "]", "|", "}", "{", "\\", "•", "<", ">", '–',
             "\"", "\'", "!", "@", "#", "$", "%", "^", "&", "*", "~", "`", "§", "®", "»", "«"] # '.',
indent_list = ['/',' ', '\t', ',', '.', '-']
emoji_list = ['©', '🍓', '🔥', '🏆', '🦸', '🍑', '�', '💚', '🕊', '🌳', '🌙',
              '🐅', '🏔', '🎨', '💙', '🧚', '💸', '⭐', '☀', '❄', '🌊', '\\u200e',
              '🌐', '💀', '😍', '👌', '👍', '🚀', '📈', '🤖', '☆']
example = 'https://updater.com/moving-tips/first-apartment-checklist'

def format_with_list(list_of_str, replace):
    global linestr
    linestr = str(linestr)
    for line in range(len(list_of_str)):
        linestr = linestr.replace(list_of_str[line], replace)
    return linestr

def remove_extras(string):
    lirt = str(string).split("\n")
    n_list = list(dict.fromkeys(lirt))
    lirt_str = '\n'.join(n_list).title()
    return lirt_str

with open (filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    linestr = ''.join(lines).title()
    linestr = format_with_list(indent_list, '\n')
    linestr = format_with_list(char_list, '\n')
    linestr = format_with_list(emoji_list, '\n')
    linestr = remove_extras(linestr)
f.close()

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(linestr)
f.close()
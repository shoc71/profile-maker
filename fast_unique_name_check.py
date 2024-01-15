filename = 'full_list_of_names.txt'

with open (filename, mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    lin_str = ''.join(list(dict.fromkeys(lines))).title()
    # n_list = list(dict.fromkeys(line))
    # lirt_str = ''.join(n_list).title()

with open (filename, mode='w', encoding='utf-8') as f:
    f.write(lin_str)
f.close()

lirt = []
filename = 'full_list_of_names.txt'

with open (filename, mode='r', encoding='utf-8') as f:
    line = f.readlines()
    n_list = list(dict.fromkeys(line))
# lirt = random.sample(lirt, len(lirt))
lirt_str = ''.join(n_list).title()

with open (filename, mode='w', encoding='utf-8') as f:
    f.write(lirt_str)
f.close()
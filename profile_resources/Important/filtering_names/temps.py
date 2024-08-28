

all_list = []

all_string = '\n'.join(all_list)

with open ("output.txt", 'w') as file:
    file.write(all_string)
filepath_for_input = 'profile_resources/input.txt'

def notepad_function(file, mode, contents = False):
    """
    Opening up a notepad to read the contents inside, while removing the redundancy 
    of opening the file over and over again.

    Arguments:
        file = filename and filepath
        mode = 'r' for read, 'w' for write
        if 'w', put any contents in as a list or string
    
    RETURNS:
        if 'r', A list of strings split on spaces
        if 'w', writes on the notepad, defaults to blank if contents=False
    """
    if (mode == 'r'):
        with open(file=file, mode='r', encoding='utf-8', errors='ignore') as file:
            return file.read().splitlines()
    
    if (mode == 'w'):
        with open(file=file, mode='w', encoding='utf-8', errors='ignore') as file:
            if (contents == False):
                    file.write('')

            else:
                if isinstance(contents, str):
                        file.write(contents)

                elif isinstance(contents, list): 
                    file.write('\n'.join(contents))

def writing_into_file(total_list, file_name, divisible_count):
    sum_100k_list = []

    if (len(total_list) < divisible_count):
        sum_100k_list += total_list[0:len(total_list)]
        notepad_function(file=file_name,mode='w',contents=sum_100k_list)
        notepad_function(file=filepath_for_input,mode='w')
        return []
    
    else:
        sum_100k_list += total_list[0:divisible_count]
        # print(sum_100k_list)
        notepad_function(file=file_name,mode='w',contents=sum_100k_list)
        filtered_list = list(set(total_list).difference(sum_100k_list))

        return filtered_list
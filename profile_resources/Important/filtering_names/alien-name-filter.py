import os
import notepad
import random

names_directory = []
aliens_directory = []
main_names_list = []
alien_names_list = []
DIVISIBLE_COUNT = 100_000
DISPLAY_SUS_LIST = False

''''''

looking_for_alien_x = input("\nWhat alien names are we looking for? : ")
alien_scaner_true = looking_for_alien_x

''''''
name_folder = 'profile_resources/names_list/'
alien_folder = 'profile_resources/alien_names/'

name_files = os.listdir(name_folder)
alien_files = os.listdir(alien_folder)

for name_file in name_files:
    names_directory.append(name_folder + name_file)

for alien_file in alien_files:
    aliens_directory.append(alien_folder + alien_file)

for names_path in names_directory:
    main_names_list += notepad.notepad_function(file=names_path, mode='r')

for alien_path in aliens_directory:
    alien_names_list += notepad.notepad_function(file=alien_path, mode='r')

print(f"\nSearching for aliens with '{alien_scaner_true}' as the search_term...")

def alien_search(string: str):
    return alien_scaner_true.lower() in string.lower()

def human_search(string: str):
    return user_filter_text.lower() in string.lower()

aliens_filtered = list(filter(alien_search, main_names_list))
# combined_alien_list = list(set(alien_names_list)) + aliens_filtered
old_total_name_count = len(main_names_list)
old_alien_count = len(alien_names_list)

alien_count = len(list(aliens_filtered))
main_names_list = [alien_name for alien_name in main_names_list if alien_name not in aliens_filtered]
suspicious_filtered_length = list(filter(lambda x: len(x) != 6, aliens_filtered))

# random.shuffle(main_names_list)
# random.shuffle(alien_names_list)

'''
afjmrw
gnorvx
Dfgmps
bghlsw
ahoprx
pfjpvy
Uloaku
Aegkop
Hkqruz
Lmtuwy
Aegiuv
Mprtwx
Cgnouy
Cdfiju
hinpvz
Bimqux
Bcdgwy
Bdhpqy
cfkpqv
Degknt
Apsuwz
Bdmrux
dgmqxt
'''
print((aliens_filtered))
print(f"\nNumber of aliens found with '{alien_scaner_true}' is {alien_count}\n")
print(f"Words of interest : {suspicious_filtered_length} - length '{len(suspicious_filtered_length)}'\n")

running = True

# Loop list to catch and remove all the human names caught
while running:

    if alien_count == 0:
        running = False
        user_input = "n" # prevent user_input not declared error from raising
        print(f"No aliens with '{alien_scaner_true}' in their name has been found.", end=" " 
              f"This part of the program has been skipped.\n")
        main_names_list += aliens_filtered
    else:
        display_sus_check = input("Before we continue, would you like to continue to see the list of words that have been filtered outbefore the conditions have been set? (Y/N) : ").lower()

        if display_sus_check == "y":
            DISPLAY_SUS_LIST = True
        
        user_input = input("This is the current list. Would you like to remove any accidental human adductions? (Y/N) : ")

    if user_input in ["no", "n", "not", "nah"]:
        running = False
        alien_count = len(list(aliens_filtered))
        new_total_name_count = len(main_names_list)
        # main_names_list += aliens_filtered

    elif user_input in ["yes", "y", "ye", "yea"]:
        old_alien_count_beta = len(list(aliens_filtered))
        user_filter_text = input("Please enter the words/characters that you want removed. : ")
        if user_filter_text == "quit":
            continue
        user_filter = list(filter(human_search, aliens_filtered))
        aliens_filtered = [item for item in aliens_filtered if item not in user_filter]
        suspicious_filtered_length = [item for item in suspicious_filtered_length if item not in user_filter]
        aliens_filtered = [item for item in aliens_filtered if item not in suspicious_filtered_length]
        alien_count = len(list(aliens_filtered))
        print((aliens_filtered))
        print(f"\nHumans with '{user_filter_text}' have been removed from the list.")
        print(f"The old count is '{old_alien_count_beta}' and new count is '{alien_count}' - length {len(suspicious_filtered_length)}" 
              f" BUT list reduction {old_alien_count_beta - alien_count}")
        print(f"Number of aliens found with '{alien_scaner_true}' is {alien_count}\n")
        if DISPLAY_SUS_LIST == True:
            print(f"Words of interest : {suspicious_filtered_length} - length {len(suspicious_filtered_length)}\n")

    else:
        print("Please input YES or NO. Depending on your response.")

combined_alien_list = list(set(alien_names_list)) + aliens_filtered
alien_notepad_count = int(round((alien_count / 100_000), 0) + 2)
print(f"\nNumber of list names for aliens: {alien_notepad_count + 1}")
for i in range(1, alien_notepad_count):
    if i <= 999:
        file_name = f"{alien_folder}names_{i:04d}.txt" 
        combined_alien_list = notepad.writing_into_file(total_list=combined_alien_list, file_name=file_name, divisible_count=DIVISIBLE_COUNT)

main_notepad_count = int(round((len(main_names_list) / 100_000), 0))
print(f"Number of list names for humans: {main_notepad_count}")
for i in range(1, main_notepad_count + 1):
    if i <= 999:
        file_name = f"{name_folder}names_{i:04d}.txt" 
        main_names_list = notepad.writing_into_file(total_list=main_names_list, file_name=file_name, divisible_count=DIVISIBLE_COUNT)

print(f"\nOld Total_Names count: {old_total_name_count}\n"
      f"New Total_Names count: {new_total_name_count}\n"
      f"Old Total_Aliens count: {old_alien_count}\n"
      f"New Total_Aliens count: {alien_count + old_alien_count}\n"
      f"Difference Count for Names: {old_total_name_count - new_total_name_count}.\n"
      f"Difference Count for Aliens: {alien_count}.")
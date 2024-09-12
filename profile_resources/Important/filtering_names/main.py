import os
import notepad
import math

names_directory = []
aliens_directory = []
main_names_list = []
alien_names_list = []
DIVISIBLE_COUNT = 100_000
DISPLAY_SUS_LIST = False

# User Input
looking_for_alien_x = input("\nWhat alien names are we looking for? : ")
alien_scaner_true = looking_for_alien_x.lower()

# Directories
name_folder = 'profile_resources/names_list/'
alien_folder = 'profile_resources/alien_names/'

# Fetch files
name_files = sorted(os.listdir(name_folder))
alien_files = sorted(os.listdir(alien_folder))

# Append file paths to the respective directories
names_directory = [name_folder + name_file for name_file in name_files]
aliens_directory = [alien_folder + alien_file for alien_file in alien_files]

# Read names from files into lists
main_names_list = [name for names_path in names_directory for name in notepad.notepad_function(file=names_path, mode='r')]
alien_names_list = [name for alien_path in aliens_directory for name in notepad.notepad_function(file=alien_path, mode='r')]

print(f"\nSearching for aliens with '{alien_scaner_true}' as the search term...")

# Search functions
def alien_search(string: str):
    return alien_scaner_true in string.lower()

# Filtering alien names
aliens_filtered = list(filter(alien_search, main_names_list))
old_total_name_count = len(main_names_list)
old_alien_count = len(alien_names_list)

# Separate suspicious words based on length
suspicious_filtered_length = [name for name in aliens_filtered if len(name) != 6]

# Automatically remove suspicious words from aliens_filtered
aliens_filtered = [name for name in aliens_filtered if name not in suspicious_filtered_length]

alien_count = len(aliens_filtered)

# Display results
print(f"\nNumber of aliens found with '{alien_scaner_true}': {alien_count}")
print(f"Suspicious words (automatically removed): {suspicious_filtered_length}, count: {len(suspicious_filtered_length)}\n")

running = alien_count > 0

# Loop to handle accidental human abductions
while running:
    print(aliens_filtered)
    display_sus_check = input("\nWould you like to see the filtered list? (Y/N): ").lower()

    if display_sus_check == "y":
        DISPLAY_SUS_LIST = True

    user_input = input("Would you like to remove any human names? (Y/N): ").lower()

    if user_input in ["n", "no"]:
        running = False
    elif user_input in ["y", "yes"]:
        user_filter_text = input("Enter the words/characters to remove: ").lower()
        aliens_filtered = [name for name in aliens_filtered if user_filter_text not in name.lower()]
        alien_count = len(aliens_filtered)

        print(f"\nHumans with '{user_filter_text}' have been removed. New alien count: {alien_count}")
        if DISPLAY_SUS_LIST:
            print(f"Words of interest: {suspicious_filtered_length}, count: {len(suspicious_filtered_length)}")
    else:
        print("Please input 'yes' or 'no'.")

# --- File Writing for Alien Names ---

# Combine alien list with filtered aliens
combined_alien_list = list(set(alien_names_list) | set(aliens_filtered))

# Calculate number of files to write
alien_notepad_count = math.ceil(len(combined_alien_list) / DIVISIBLE_COUNT)

print(f"\nNumber of alien name files to create: {alien_notepad_count}")

# Write to each file
for i in range(1, alien_notepad_count + 1):
    file_name = f"{alien_folder}names_{i:04d}.txt"
    # Get the next chunk of names to write to the file
    start_idx = (i - 1) * DIVISIBLE_COUNT
    end_idx = start_idx + DIVISIBLE_COUNT
    chunk = combined_alien_list[start_idx:end_idx]

    # Write chunk to the file
    notepad.notepad_function(file=file_name, mode='w', contents=chunk)

# --- File Writing for Human Names ---

# Calculate number of files to write
main_notepad_count = math.ceil(len(main_names_list) / DIVISIBLE_COUNT)

print(f"\nNumber of human name files to create: {main_notepad_count}")

# Write to each file
for i in range(1, main_notepad_count + 1):
    file_name = f"{name_folder}names_{i:04d}.txt"
    # Get the next chunk of names to write to the file
    start_idx = (i - 1) * DIVISIBLE_COUNT
    end_idx = start_idx + DIVISIBLE_COUNT
    chunk = main_names_list[start_idx:end_idx]

    # Write chunk to the file
    notepad.notepad_function(file=file_name, mode='w', contents=chunk)

# Final output of statistics
new_total_name_count = len(main_names_list)

print(f"\nOld Total_Names count: {old_total_name_count}\n"
      f"New Total_Names count: {new_total_name_count}\n"
      f"Old Total_Aliens count: {old_alien_count}\n"
      f"New Total_Aliens count: {alien_count + old_alien_count}\n"
      f"Difference Count for Names: {old_total_name_count - new_total_name_count}\n"
      f"Difference Count for Aliens: {alien_count - len(suspicious_filtered_length)}")

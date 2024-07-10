'''
Instances of collected_words.txt being too big to even open.
'''
import time
# from Important import x_word_count

start_time = time.time()
print(f"Program has started on - {start_time}")
current_location = "profile_resources/Important/collected_words.txt"
destination = "profile_resources/input.txt"

with open(file=current_location, mode='r', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()

with open(file=destination, mode='w', encoding='utf-8', errors='ignore') as file:
    importable_string = '\n'.join(lines)
    file.write(importable_string)

end_time = time.time()
print(f"Time : {end_time - start_time}")
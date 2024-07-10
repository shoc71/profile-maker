import random

current_location = "profile_resources/Important/collected_words.txt"

with open(file=current_location, mode='r', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()

def new_name(number_of_names):
    number_of_names = int(number_of_names)
    for n in range(number_of_names):
        fname, lname = random.choice(lines), random.choice(lines)
        print(f"{n+1}. {fname} {lname}")

new_name(150)
import random
def new_name(txt_filename, number_of_names):
    txt_filename, number_of_names = str(txt_filename), int(number_of_names)
    with open(txt_filename, mode="r", encoding="utf-8", errors="ignore") as f:
        lines = [line.rstrip() for line in f.readlines()]
        for n in range(number_of_names):
            fname, lname = random.choice(lines), random.choice(lines)
            print(f"{n+1}. {fname} {lname}")
            # return f"{n+1}. {fname} {lname}"

new_name("profile_resources/names_list/names.txt", 5)
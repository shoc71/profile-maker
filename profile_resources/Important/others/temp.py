from Important.notepad import notepad_function
'''help function'''
# help(notepad_function)

name = "joe"
'''print function'''
# print("Hi, my name is",name,"nice to meet you! Im",name, sep="|", end="-pp-")
# print("Lol")

# help(range)

rng = range(-8, 14, 3)
# print(rng) # iterator
# print(list(rng)) # puts everything into a list

# iterable object is something that you can loop through
bag = ["apple", "cheese", "bone", "pencils", "hamburger", "tea", "py"]

def add_s(string):
    # lambda x:x +"s" - works too, kinda know why
    return string + "s"
'''map function'''
length = map(add_s, bag) # map () apply a function to every single function in an iterable object
# print(list(length))

def return_o(string):
    # return len(string) > 4
    if "o" in string:
        return string
'''filter function'''
filtered = filter(return_o, bag) # conditional filter needed to be added here
filtered = filter(lambda x: len(x) > 4, bag)
# print(list(filtered))

numbers = [2, 32, 41, -32, -56, 8, 83, 0, -12, -43, -2]

people = [
    {"name": "Alice", "age": 30},
    {"name": "Lia", "age": 35},
    {"name": "Stacy", "age": 25},
    {"name": "John", "age": 12}
]
# print(sum(numbers, start=-10))
'''sorted function'''
sorted_people = sorted(people, key= lambda person: person["age"], reverse=True)

# print(sorted_people)

tasks = ["Write Report", 'Attend Meeting', 'Review Code', 'Submit Timesheet']
'''enumerate function'''
# for index_value, value_inside in enumerate(tasks): # enum() returns a tuple (index_value, value_from_list)
#     print(f"{index_value + 1}. {value_inside}")
    # examples (index + 1, write report (value at that index position))

# print(list(enumerate(tasks)))

names = ["Alice", "Bob", "Jesar", "Prot", "tim"]
ages = [30, 32, 31, 21]
gender = ["male", "female", "male"]

# for index in range(min(len(names), len(ages))): # preventing a list index out of range error
    # name = names[index]
    # age = ages[index]
    # print(f"{name} is {age} years old")
'''zip function'''
combined_info = list(zip(names, ages, gender))

for name_index, age_index, gender_index in combined_info:
    print(f"{name_index} is {age_index} years old and is {gender_index}")

print(combined_info)

# use with open() auto closes when you are doen
'''open function'''
with open("test.txt",'a') as file:
    file.write("\nnew addition")
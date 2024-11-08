# Imports
from scoring import score_name

names_of_interest = []
names_to_remove = []

# Function to score a list of names
def score_names(names_list):
    results = {}
    for names in names_list:
        score, deductions = score_name(names)
        results[names] = {"score": score, "deductions": deductions}
    return results

# Define a custom function to extract the score for sorting
def get_score(item):
    name, details = item # technically a tuple (name, detail)
    return details['score']

# Function to print the names sorted by their score
def print_sorted_names_by_score(scored_names):
    sorted_names = sorted(scored_names.items(), key=get_score, reverse=True)

    for name, details in sorted_names:
        print(f"Name: {name}, Score: {details['score']}, Deductions: {details['deductions']}")

        if details['score'] != 0:
            names_of_interest.append(name)
        else:
            names_to_remove.append(name)

names = []

test_names = '''
Anoprw
Dgimxz
Bfhimq
Ehpqvz
Lwa
afjmrw
gnorvx
Dfgmps
bghlsw
Abejns
ahoprx
pfjpvy
Befmoq
Cimoqw
Aegkop
Hituyz
Abdlnt
Hkqruz
Lmtuwy
lmnop
Adhlsy
Aefruv
Abklor
Celqvy
Bcilwz
Bgknrw
Efijpu
Bgortu
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

test = test_names.split('\n')
for t in test:
    names.append(t.title())

# Output the results
print_sorted_names_by_score(score_names(names))
print(f"Good to use-ish : {names_of_interest}")
print(f"Names to remove : {names_to_remove}")

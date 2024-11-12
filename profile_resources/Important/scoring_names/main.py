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
    order = 0

    for name, details in sorted_names:
        order += 1
        print(
            f"{order}. "
            f"Name: {name}, Score: {details['score']}, Deductions: {details['deductions']}"
            f"\n"
        )

        if details['score'] != 100:
            names_to_remove.append(name)
        else:
            names_of_interest.append(name)

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
liege
regfer
Abejns
ahoprx
piccolo
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
print(
    f"\n"
    f"Good to use-ish : {names_of_interest}"
)
print(
    f"\n"
    f"Names to remove : {names_to_remove}"
)

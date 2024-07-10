# import
import itertools
import string
import time

start_time = time.time()

'''Technically works, just not what I wanted'''
# def all_combinations(word):
#     result = []
#     length = len(word)
#     for i in range(1, length + 1):
#         for combo in combinations(word, i):
#             result.append('\n'.join(combo))
#     return result

# word = string.ascii_lowercase
# combinations_list = all_combinations(word)

def formatting_numbercount(number):

    if isinstance(number, (float, int)):
        formated_number = f"{number:,}" # f"{amount:,.2f}".replace(',', '_')
        return formated_number

def generate_combinations(word, length):
    # Generate all combinations of the word with the given length
    combos = itertools.product(word, repeat=length)
    
    # Convert combinations from tuples back to strings
    combos = [''.join(comb) for comb in combos]
    
    return combos

# Example usage
word = string.ascii_lowercase
length = 6
combos = generate_combinations(word, length)

filepath = "profile_resources/Important/collected_words.txt"
with open(file=filepath, mode='w', encoding='utf-8', errors='ignore') as f:
    multi_word_combo = '\n'.join(combos)
    f.write(multi_word_combo)

end_time = time.time()

print(f"Saved to {filepath}")
print(f"Length of list: {formatting_numbercount(len(combos))} "
      f"- Expected Length: {formatting_numbercount(len(word) ** length)}")
print(f"Time : {end_time - start_time}")
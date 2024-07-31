alien_scaner_true = 'omar'

def alien_search(string):
    print(f"Checking '{alien_scaner_true}' in '{string}'")  # Debugging line
    return alien_scaner_true.lower() in string.lower()  # Case-insensitive search

# Test cases
names = ['Bomar', 'omar', 'Egglp', 'testEGlp']

# Filter using the alien_search function
filtered_names = filter(alien_search, names)
print(list(filtered_names))  # Output will show matching names

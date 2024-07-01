# Removing Extreme Start or End apostrophe and fixing apostrophe issues
def remove_extreme_apostrophe(name: str) -> str:
    
    # Remove leading/trailing whitespace and newlines
    name = name.strip()

    # Remove apostrophe at the start
    if name.startswith("'"):
        name = name[1:]

    # Remove apostrophe at the end
    if name.endswith("'"):
        name = name[:-1]

    # Ensure apostrophe is followed by a lowercase letter
    parts = name.split("'")
    if len(parts) > 1:
        for i in range(1, len(parts)):
            if parts[i] and parts[i][0].isupper():
                parts[i] = parts[i][0].lower() + parts[i][1:]
        name = "'".join(parts)
    return name

# Test the function with sample names
with open('profile_resources/names.txt', 'r', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()

sample_names = lines[0:1000]

for name in sample_names:
    fixed_name = remove_extreme_apostrophe(name)
    if fixed_name != name:
        print(f"Original: {name.strip()} => Fixed: {fixed_name.strip()}")
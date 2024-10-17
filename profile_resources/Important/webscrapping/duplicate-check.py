filepath = 'profile_resources/Important/webscrapping/'
target_file = filepath + 'collected_words.txt'
output_file = filepath + 'output.txt'

new_list = []
dup_list = []
dup_count = {}

with open (target_file, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for line in lines:
    if line not in new_list:
        new_list.append(line)
    else:
        dup_list.append(line)

for line in range(len(dup_list)):
    if dup_list[line] not in dup_count:
        dup_count[dup_list[line]] = 1
    else:
        dup_count[dup_list[line]] += 1

def mykeys(thekey):
    return thekey[1]

dup_count_sorted = sorted(dup_count.items(), key=mykeys, reverse=True)

print(f"unique word count: {len(new_list)}, duplicate word count: {len(dup_list)}" + "\n"
      f"Total words to check {len(lines)}, New + Dup: {len(new_list) + len(dup_list)}" + "\n"
      f"\n{dup_count_sorted}")

new_words = ''.join(new_list)

with open (output_file, 'w', encoding='utf-8', errors='ignore') as f:
    f.write(new_words)

print("end of program")
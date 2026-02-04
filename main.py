from typing import List # 3.9 type hinting doesnt work on cccgrader so here we are
### ccc '25 s2

# get input
raw_pattern:str = input()
idx = int(input())


import re

# declare variables
p_lengths:List[int] = []
p_letters:List[str] = []
total_len = 0

# parse string input using regex
pattern = "(.\\d+)"
found:List[str] = re.findall(pattern, raw_pattern)

# sort regex group into letters and lengths
for group in found:
    p_letters.append(group[0])
    p_lengths.append(int(group[1:]))
    total_len += int(group[1:])

# use modulus to reduce excess cycles
idx %= total_len

# reduce the index by p_lengths[i] for each iteraton in p_lengths
#   if resulting index is smaller than 0, 
#       print the letter at p_letters[i]
#       break loop

for i,length in enumerate(p_lengths):
    idx -= length
    if idx < 0:
        print(p_letters[i])
        break
    

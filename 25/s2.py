### ccc '25 s2
import re

# get input
raw_pattern:str = input()
index = int(input())

# declare variables
p_lengths:list[int] = []
p_letters:list[str] = []
total_len = 0

# parse string input using regex
pattern = "(.\\d+)"
found:list[str] = re.findall(pattern, raw_pattern)

# sort regex group into letters and lengths
for group in found:
    p_letters.append(group[0])
    p_lengths.append(int(group[1:]))
    total_len += int(group[1:])

# use modulus to reduce excess cycles
index %= total_len

# reduce the index by p_lengths[i] for each iteraton in p_lengths
#   if resulting index is smaller than 0, 
#       print the letter at p_letters[i]
#       break loop

for i,length in enumerate(p_lengths):
    index -= length
    if index < 0:
        print(p_letters[i])
        break
    


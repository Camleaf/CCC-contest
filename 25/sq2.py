### ccc '25 s2
import re


raw_pattern:str = input()
index = int(input())

p_lengths:list[int] = []
p_letters:list[str] = []
total_len = 0


num_build = ''
pattern = "(.\\d+)"
found:list[str] = re.findall(pattern, raw_pattern)
for group in found:
    p_letters.append(group[0])
    p_lengths.append(int(group[1:]))
    total_len += int(group[1:])

index %= total_len

for i,length in enumerate(p_lengths):
    index -= length
    if index < 0:
        print(p_letters[i])
        break
    


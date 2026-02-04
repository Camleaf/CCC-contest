
### ccc '25 j3
import re

patternStr = "([A-Z])"
patternInt = "(-?\\d+)"

for i in range(int(input())):
    

    word = input()
    foundStr:list[str] = re.findall(patternStr, word)
    foundInt:list[str] = re.findall(patternInt, word)

    total = 0
    stringbuild = ''

    for token in foundStr:
        stringbuild += token

    for token in foundInt:
        total += int(token)

    print(stringbuild + str(total))

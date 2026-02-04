### ccc '25 j3




for i in range(int(input())):
    new_total:int = 0
    new_string:str = ''

    for letter in input():
        if letter not in "abcdefghijklmnopqrstuvwxyz".upper():
            continue
        elif letter in "123456789":
            new_total += int(letter)

    print(new_string+str(new_total))

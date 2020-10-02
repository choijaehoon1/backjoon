test = input()

result = 0
for i in test:
    num = 0
    if i == 'A' or i == 'B' or i == 'C':
        num += 2
    elif i == 'D' or i == 'E' or i == 'F':   
        num += 3
    elif i == 'G' or i == 'H' or i == 'I':   
        num += 4
    elif i == 'J' or i == 'K' or i == 'L':   
        num += 5
    elif i == 'M' or i == 'N' or i == 'O':   
        num += 6
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':   
        num += 7
    elif i == 'T' or i == 'U' or i == 'V':   
        num += 8
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':   
        num += 9                    
    result += num
    result += 1     
print(result)    

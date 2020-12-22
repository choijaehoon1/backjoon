import sys
n = int(sys.stdin.readline().rstrip())

array = []
for i in range(n):
    for j in range(n):
        flag = True
        x = i
        y = j
        while y != 0:
            if x % 3 == 1  and y % 3 == 1:
                flag = False
                array.append(' ')
                break
            x //= 3
            y //= 3
        if flag:
            array.append('*')
    array.append('\n')
result = ''.join(array)    
print(result)


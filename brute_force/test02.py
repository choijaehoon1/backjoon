n = int(input())

def func(n):
    result = n
    while n > 0:
        result += n%10
        n //= 10
    return result

x = 0
while func(x) != n:
    if x == n:
        x = 0
        break
    else:
        x +=1
print(x)        


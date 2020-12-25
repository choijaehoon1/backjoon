import math
import sys
n,k = map(int, sys.stdin.readline().rstrip().split())
down = math.factorial(k)
num = 1
flag = True
while k > 0:
    if k == 0:
        flag = False
        break
    num *= n
    n -= 1
    k -= 1

if flag:
    print((num // down) % 10007)
else:
    print(1)

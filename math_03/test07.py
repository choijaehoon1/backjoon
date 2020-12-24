import math
import sys
n,k = map(int,sys.stdin.readline().rstrip().split())
tmp = 1
num = n
while tmp < k:
    num *= n-tmp
    tmp += 1

if k == 0:
    print(1)
else:
    print(num // math.factorial(k))    

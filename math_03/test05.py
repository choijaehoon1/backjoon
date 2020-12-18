import sys
import math
n = int(sys.stdin.readline().rstrip())

array = []
gcd = 0
for i in range(n):
    num = int(input())
    array.append(num)
    gcd = math.gcd(abs(array[i]-array[i-1]),gcd)        

result = [gcd]
for i in range(2,int(math.sqrt(gcd))+1):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd//i)
result = list(set(result))
result.sort()
for i in result:
    print(i, end=' ')


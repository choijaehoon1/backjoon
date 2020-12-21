import math
import sys
n = int(sys.stdin.readline().rstrip())

array = list(map(int,sys.stdin.readline().rstrip().split()))
start = array[0]
for i in range(1,len(array)):
    gcd = math.gcd(start, array[i])
    up = start // gcd
    down = array[i] // gcd
    print(str(up)+"/"+str(down))


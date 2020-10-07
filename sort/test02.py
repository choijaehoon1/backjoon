import sys

n = int(sys.stdin.readline().rstrip())
array = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    array.append(num)
array.sort()
for i in array:
    print(i)    

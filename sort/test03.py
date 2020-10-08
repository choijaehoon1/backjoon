import sys

n = int(sys.stdin.readline().rstrip())
array = [0] * 10001

for i in range(n):
    num =int(sys.stdin.readline().rstrip())
    array[num] += 1

for i in range(len(array)):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)

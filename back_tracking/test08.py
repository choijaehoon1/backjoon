from itertools import combinations
import sys
n = int(sys.stdin.readline().rstrip())
person = [i for i in range(n)]
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

tmp = list(combinations(person,n//2))

result = int(1e9)
for i in range(len(tmp)//2):
    start = list(tmp[i])
    link = [x for x in person if x not in start]
    a = 0
    b = 0
    for x in range(len(start)):
        for y in range(x+1,len(start)):
            a += array[start[x]][start[y]] + array[start[y]][start[x]]
            b += array[link[x]][link[y]] + array[link[y]][link[x]]
    result = min(result,abs(a-b))
print(result)


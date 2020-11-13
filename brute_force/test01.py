from itertools import combinations
n,m = map(int,input().split())

array = list(map(int, input().split()))
tmp = list(combinations(array,3))
# print(tmp)
result = 0
for i in tmp:
    if sum(i) <=m:
        result = max(result, sum(i))
print(result)

from itertools import combinations
n, m= map(int, input().split())

array = [i for i in range(1,n+1)]

result_list = list(combinations(array,m))

for i in result_list:
    for j in i:
        print(j, end=' ')
    print()

from itertools import product
n, m= map(int, input().split())

array = [i for i in range(1,n+1)]

result_list = list(product(array,repeat=m))

for i in result_list:
    for j in i:
        print(j, end=' ')
    print()

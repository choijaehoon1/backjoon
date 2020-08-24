N, M = map(int,input().split())
A_list = []
for i in range(N):
    A_list.append(list(map(int, input().split())))

B_list = []
M, K = map(int,input().split())
for i in range(M):
    B_list.append(list(map(int, input().split())))
arr = [[0 for i in range(K)] for j in range(N)]
# print(A_list)
# print(B_list)
# print(arr)

for n in range(N):
    for k in range(K):
        for m in range(M):
            arr[n][k] += A_list[n][m] * B_list[m][k]
# print(arr)        
for i in arr:
    for j in i:
        print(j, end=' ')
    print()    

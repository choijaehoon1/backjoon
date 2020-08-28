def solve(x,y,A):
    for i in range(3):
        for j in range(3):
            if A[x+i][y+j] == 0:
                A[x+i][y+j] = 1
            else:
                A[x+i][y+j] = 0
    return A                

n, m = map(int, input().split())
A = []
B = []
for i in range(n):
    A.append(list(map(int,input())))
for i in range(n):
    B.append(list(map(int,input())))
# print(A)
# print(B)
cnt = 0
# n-3, m-3까지의 범위만 확인하면 됨
# 이후 solve함수를 통해 행열 3칸씩 이동하며 검사하므로
for i in range(n-3+1):
    for j in range(m-3+1):
        if A[i][j] != B[i][j]:
            A = solve(i,j,A)
            cnt += 1

answer = True
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            answer = False
if answer:
    print(cnt)
else:
    print(-1)    

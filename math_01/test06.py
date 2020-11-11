import sys
tc = int(sys.stdin.readline().rstrip())

array = [[0]*15 for _ in range(15)]

for i in range(14):
    array[0][i] = i+1
    array[i+1][0] = 1
# print(array)    

for i in range(1,15):
    for j in range(1,15):
        array[i][j] = array[i-1][j] + array[i][j-1]

for _ in range(tc):
    n=int(sys.stdin.readline().rstrip())
    k=int(sys.stdin.readline().rstrip())
    print(array[n][k-1])


board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

zeros = [(i,j) for i in range(9) for j in range(9) if board[i][j] ==0]
# print(zeros)

def is_promising(i,j):
    promising = [1,2,3,4,5,6,7,8,9]

    # 행열검사
    for k in range(9):
        if board[i][k] in promising:
            promising.remove(board[i][k])
        if board[k][j] in promising:
            promising.remove(board[k][j])

    i //= 3
    j //= 3

    for p in range(i*3,(i+1)*3):
        for q in range(j*3,(j+1)*3):
            if board[p][q] in promising:
                promising.remove(board[p][q])
    return promising                

flag = False
def dfs(x):
    global flag

    if flag == True:
        return

    if x == len(zeros):
        for row in board:
            print(*row)
        flag = True
        return
    else:
        i,j = zeros[x]
        promising = is_promising(i,j)
        for num in promising:
            board[i][j] = num
            dfs(x+1)
            board[i][j] = 0 # 초기화
dfs(0)



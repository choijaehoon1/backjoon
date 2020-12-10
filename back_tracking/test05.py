import sys
# 윗줄에 겹치는 퀸이 있는가?
def adjacent(x):
    for i in range(x): # 처음 부터 x행까지 확인
        if row[x] == row[i] or (abs(row[x]-row[i]) == x-i): # 바로위에 행이거나 대각선에 위치
            return False
    return True        


def dfs(x):
    global result

    if x >= n: # 끝까지 가능한 경우에만 1증가
        result += 1
    else:
        for i in range(n):# 각 행에 대해 반복
            row[x] = i
            if adjacent(x) == True:
                dfs(x+1)    

n  = int(sys.stdin.readline().rstrip())
row = [0] * n
result = 0
dfs(0)
print(result)


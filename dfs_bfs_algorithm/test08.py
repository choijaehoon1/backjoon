def solution(n, computers):
    answer = 0
    visit = [0 for i in range(n)]
    for i in range(n):
        if visit[i] == 0:
            dfs(n, computers, visit, i)
            answer += 1
    return answer

def dfs(n, computers, visit, i):    
    if visit[i] == 0:
        visit[i] = 1
    for j in range(n):
        if computers[i][j] == 1 and visit[j] == 0:
            dfs(n,computers, visit, j)

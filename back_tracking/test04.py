n, m= map(int, input().split())

result = []

def dfs(depth, idx):
    if depth == m:
        print(' '.join(map(str,result)))
        return

    for i in range(idx,n):
        result.append(i+1) # 0부터 시작이므로 맞춰주기
        dfs(depth+1, i)
        result.pop()
dfs(0,0)        


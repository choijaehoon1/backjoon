N, M, V = map(int,input().split())

matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    link= list(map(int,input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1
# print(matrix)    

def dfs(current_node, row, foot_print):
    foot_print += [current_node]
    
    for search_node in range(len(row[current_node])):# 해당 행에 대해서 반복
        # 해당 행의 열을 증가 시켜가며 연결되어있고 방문안한 것 찾기
        if row[current_node][search_node] == 1 and search_node not in foot_print:
            dfs(search_node, row, foot_print)
    return foot_print    

def bfs(start):
    queue = [start]
    foot_print = [start]
    while queue:
        current_node = queue.pop(0)

        for search_node in range(len(matrix[current_node])):   # 해당 행에 대해서 반복
            # 해당 행의 열을 증가 시켜가며 연결되어있고 방문안한 것 찾기
            if matrix[current_node][search_node] == 1 and search_node not in foot_print:
                foot_print += [search_node]
                queue += [search_node]
    return foot_print    
        

print(*dfs(V,matrix,[])) # list를 풀어주는 역할(*)
print(*bfs(V))

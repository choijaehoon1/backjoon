N = int(input())
M = int(input())

matrix = [[0]*(N+1) for _ in range(N+1)]
# print(matrix)

for i in range(M):
    link = list(map(int,input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1
# print(matrix)

def dfs(current_node, row, foot_print):
    foot_print += [current_node]

    for search_node in range(len(row[current_node])):
        if matrix[current_node][search_node] == 1 and search_node not in foot_print:
            dfs(search_node, row, foot_print)

    return foot_print
arr = dfs(1,matrix,[])
print(len(arr) -1) # 1을 제외한 개수구하기 이므로


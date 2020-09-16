
# 인접 행렬 방식 예제
INF = 999999999 # 무한의 비용
graph =[
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
print(graph)

# 인접 리스트 방식 예제

graph = [[] for _ in range(3)]
# 노드0에 연결된정보
graph[0].append((1,7)) # 노드와 거리정보
graph[0].append((2,5)) # 노드와 거리정보

# 노드1에 연결된정보
graph[1].append((0,7)) # 노드와 거리정보

# 노드2에 연결된정보
graph[2].append((0,5)) # 노드와 거리정보
print(graph)


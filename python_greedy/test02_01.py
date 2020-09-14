n,m,k = map(int, input().split())

num_type = list(map(int, input().split()))
num_type.sort(reverse=True)

answer = 0
while True:
    for i in range(k):
        if m == 0:
            break
        answer += num_type[0]
        m -= 1
    # for문 다돌고 m 감소 시켰는데 0이 됬으면 빠져나와야 됨
    if m == 0:
        break
    answer += num_type[1]
    m -= 1
print(answer)    

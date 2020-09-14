n,m,k = map(int, input().split())
num_type = list(map(int, input().split()))
num_type.sort(reverse=True)

max_num = num_type[0]
second = num_type[1]

# 수열로 생각(가장큰 수 3번, 가장 작은수 1번) 즉, 수열의 길이는 k+1
# [6,6,6,5] [6,6,6,5] ...

# 가장 큰 수 횟수 구하기
# k+1 길이의 수열이 반복되는 수를 구하고 가장 큰수는 k번 반복되니 곱해줌
count = (m // (k+1)) * k # 반복되는 수열에서 가장 큰 수 횟수
# m이 수열의 길이보다 작은 경우도 고려해줘서 더해 줌 ex)[6,6,6]
count += m % (k+1) 

answer = count * max_num
answer += (m-count) * second
print(answer)

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.reverse()
# print(arr)

num = 0
answer = []
while K > 0:
    for i in arr:
        if i > K:
            continue
        num += K//i     # num에는 몫을 더하면서 저장해 줌
        K %= i          # K는 i로 나누어줌
print(num)            

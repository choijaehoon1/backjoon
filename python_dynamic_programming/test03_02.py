n = int(input())
d = [0] * 100
arr = list(map(int,input().split()))

# i-1번째 식량창고를 털면 현재식량창고 못 털음
# i-2번째 식량창고를 털면 현재식량창고 털음
# 두가지 경우 중 더 많은 식량을 털 수 있는경우가 답
d[0] = arr[0]
d[1] = max(arr[0],arr[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + arr[i])
print(d[n-1])

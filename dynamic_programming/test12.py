# 최대증가 수열 + 최소감소수열 -1
n = int(input())
arr = list(map(int, input().split()))
# print(arr)
dpa = [0 for i in range(n)]
dpb = [0 for i in range(n)]
dpc = [0 for i in range(n)]
# 정방향 포문
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dpa[i] < dpa[j]:
            dpa[i] = dpa[j]
    dpa[i] += 1        
# 역방향 포문
for i in range(n-1,-1,-1): # 두번째 인자는 포함안되므로 0까지 가려면 -1써야함
    for j in range(n-1,i,-1):
        if arr[i] > arr[j] and dpb[i] < dpb[j]:
            dpb[i] = dpb[j]
    dpb[i] += 1
# 둘이 합치고 가장 큰 수 찾는다.
for i in range(n):
    dpc[i] = dpa[i] + dpb[i] -1
print(max(dpc))    


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
num = 0
for i in range(N):
    for j in range(i+1):
        num += arr[j]
print(num)         

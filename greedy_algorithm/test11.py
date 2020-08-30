n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
num = 1 # 그때의 num값 +1이 최소값임
for i in range(n):
    if num < arr[i]: # 즉 누적된 값보다 특정 i번째 값이 더 크면 중지
        break
    num += arr[i] # num에는 계속 이전값 누적    
print(num)        

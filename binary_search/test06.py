from bisect import bisect_left, bisect_right
n = int(input())
k = int(input())

# 1 2 3
# 2 4 6
# 3 6 9  
start = 0
end = k # k번째 수는 k를 못넘음 
result = 0
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in range(1,n+1):
        cnt += min(mid//i,n) # 각 행은 최대 n보다는 작아야함

    if cnt < k: # 값을 키워서 k와 맞춰줘야함
        start = mid +1
    else: # 최소 값 찾는것이므로 같을 때는 줄여준다
        end = mid - 1
        result = mid
print(result)

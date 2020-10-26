import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int,sys.stdin.readline().rstrip().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    mid = (start+end)//2
    tmp = 0
    for i in array:
        if i > mid:
            tmp += i - mid

    if tmp >= m: # 더 많아 있는 곳에서 갱신
        result = mid
        start = mid +1
    else:
        end = mid -1
        
print(result)        

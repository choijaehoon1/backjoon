import sys
k,n = map(int,sys.stdin.readline().rstrip().split())
array = []
for i in range(k):
    num = int(sys.stdin.readline().rstrip())
    array.append(num)

start = 1 # 자연수
end = max(array)
result = 0
while start <= end:
    mid = (start+end)//2

    count = 0
    for i in array:
        count += i // mid
    
    if count < n:
        end = mid -1
    else: # 충분한 경우
        result = mid
        start = mid +1
print(result)



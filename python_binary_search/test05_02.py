import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진탐색을 위한 시작점과 끜점 설정
start = 0
end = max(array)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in array:
        if i > mid:
            total += (i-mid)
    # 떡의 양이 부족한 경우 (즉, 왼쪽에 답이있다)
    if total < m:
        end = mid -1
    else:
        result = mid # 최대한 덜 짤렸을 때이므로 여기서 result에 값 갱신
        start = mid + 1    
print(result)


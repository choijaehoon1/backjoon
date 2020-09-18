# 계수정렬을 이용한 풀이
n = int(input())
total = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))
total = sorted(total)
want = sorted(want)

array = [0] * 1000001

for i in total:
    array[i] = 1

for i in want:
    if array[i] == 1:
        print('yes',end=' ')
    else:
        print('no',end=' ')    

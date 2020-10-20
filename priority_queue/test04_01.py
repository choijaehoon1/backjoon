from bisect import bisect_left

n = int(input())

array = []
cnt = 0
for i in range(n):
    num = int(input())
    cnt += 1
    index = bisect_left(array,num)
    array.insert(index,num)

    if cnt%2 != 0:
        print(array[cnt//2])
    else:
        print(min(array[cnt//2-1],array[cnt//2]))

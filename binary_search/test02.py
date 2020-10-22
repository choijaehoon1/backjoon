from bisect import bisect_left, bisect_right
n = int(input())
array = list(map(int,input().split()))
array.sort()

def count_by_range(array,x):
    left_index = bisect_left(array,x)
    right_index = bisect_right(array,x)
    return right_index - left_index

m = int(input())
check_list = list(map(int,input().split()))

for target in check_list:
    result = count_by_range(array,target)
    print(result,end=' ')

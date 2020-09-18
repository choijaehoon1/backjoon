import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array = sorted(array)


def binary_search(array,m,start,end):
    while start <= end:
        tmp_mid = (start + end) // 2
        tmp_list = [x-tmp_mid for x in array if x > tmp_mid]
        if sum(tmp_list) == m:
            return tmp_mid
        elif sum(tmp_list) > m:
            start = tmp_mid +1
        else:
            end = tmp_mid -1            
    return 0



print(binary_search(array,m,array[0],array[-1]))





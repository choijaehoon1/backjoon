n = int(input())
total = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))
total = sorted(total)
want = sorted(want)

def binary_search(total,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if total[mid] == target:
            return True
        elif total[mid] > target:
            end = mid -1
        else:
            start = mid +1        
    return False

for i in range(m):
    result = binary_search(total,want[i],0,len(total)-1)
    if result == True:
        print('yes',end=' ')
    else:
        print('no',end=' ')    


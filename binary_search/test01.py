n = int(input())

array = list(map(int,input().split()))
array.sort()

m = int(input())
tmp_array = list(map(int,input().split()))

def binary_search(array,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return False                        

for target in tmp_array:
    flag = binary_search(array,target,0,n-1)
    if flag == True:
        print(1)
    else:
        print(0)    

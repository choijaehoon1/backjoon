while True:
    array = list(map(int, input().split()))
    array.sort()
    if array[0] == 0 and array[1] == 0 and array[2] ==0:
        break
    if pow(array[0],2) + pow(array[1],2) == pow(array[2],2):
        print("right")
    else:
        print("wrong")    

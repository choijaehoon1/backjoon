# 1 1                                                1
# 2 00 112                                           2   
# 3 001 100 010                                      3
# 4 0000 0011 1001 0011 1111                         5
# 5 00001 00100 10000 11100 00111 10011 11001 11111  8

n = int(input())
arr = []
for i in range(n):
    if i == 0 or i == 1:
        arr.append(i+1)
    else:
        tmp = arr[i-1] + arr[i-2]
        tmp %= 15746
        arr.append(tmp)
# print(arr) 결국 피보나치임
print(arr[-1])

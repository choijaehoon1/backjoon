n = int(input())
n = 1000 - n

cnt = 0
arr = [500,100,50,10,5,1]

for i in arr:
    cnt += n // i
    n = n % i
print(cnt)


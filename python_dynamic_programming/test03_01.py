n = int(input())

d = [0] * 101
arr = [0] + list(map(int,input().split()))

d[1] = arr[1]
d[2] = arr[2]
for i in range(3,n+1):
    d[i] = max(d[i-1], d[i-2] + arr[i])
# print(d)
print(d[n])

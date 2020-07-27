N = int(input())

arr = []
for i in range(N):
    num = int(input())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)
sum = 0
for i in arr:
    if len(arr) != 0:
        sum += i
print(sum)

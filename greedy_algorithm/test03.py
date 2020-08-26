n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

result = []
for i in range(n):
    result.append(arr[i] * (i+1))
print(max(result))

N = int(input())
arr = []

for i in range(N):
    str = input()
    arr = list(str)
    sum = 0
    cnt = 1
    for i in arr:
        if i == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)

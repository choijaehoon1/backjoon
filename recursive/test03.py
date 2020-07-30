def hanoi(from1, by, to, n):
    if n == 1:
        print(from1, to)
    else:
        hanoi(from1, to, by, n-1)
        print(from1, to)
        hanoi(by, from1, to, n-1)
N = int(input())
sum = pow(2,N) -1
print(sum)
hanoi(1, 2, 3, N)

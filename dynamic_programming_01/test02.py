# 0이 나오는 횟수와 1이 나오는 횟수
zero = [1,0,1]
one = [0,1,1]

# zero와 one배열의 새로운 피보나치수의 0과 1의 개수를 추가해줌
def cnt(n):
    if len(zero) <= n:
        for i in range(len(zero), n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])         
    print(zero[n], one[n])
test = int(input())
for i in range(test):
    N = int(input())
    cnt(N)

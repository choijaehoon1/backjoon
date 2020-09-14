# 그리디 제일 욕심적인 해를 구하는 것(탐욕적)
# 어떻게 해야 최고로 욕심적으로 풀 수 있을까?
n, k = map(int, input().split())

cnt = 0
result = 0
while True:
    # 3으로 나누어떨어지는 수 만들기
    target = (n//k) * k
    result += (n - target) # 3으로 나누어 떨어지는 수가 될때까지 만들어준 횟수임(즉 1씩 빼주는 것의 횟수)
    n = target
    # 더이상 나눌 수 없으면 빠져나옴
    if n < k:
        break
    n = n // k 
    result += 1

# 1 빼주기(result -= 1)
result += (n-1) # n은 0이 되서 빠져나오게됨(즉, 횟수를 한번 빼줘야 1을 만드는 횟수를 구할 수 있음)
print(result)

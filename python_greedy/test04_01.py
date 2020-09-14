# 그리디 제일 욕심적인 해를 구하는 것(탐욕적)
# 어떻게 해야 최고로 욕심적으로 풀 수 있을까?
n, k = map(int, input().split())

cnt = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n = n // k
        cnt += 1
    else:
        n -= 1    
        cnt += 1
print(cnt)        

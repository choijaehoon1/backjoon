# n과 m을 입력받았을떄 n! 을 m!과 (n-m)!로 나눈 값이 조합입니다.
# 1. n!가 가지고 있는 2의 개수 - m!이 가지고 있는 2의 개수 - (n-m)!이 가지고 있는 2의 개수
# 2. n!가 가지고 있는 5의 개수 - m!이 가지고 있는 5의 개수 - (n-m)!이 가지고 있는 5의 개수
# 끝자리 0의 개수는 1과 2중에 작은 수

n,m = map(int, input().split())

def divide_2(n):
    cnt = 0
    while n != 0:
        cnt += n // 2
        n //= 2
    return cnt        

def divide_5(n):
    cnt = 0
    while n != 0:
        cnt += n // 5
        n //= 5
    return cnt

result = min((divide_2(n) - divide_2(m) - divide_2(n-m)),(divide_5(n) - divide_5(m) - divide_5(n-m)))    
print(result)

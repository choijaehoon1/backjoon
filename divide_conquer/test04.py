A,B,C = map(int, input().split())

# b가 짝수인지 홀수인지 판단
# 10 * 10 = (10 * 5)^2 형태로 변환(b가 짝수)
# 10 * 11 = (10 * 5)^2 * 10 형태로 변환(b가 홀수)
def power(a,b):
    if b == 1:  # b가 1 이면 그냥 값을 리턴해도 됨
        return a%C
    else:
        tmp = power(a, b//2) # 미리 구해놓음
        if b % 2 == 0:
            return tmp * tmp % C
        else:
            return tmp * tmp * a % C 
print(power(A,B))

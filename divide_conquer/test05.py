# 페르마의 소정리는 p가 소수이고 a가 정수이면 
# a^(p-1) % p = 1가 성립 한다는 것이다.
# 이 식을 활용 하기 위해 양변에 a^-1을 곱하면
# (a^-1 * a^(p-1)) % p = (a^-1) % p
# (a^(p-2)) % p = (a^-1) % p
N, K = map(int,input().split())
def power(a,b):
    if b == 0:
        return 1

    if b % 2 == 0:
        return (power(a,b//2) ** 2) % p    
    else:
        return (power(a,b//2) ** 2 * a) %p

p = 1000000007
fact = [1 for _ in range(N+1)]

for i in range(2,N+1):
    fact[i] = fact[i-1] * i %p
# print(fact)    

A = fact[N] 
B = fact[N-K] * fact[K] 

# (a^(p-2)) % p = (a^-1) % p
# (A/B) % p
# (A * B^-1) % p
# (A * B^p-2) % p
# (A%p) * (B^p-2 % p) 
A = (A%p)
B = (power(B,p-2)%p)
print((A*B) %p)

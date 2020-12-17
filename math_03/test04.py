import math
a,b = map(int,input().split())
gcd = math.gcd(a,b)
tmp_a = a // gcd
tmp_b = b // gcd
result = tmp_a * tmp_b * gcd

print(gcd)
print(result)


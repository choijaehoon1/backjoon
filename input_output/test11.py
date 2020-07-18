a = int(input())
b = int(input())

x = b % 10  # 5
# print(x)
b = b // 10
y = b % 10
# print(y)
b = b // 10
z = b % 10
# print(z)
print(a * x)
print(a * y)
print(a * z)
print((a * x) + (a * y) * 10 + (a * z) * 100)


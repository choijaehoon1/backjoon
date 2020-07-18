num_list = []
result = []
for i in range(10):
    N = int(input())
    num_list.append(N)
# print(num_list)
for i in num_list:
    tmp = i % 42
    if tmp in result:
        continue
    else:
        result.append(tmp)
print(len(result))

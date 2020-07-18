res_list = []
for i in range(10):
    N = int(input())
    res = N%42
    res_list.append(res)
# print(res_list)
res_list = set(res_list)
print(len(res_list))

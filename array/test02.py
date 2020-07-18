num_list = []
for i in range(1,10):
    n = int(input())
    num_list.append(n)
# print(num_list)

max_result = max(num_list)
max_line = num_list.index(max_result)+1
print(max_result)
print(max_line)

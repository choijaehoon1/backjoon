from itertools import permutations
import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
add,sub,mal,div = map(int, sys.stdin.readline().rstrip().split())

asmd_list = []
if add > 0:
    for _ in range(add):
        asmd_list.append('+')        
if sub > 0:
    for _ in range(sub):
        asmd_list.append('-')
if mal > 0:
    for _ in range(mal):
        asmd_list.append('*')
if div > 0:
    for _ in range(div):
        asmd_list.append('/')                

pm_list = list(permutations(asmd_list,n-1))
answer = []
for i in range(len(pm_list)):
    tmp = array[0]
    for j in range(n-1):
        if pm_list[i][j] == '+':
            tmp += array[j+1]
        if pm_list[i][j] == '-':
            tmp -= array[j+1]
        if pm_list[i][j] == '*':
            tmp *= array[j+1]
        if pm_list[i][j] == '/':
            tmp = int(tmp/array[j+1])
    answer.append(tmp)
print(max(answer))
print(min(answer))                

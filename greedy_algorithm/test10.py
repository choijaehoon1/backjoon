n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
# print(arr)    
ans = 0
minus = []
plus = []

for num in arr:
    if num == 1: # 1일때는 더 하는게 가장 큼
        ans += 1
    elif num <=0: # 0이거나 음수일때는 minus쪽에 저장
        minus.append(num)
    elif num >0: # 양수는 plus쪽에 저장
        plus.append(num)
minus.sort()
plus.sort(reverse=True)
# print(minus)
# print(plus)                
for i in range(0,len(minus),2):
    if i+1 < len(minus): # 두번째 묶을 숫자가 전체길이보다 작을때는 묶어서 곱함
        ans += minus[i] * minus[i+1]
    else: # 아닐시는 마지막 숫자 하나 남은것이므로 그냥 더함
        ans += minus[i]    

for i in range(0,len(plus),2):
    if i+1 < len(plus):
        ans += plus[i] * plus[i+1]
    else:
        ans += plus[i]
print(ans)        

from collections import Counter
import sys
n = int(sys.stdin.readline().rstrip())
array = []
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))
array.sort()
# print(array)    

sum_value = 0
count_value = 0
for i in array:
    sum_value += i
print(format(round(sum_value/n,0),".0f")) # 평균    
print(array[n//2]) # 중앙 값

# Counter함수(리스트): 리스트에 원소에 대해 개수 반환
# print(Counter(array))
mode_dict = Counter(array)
modes = mode_dict.most_common() # 빈도수가 높은순으로 튜플형태로 만들어줌(원소, 빈도수)
# print(modes)
if len(array) > 1:
    if modes[0][1] == modes[1][1]: # 빈도수가 같으면 2번째 원소 출력
        print(modes[1][0])
    else: # 같지 않으면 첫번째꺼가 빈도수 제일크니 첫번째 출력
        print(modes[0][0])
else: # 하나일 경우는 첫번째 원소의 값을 출력 
    print(modes[0][0])     

print(max(array) - min(array))

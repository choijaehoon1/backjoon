# - 기준으로 잘라서 앞에 부분의 값만 저장하고 
# 뒤에 괄호를 쳐서 뺄 때가 최솟값이 된다.
arr = input().split('-')
# print(arr) # arr은 배열이므로 ['55', '50+40']

num = 0
# 0번째 인자에 연산자 + 가 있을 수도 있음
# split()함수는 만약 지정한 문자가 없을시 그냥 그대로 출력됨
for i in arr[0].split('+'): # split함수를 쓰면 반환값을 list형 
    # print(i)
    num += int(i)

for i in arr[1:]:
    for j in i.split('+'): # split함수를 쓰면 반환값을 list형
        num -= int(j)        
print(num)    

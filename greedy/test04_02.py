# 최소값을 만들려면 -를 기준으로 괄호를 치면 된다.
arr = input().split('-')

answer = []
for i in arr:
    inner_arr = i.split('+') # +가 없든 있든 그냥 괄호를 기준으로 잘라서
    num = 0                  # 리스트에 우선 다 넣음
    for j in inner_arr:
        num += int(j)        # 괄호 덩어리안에 거 더한 후
    answer.append(num)       # 더해줌
# print(answer)
result = answer[0]            # 맨 앞에 숫자는 더 해주고

for i in range(1,len(answer)):# 나머지는 다 빼줌
    result -= answer[i]
print(result)

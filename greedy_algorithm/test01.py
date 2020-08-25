n = int(input())
# print(n//5)
cnt = 0
# 최대 5kg 개수와 나머지 구하기
five = n//5
res = n % 5
three = 0
# 나머지가 0이 아니면 3kg 개수 구함
if res != 0:
    while five >=0:
        if res % 3 == 0:
            three = res//3
            break
        five -=1    # 몫을 줄이고
        res += 5    # 나머지를 늘려 정확히 3kg로 나누어떨어질때 구하기

# 3kg와 5kg이 하나도 없는경우
if cnt <1:
    cnt = -1
cnt = five + three
print(cnt)        


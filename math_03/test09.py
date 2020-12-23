# 종류 1이 n개, 종류 2가 m개 주어진다면 종류 1과 종류 2를 조합하는 경우의 수는 n*m 개
# 다만 주의해야할 점은 이 경우의 수는 모든 종류별로 하나씩 골라야 했을 때의 경우의 수입니다.
# 하지만 이 문제에서는 종류 1은 고르지 않고 종류 2만 선택하는 경우도 발생할 수 있습니다. 
# ex) (선글라스만 끼고 일하는 노출증 있는 스파이랍니다.) 
# 그렇기 때문에 선택하지 않는다. 라는 선택으로 (n+1) * (m+1) 으로 경우의 수가 나타납니다.

tc = int(input())
for _ in range(tc):
    n = int(input())
    closet = {}
    for i in range(n):
        close, close_type = input().split()
        if close_type in closet:
            closet[close_type].append([close])
        else:
            closet[close_type] = [close]

    cnt = 1
    for i in closet.keys():
        cnt *= len(closet[i]) + 1
    print(cnt-1) # 모두 안입은 경우를 제외시킨다.

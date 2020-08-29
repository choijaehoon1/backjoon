n, m = map(int, input().split())

if n == 1: # 높이가 1일때는 무조건 1
    print(1)
elif n == 2: # 높이가 2일때는 m값이 1,2 -> 1
             # 높이가 2일때는 m값이 3,4 -> 2 ...
    print(min(4,(m+1)//2))
else: # n >= 3클때
    if m <= 6: # m이 7보다 작으면 모든 4가지경우를 수행하지 못함(3가지까지 밖에)
        print(min(4,m))
    else:
        print(m-2)    

num = 0
while True:
    l,p,v=map(int, input().split())
    
    if l == p == v == 0:
        break
    x = v // p
    if l>=v%p:
        ans = l * x + (v%p)
    else: # 예외: 나머지가 더클 경우 L만 더해줘야함
        ans = l* x + l 
    num +=1
    print("Case %d: %d" %(num,ans))


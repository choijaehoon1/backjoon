import sys
a,b,c = map(int, sys.stdin.readline().rstrip().split())

# a + b*n = c*n일 때 같음
if b >= c: # b가 c보다 같거나 크게되면 손익분기점은 업슴
    print(-1)
else: # c와 b의 차이만큼 줄어들게 되고 같아질때보다 1클때가 정답    
    print(int(a/(c-b))+1)

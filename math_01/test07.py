import sys
tc = int(sys.stdin.readline().rstrip())
# 1 1 -> (1)
# 2 1 1 -> (2)
# 3 1 1 1 -> (3) 양옆이 1이므로 연결되어있으므로 그 다음에 2 가능
# 4 1 2 1 -> (3)
# 5 1 2 1 1 -> (4)
# 6 1 2 2 1 -> (4)
# 7 1 2 2 1 1 -> (5)
# 8 1 2 2 2 1 -> (5) 양옆이 2이므로 연결되어있으므로 그 다음에 3 가능
# 9 1 2 3 2 1 -> (5)

for _ in range(tc):
    x,y = map(int, sys.stdin.readline().rstrip().split())    
    dist = y - x
    start = 0
    tmp = 1
    cnt = 0

    while start < dist:
        start += tmp
        cnt+=1
        if start < dist:
            start += tmp
            cnt+=1
        else:
            break
        tmp += 1 # 1 만큼 이동    
    print(cnt)
    

tc = int(input())

for _ in range(tc):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    r = ((x2-x1)**2 + (y2-y1)**2)**0.5 # 원과 원사이 거리
    r_list = [r,r1,r2]
    max_r = max(r_list)
    r_list.remove(max_r)

    if r == 0 and r1 == r2: # 두 원이 일치하는 경우
        print(-1)
    else:
        if r == (r1 + r2) or max_r == sum(r_list): # 외접하거나 내접하는 경우
            print(1)
        else:
            if max_r > sum(r_list): # 두 원이 만나지 않는 경우
                print(0)
            else: # 두 원이 두 점에서 만나는 경우
                print(2)                      


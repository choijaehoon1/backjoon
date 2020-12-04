import math
r = int(input())
# 택시기하학: 두 대각선의 길이가 같은 사각형, 즉 마름모
x1,y1 = 0,0
x2,y2 = r,r
ucrid = math.pi * pow(r,2)
taxi = pow(r,2) * 2 # 밑변과 높이가 r인 삼각형 4개

print(format(ucrid,".6f"))
print(format(taxi,".6f"))

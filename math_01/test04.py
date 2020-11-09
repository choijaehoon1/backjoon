import sys
a,b,v = map(int, sys.stdin.readline().rstrip().split())

result = 0
# 달팽이는 하루에 a-b만큼 이동
# 목표지점에 도달했을때는 미끄러지지 않으므로 v-b만큼 올라가는 것
if (v-b) % (a-b) == 0:
    result = (v-b) // (a-b)
else: # 입력값이 실수인 경우 실수가 출려될수도 있음
    result = (v-b) // (a-b) + 1 # ex) 값이 4.2이면 5일결려야 가능이므로 +1
print(result)            

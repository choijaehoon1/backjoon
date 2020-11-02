# import copy
from collections import deque
import sys

for tc in range(int(sys.stdin.readline().rstrip())):
    p = sys.stdin.readline().rstrip()
    n = sys.stdin.readline().rstrip()
    array = sys.stdin.readline().rstrip()[1:-1]
    q = deque()

    if len(array) != 0:
        for i in array.split(','):
            q.append(int(i))    

    check = 0
    for i in p:
        if i == 'R': # 방향뒤집기
            if check == 0:
                check = 1
            elif check == 1:
                check = 0    
        elif i == 'D':
            if len(q) == 0:
                check = 2
                break
            if check == 0: # 정방향은 맨앞꺼빼기
                q.popleft()
            elif check == 1: # 역방향은 맨뒤꺼빼기
                q.pop()         
    
    if check == 1: # check가 1이면 방향뒤집어야함
        q.reverse() # reverse가 시간많이사용하므로 여기서만해줌
    if check == 2:
        print('error')    
    else:
        print('[',end='')
        for i in range(len(q)):
            print(q[i],end='')
            if i != len(q)-1:
                print(',',end='')
        print(']')

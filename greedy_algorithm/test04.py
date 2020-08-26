import sys
test = int(sys.stdin.readline())

for _ in range(test):
    n = int(input())
    s = [0 for _ in range(n+1)]
    # 서류 성적기준 오름차순으로 정렬됨
    for i in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        s[a] = b
    # print(s)
    min = s[1]
    cnt = 0
    for i in range(2,n+1):
        if s[i] > min:
            cnt += 1  
        else: # min보다 작은 값이 있다면 min에 저장해준다.
            min = s[i]   
    print(n-cnt)               

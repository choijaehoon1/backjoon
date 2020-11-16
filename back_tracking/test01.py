n,m = map(int, input().split())

visit = [False] * (n+1) # 1부터 n까지만 사용
array = [0 for i in range(m)] # array는 m 길이 만큼 만들어 줌(0으로 초기화)

def back_tracking(index):
    if index == m: # 끝까지 도착하면
        print(' '.join(map(str,array))) # 리스트를 map함수를 이용하여 str로 만든후 join
        return    
    
    for i in range(1,n+1):
        if visit[i] == False: # 방문하지 않았을 때만
            visit[i] = True # 방문처리
            array[index] = i
            back_tracking(index+1)
            visit[i] = False # 원상복구
back_tracking(0)         

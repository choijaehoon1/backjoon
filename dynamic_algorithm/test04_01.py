n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
# print(arr)    

answer = 0
def go(day, total):
    global answer
    if day == n: # 알맞게 도착했을 때 정답
        answer = max(answer,total)
        return
    if day > n: # 기간 넘어가면 안됨
        return

    go(day+1,total) # 그냥 넘어가는 경우
    go(day+arr[day][0], total + arr[day][1]) # 일을 처리 but 기간도 점프
go(0,0)
print(answer)    

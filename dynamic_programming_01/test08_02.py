def cal(a):
    list = []
    for i in a:
        list.append(i-1)
        if i%3 ==0:
            list.append(i/3)
        if i%2 ==0:
            list.append(i/2)  
    return list      

n = int(input())          
arr = [n]
cnt = 0

while True:
    if n == 1:
        print(cnt)
        break
    temp = arr
    arr = cal(temp)
    cnt += 1
    if min(arr) ==1: # 1이 나오면 그떄의 cnt값 리턴
        print(cnt)
        break

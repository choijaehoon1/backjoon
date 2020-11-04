n = int(input())

cnt = 1
cnt_six = 6
result = 1

while n > cnt:
    cnt += cnt_six
    cnt_six += 6
    result +=1
print(result)    

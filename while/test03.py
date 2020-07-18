tmp = N = int(input())
cnt = 0
while True:
    a = tmp // 10 # 앞자리 2
    b = tmp % 10 # 뒷자리 6

    c = a + b # 더한 값 8
    tmp = int(str(tmp%10) + str(c%10)) # 68
    cnt += 1
    if(tmp == N):
        break;
print(cnt)


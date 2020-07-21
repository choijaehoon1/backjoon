def solution(num):
    answer = num

    while True:
        a = num % 10
        num //= 10
        answer += a
        if(num == 0):
            break
    return answer

list1 = []
list2 = []
for i in list(range(1,10001)):
    list1.append(solution(i))
    if i not in list1:
        list2.append(i)
for i in list2:
    print(i)

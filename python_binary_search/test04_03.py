# set()함수를 이용한 풀이
n = int(input())
# 단순히 특정 데이터가 존재하는지 검사할 때 매우 효과적
# set 중복제거(이것도 리스트 형태임)
total = set(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))
total = sorted(total)
want = sorted(want)


for i in want:
    if i in total:
        print('yes',end=' ')
    else:
        print('no',end=' ')    

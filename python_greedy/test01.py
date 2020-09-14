# 가지고 있는 동전의 큰 단위는 항상 작은 단위 배수관계
n = int(input())
# 큰단위 화폐부터 확인
coin_type = [500,100,50,10]
count = 0 

for i in coin_type:
    count += n // i # 해당 화폐로 거슬러줄 수 있는 동전 개수
    n %= i
print(count)     

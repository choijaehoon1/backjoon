# 한번 계산된 결과를 메모이제이션 하기위한 리스트
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한적 있으면 그대로 반환    
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에따라 피보나치 결과반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
print(fibo(6))            

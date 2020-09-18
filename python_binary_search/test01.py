# 순차 탐색: 리스트에 특정한 값의 원소가 있는지 체크하거나
#            특정한 값을 가지는 원소으 개수를 세는 count()메소드에 사용

def sequential(n,target,array):
    for i in range(n):
        if array[i] == target:
            return i+1 # 인댁수눈 0부터 시작


print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input()
n = int(input_data.split()[0])
target = input_data.split()[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다")
array = input().split()
print(sequential(n,target,array))

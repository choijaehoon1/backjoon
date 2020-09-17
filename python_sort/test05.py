# 정렬 라이브러리(sorted)
array = [7,5,9,0,3,1,6,2,4,8]
result = sorted(array)
print(result)

# 정렬 라이브러리(sort)
array = [7,5,9,0,3,1,6,2,4,8]
array.sort()
print(array)

# 리스트안에 튜플
# 함수 선언방식
array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]
result = sorted(array, key=setting)     
print(result)

# 리스트안에 튜플
# 람다식: 첫번째 원소를 기준으로 정렬
array = [('바나나',2),('사과',5),('당근',3)]
result = sorted(array, key=lambda a: a[1])
print(result)

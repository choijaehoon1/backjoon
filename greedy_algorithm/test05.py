num_list = [9,8,7,6,5,4,3,2,1,0]

test = int(input())

str_list = []
for i in range(test):
    str_list.append(input())
# print(str_list)    

alphabet = [0 for i in range(26)]

for str in str_list: # 한 문자씩 추출
    i = 0
    while str:
        tmp = str[-1] # 가장 뒤에 문자 부터 확인
        alphabet[ord(tmp) - ord('A')] += pow(10,i)
        i += 1
        str = str[:-1] # 가장 마지막문자 앞까지 split하므로 마지막문자 제외됨
alphabet.sort(reverse=True) 
# print(alphabet)  

answer = 0
for i in range(9,-1,-1):
    answer += alphabet[i] * (9-i)
print(answer)    

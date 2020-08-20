n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input())))
# print(arr)    

def check(x,y,n):
    tmp = arr[x][y]
    result = []

    if n == 1:
        return str(tmp)

    for i in range(x,x+n):
        for j in range(y,y+n):
            if tmp != arr[i][j]:
                result.append('(')
                result.extend(check(x,y,n//2))      # 1사분면
                result.extend(check(x,y+n//2,n//2)) # 2사분면
                result.extend(check(x+n//2,y,n//2)) # 3사분면
                result.extend(check(x+n//2,y+n//2,n//2)) # 4사분면
                result.append(')')
                return result
    
    return str(tmp)
print(''.join(check(0,0,n)))

cnt = [-1] * 26
str = input()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(str)):
    if str[i] in alpha:        
        index = alpha.index(str[i])        
        if cnt[index] != -1:
            continue
        cnt[index] = i
print(*cnt)        

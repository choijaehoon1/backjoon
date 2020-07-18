str = input()
str = str.split(' ')
a = int(str[0])
b = int(str[1])

if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')

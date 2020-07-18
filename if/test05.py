str = input()
str = str.split(' ')
H = int(str[0])
M = int(str[1])

if M >= 45:
    M = M - 45
    print(H, M)
else:
    M = (M+60) - 45
    if H == 0:
        H = (H+24) - 1
        print(H, M)
    else:
        H = H - 1
        print(H, M)

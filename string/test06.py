test = input().strip()
cnt = test.count(' ')
if test == '':
    print(0)
elif cnt == 0:
    print(1)
else:
    print(cnt+1)    

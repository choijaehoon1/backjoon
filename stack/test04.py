while True:
    str = input()
    if str == '.':
        break
    arr = []
    answer =True
    for i in str:
        if i == '(' or i == '[':
            arr.append(i)
        elif i == ')':
            try:
                if arr[-1] == '(':
                    arr.pop()
                else:
                    answer = False
                    break
            except:
                answer = False
                break
        elif i == ']':
            try:
                if arr[-1] == '[':
                    arr.pop()
                else:
                    answer = False
                    break
            except:
                answer = False
                break      
    if len(arr) == 0 and answer == True:
        print("yes")
    else:
        print("no")

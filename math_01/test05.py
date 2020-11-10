import sys
tc = int(sys.stdin.readline().rstrip())
for i in range(tc):
    h,w,n = map(int, sys.stdin.readline().rstrip().split())
    ho = 0
    res = 0
    result = ""
    if n % h == 0:
        ho = n//h
        res = h
    else:
        ho = (n//h) + 1
        res = n % h
    if h*9 < n:
        result = str(res) + str(ho)        
    else:                
        result = str(res) + str(0)+ str(ho)
    print(result)

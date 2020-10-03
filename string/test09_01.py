remove_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input()
result = 0 
for i in remove_list:
    if i in a:
        result += a.count(i)        
print(len(a) - result)    

remove_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input()

for i in remove_list:
    a = a.replace(i,'a')
print(len(a))    

x,y,w,h = map(int, input().split())

start = 0

array = [x-start,w-x, y-start, h-y]
print(min(array))

import sys
from bisect import bisect_left
n = int(sys.stdin.readline().rstrip())
array = list(map(int,sys.stdin.readline().rstrip().split()))

dp = []

for i in array:
    k = bisect_left(dp,i)
    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i          
print(len(dp))

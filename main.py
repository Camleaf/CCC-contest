# idea for optimization. only store top two layers. will need to fix system though
import sys
#print = sys.stdout.write
input = sys.stdin.readline
#solves for first 5 part marks

N,M,Q = list(map(int,input().split(" ")))

highest_prettiness = [0 for _ in range(M)]
greatest_second:int = 0

for i in range(N):
    c,p = list(map(int,input().split(" ")))
    
    if (highest_prettiness[c-1] < p):
        greatest_second = max(greatest_second,highest_prettiness[c-1])
        highest_prettiness[c-1] = p
    
    elif (greatest_second < p):
        greatest_second = p


lowest_high = min(highest_prettiness)
#print(lowest_high, greatest_second, highest_prettiness)
total = sum(highest_prettiness) - lowest_high + max(lowest_high,greatest_second)

_=print(str(total))

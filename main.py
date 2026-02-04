# idea for optimization. only store top two layers. will need to fix system though
import sys
print = sys.stdout.write
input = sys.stdin.readline
#solves for first 5 part marks

N,M,Q = list(map(int,input().split(" ")))

highest_prettiness = [0 for _ in range(M)]
lowest_high:int = 0
greatest_second:int = 0

for i in range(N):
    c,p = list(map(int,input().split(" ")))
    
    if (highest_prettiness[c-1] < p):
        highest_prettiness[c-1] = p

        if (lowest_high == 0 or lowest_high > p):
            lowest_high = p
    
    elif (greatest_second < p):
        greatest_second = p

total = sum(highest_prettiness) - lowest_high + max(lowest_high,greatest_second)

_=print(str(total)+"\n")

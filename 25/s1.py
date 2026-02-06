### ccc '25 s1


x1,y1,x2,y2 = list(map(int,input().split(" ")))


print(2*min(
        (x1+x2) + max(y1,y2), 
        (y1+y2) + max(x1,x2)
    )
)


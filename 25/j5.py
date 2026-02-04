### ccc '25 j5

rows:int = int(input())
cols:int = int(input())
max_count:int = int(input())


# use caching
def get_tile_cost(x:int,y:int) -> int:
    
    return 0

cached = {}

def dfs(x:int,y:int,cost:int)->int:
    
    cost += get_tile_cost(x,y)
    

    # propogate downstream

    downstream_arr:list[int] = []
    for n_x in ((-1+x),(x),(1+x)):
        
        if (n_x < 0 or n_x >= rows): 
            continue

        downstream_arr.append(
            dfs(n_x, y+1,cost),
        )

    minimum = min(downstream_arr)
    cached[hash((x,y))] = minimum

    return minimum

        


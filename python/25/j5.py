### ccc '25 j5
from typing import Dict, List, Tuple

rows:int = int(input())
cols:int = int(input())
max_count:int = int(input())

# use caching
tile_cost_cache:Dict[Tuple[int,int],int] = {}

def get_tile_cost(x:int,y:int) -> int:
    hashed_tile = (x,y)

    if (hashed_tile in tile_cost_cache):
        return tile_cost_cache[hashed_tile]

    base = max_count - (2*y) + (x+1)
    base %= max_count
    if base == 0: base = max_count
    
    tile_cost_cache[hashed_tile] = base

    return base



dfs_cache:Dict[Tuple[int,int],int] = {}

def dfs(x:int,y:int)->int:


    if (y == rows-1):
        return get_tile_cost(x,y)

    hashed_tile = (x,y)

    if (hashed_tile in dfs_cache):
        return dfs_cache[hashed_tile]

    # propogate downstream

    # base case
    
    downstream_arr:List[int] = []
    for n_x in ((x-1),(x),(x+1)):

        if (n_x < 0 or n_x >= cols):
            continue

        downstream_arr.append(
            dfs(n_x, y+1),
        )

    minimum = min(downstream_arr) + get_tile_cost(x,y)

    dfs_cache[hashed_tile] = minimum

    return minimum

start_loc_arr:List[int] = []
for col_num in range(cols):
    start_loc_arr.append(dfs(col_num,0))

print(min(start_loc_arr))



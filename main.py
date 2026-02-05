### ccc '25 j5
from typing import Dict, List, Tuple
import sys

sys.setrecursionlimit(2147483647)
rows:int = int(input())
cols:int = int(input())
max_count:int = int(input())


def get_tile_cost(x:int,y:int) -> int:
    base = (x+1) + (y*cols)
    base %= max_count
    if base == 0: base = max_count    

    return base



dfs_cache:Dict[Tuple[int,int],int] = {}

def dfs(x:int,y:int)->int:

    # recursion err in class 3. Use the sys import thing
    if (y == rows-1):
        return get_tile_cost(x,y)

    if (get_tile_cost(0,y) == 1 and y != 0): # if it has repeated
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
dfs_value = min(start_loc_arr)


# get repeat count
repeat_y = 0
for y in range(rows):
    if (get_tile_cost(0,y) == 1):
        repeat_y = y
        break

if (repeat_y != 0):
    repeated_times:int = rows // repeat_y
    leftover:int = rows % repeat_y


print(dfs_value)



for i in range(rows):
    x = ''
    for j in range(cols):
        x += str(get_tile_cost(j,i)) +" "

    print(x)

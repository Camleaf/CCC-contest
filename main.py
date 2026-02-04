import sys
print = sys.stdout.write
input = sys.stdin.readline
#solves for part 1

### declare classes and constants

class Pen:
    colour:int # this makes heapq ignore this value when ordering the class
    prettiness:int # heapq will sort by prettiness. Least to highest

    def __init__(self, colour:int, prettiness:int):
        self.colour = colour 
        self.prettiness = prettiness  


def getMaxPrettiness(pen_heaps:dict[int,list[Pen]])->int:

    for colour in pen_heaps.keys():
        pen_heaps[colour].sort(key=lambda x: x.prettiness,reverse=True)

    # find greatest second pen, to switch
    
    second_biggest:Pen|None = None
    first_smallest:Pen|None = None

    for colour in pen_heaps.keys():
        if (len(pen_heaps[colour]) == 0): continue

        #track the most pretty of the second-prettiest of each colour
        if len(pen_heaps[colour])>1:
            test_pen = pen_heaps[colour][1]
            if (second_biggest is not None):
                if test_pen.prettiness > second_biggest.prettiness:
                    second_biggest = test_pen
            else:
                second_biggest = test_pen

        

        # track the lesat pretty of the prettiest of each colour
        
        test_pen = pen_heaps[colour][0]
        if (first_smallest is not None):
            if test_pen.prettiness < first_smallest.prettiness:
                first_smallest = test_pen
        else:
            first_smallest = test_pen


    prettiness = 0
    if (first_smallest is not None):
        prettiness = first_smallest.prettiness

        if (second_biggest is not None):
            prettiness = first_smallest.prettiness if first_smallest.prettiness > second_biggest.prettiness else second_biggest.prettiness
    

        for colour in pen_heaps.keys():
            if (len(pen_heaps[colour]) == 0): continue
    
            if colour == first_smallest.colour:
                continue

            prettiness += pen_heaps[colour][0].prettiness
    return prettiness # to compile REMOVE THIS LINE



### solve

# get first line from input
pens,colours,images = list(map(int,input().split(" ")))


# declare variables
pen_heaps:dict[int,list[Pen]] = {x+1:[] for x in range(colours)} # organized by colour in the dict, then by ordered list


pen_address:dict[int,Pen] = {}

# grab rest of input
for i in range(pens):
    colour, prettiness = list(map(int,input().split(" ")))

    # push newly made Pen object to priority queue
    pen:Pen = Pen(colour,prettiness)
    
    pen_heaps[colour].append(pen)
    pen_address[i] = pen


_=print(str(getMaxPrettiness(pen_heaps))+"\n")

for image_num in range(images):
    mode, index, new = list(map(int,input().split(" ")))
    
    idx_pen:Pen = pen_address[index-1]
    
    if mode == 1:
        pen_heaps[idx_pen.colour].remove(idx_pen)
        idx_pen.colour = new
        pen_heaps[idx_pen.colour].append(idx_pen)
        
    else:
        pen_address[index-1].prettiness = new

    
    _=print(str(getMaxPrettiness(pen_heaps))+"\n")




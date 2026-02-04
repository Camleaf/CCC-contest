import heapq
from dataclasses import dataclass, field

#solves for part 1

### declare classes and constants

@dataclass(order=True)
class Pen:
    colour:int=field(compare=False) # this makes heapq ignore this value when ordering the class
    prettiness:int # heapq will sort by prettiness. Least to highest

    def __init__(self, colour:int, prettiness:int):
        self.colour = colour 
        self.prettiness = -prettiness  # negative so that we get to use max_heap


    def __repr(self):
        return f"C: {self.colour} | P: {self.prettiness}"



def getMaxPrettiness(pen_heaps:dict[int,list[Pen]],colours:int)->int:
    # find greatest second pen, to switch
    
    second_biggest:Pen|None = None
    first_smallest:Pen|None = None

    for colour in pen_heaps.keys():
        if (len(pen_heaps[colour]) == 0): continue

        #track the most pretty of the second-prettiest of each colour
        if len(pen_heaps[colour])>1:
            test_pen = pen_heaps[colour][1]
            if (second_biggest is not None):
                if test_pen.prettiness < second_biggest.prettiness:
                    second_biggest = test_pen
            else:
                second_biggest = test_pen

        

        # track the lesat pretty of the prettiest of each colour
        
        test_pen = pen_heaps[colour][0]
        if (first_smallest is not None):
            if test_pen.prettiness > first_smallest.prettiness:
                first_smallest = test_pen
        else:
            first_smallest = test_pen


    prettiness = 0
    if (first_smallest is not None):
        prettiness = first_smallest.prettiness

        if (second_biggest is not None):
            prettiness = first_smallest.prettiness if first_smallest.prettiness < second_biggest.prettiness else second_biggest.prettiness
    

        for colour in pen_heaps.keys():
            if (len(pen_heaps[colour]) == 0): continue
    
            if colour == first_smallest.colour:
                continue

            prettiness += pen_heaps[colour][0].prettiness
    return -prettiness # to compile REMOVE THIS LINE



### solve

# get first line from input
pens,colours,images = list(map(int,input().split(" ")))


# declare variables
pen_heaps:dict[int,list[Pen]] = {x+1:[] for x in range(colours)} # organized by colour in the dict, then by heap


pen_address:dict[int,Pen] = {}

# grab rest of input
for i in range(pens):
    colour, prettiness = list(map(int,input().split(" ")))

    # push newly made Pen object to priority queue
    pen:Pen = Pen(colour,prettiness)
    
    heapq.heappush(pen_heaps[colour],pen)
    pen_address[i] = pen

print(getMaxPrettiness(pen_heaps,colours))




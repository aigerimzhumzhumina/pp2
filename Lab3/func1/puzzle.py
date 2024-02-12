def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if(2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits 
         
numheads = 35 
numlegs = 94 
chickens, rabbits = solve(numheads, numlegs)
print(chickens)
print(rabbits)

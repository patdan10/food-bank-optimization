import math

def main(supply, capacity, demand, equalityLimit):
    # Get capacity to demand ratio. Smaller means more demand per capacity / more urgent
    ratios = [0]*len(capacity)
    for i in range(len(ratios)):
        ratios[i] = float(capacity[i])/float(demand[i])
    
    # Initializing variables. Given is how much is given to each
    given = [0]*len(capacity)
    inf = float("inf")
    
    # While there are supplies, and not everything has been given food
    while supply > 0 and min(given) <= 0:
        # Index of most urgent place
        index = ratios.index(min(ratios))
        
        # If more space is avaliable than supply, fill as much as possible
        if capacity[index] >= supply:
            given[index] = supply
            supply = 0
            break
        else:
            # Fill to capacity, loop to find next most urgent place
            given[index] = capacity[index]
            supply -= capacity[index]
            ratios[index] = inf
    
    #Uncomment to print the result of every variable
    #print(given)
                        
    #Returns the amount of excess food
    return supply
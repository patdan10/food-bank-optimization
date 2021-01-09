import random

def main(supply, capacity, demand, equalityLimit):
    #Delta
    delta = sum(demand)
    backupSupply = supply
    
    #Bottleneck Counties
    Jzero = []
    for i in range(len(demand)):
        if float(demand[i])/float(delta) > equalityLimit:
            Jzero.append(i)
    
    #List of All With Smallest Ratio as defined below. R is just one of them
    B = []
    for i in Jzero:
        if len(B) <= 0:
            B.append(i)
            continue
        
        current = float(capacity[i])/float(demand[i]-(equalityLimit*delta))
        smallest = float(capacity[B[0]])/float(demand[B[0]]-(equalityLimit*delta))
        if current == smallest:
            B.append(i)
        elif current <= smallest:
            B = [i]
    
    if len(B) > 0:
        R = float(capacity[B[0]])/float(demand[B[0]]-(equalityLimit*delta))
    else:
        R = float("inf")
    
    #Initialization
    Xs = [0]*len(demand)
    Es = [0]*len(demand)
    Je = []
    Be = []
    
    #print(delta, Jzero, B, R)
    
    #Case 2
    if (R*delta <= supply) and (len(Jzero) > 0):
        
        # Give bottlenecks what they want, otherwise find J candidates
        for j in range(len(demand)):
            if i in Jzero:
                Xs[j] = capacity[j]
            elif (R*demand[i]) <= capacity[j]:
                Xs[j] = (R*demand[j])
                Je.append(j)
        
        #Shuffle Js
        random.shuffle(Je)
        
        #Loop through all, if J then give what want
        for l in range(len(demand)):
            if l not in Je:
                Xs[l] = capacity[l]
                Es[l] = (R*demand[l])-capacity[l]
                Be.append(l)
                #Loop through J, if not full then reset E and redistribute accordingly
                for j in Je:
                    if Xs[j]+Es[l] <= capacity[j]:
                        Xs[j] = Xs[j] + Es[l]
                        Es[l] = 0
                        break
                    else:
                        Es[l] = Es[l] - (capacity[j]-Xs[j])
                        Xs[j] = capacity[j]
                        Bs.append(E)
    #Cases 1 and 3
    else:
        #Find Js
        for j in range(len(demand)):
            if ((supply*demand[j])/delta) <= capacity[j]:
                Xs[j] = (supply*demand[j])/delta
                Je.append(j)]
        
        random.shuffle(Je)
        
        #All counties, if not J then add to capacity
        for l in range(len(demand)):
            if l not in Je:
                Xs[l] = capacity[l]
                Es[l] = ((supply*demand[j])/delta)-capacity[l]
                Be.append(l)
                
                #Redistribute as necessary
                for j in range(len(Je)):
                    if (Xs[j]+Es[l]) <= capacity[j]:
                        Xs[j] = Xs[j] + Es[l]
                        Es[l] = 0
                        break
                    else:
                        Es[l] = Es[l] - (capacity[j]-Xs[j])
                        Xs[j] = capacity[j]
                        Be.append(j)
    
    #Uncomment to print the result of every variable
    #print(Xs)
                        
    #Returns the amount of excess food
    return backupSupply-sum(Xs)
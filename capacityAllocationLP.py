from gurobipy import *

def main(supply, capacity, demand, equalityLimit, addedCapacity):
    #initializations
    delta = sum(demand)
    bottleNeck = range(len(demand))
    
    
    capAlloc = Model("lbp")
    
    #Make Fraction Decision Variables. A given one represents the amount of food given to a node
    fracVars = []
    for i in range(len(bottleNeck)):
        fracVars.append(capAlloc.addVar(lb = 0.0, ub = 1, vtype=GRB.CONTINUOUS, name = "FRAC "+str(bottleNeck[i])))
    
    #Make Q
    maxMCD = capAlloc.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name = "Q")
    
    # Accounting
    capAlloc.addConstr(sum(fracVars), GRB. LESS_EQUAL, 1)
    
    #Limit Q
    for i in range(len(bottleNeck)):
        capAlloc.addConstr((maxMCD*demand[i])-(equalityLimit*delta), GRB.LESS_EQUAL, capacity[i]+(fracVars[i]*addedCapacity))
    
    
    capAlloc.update()
    
    #Objective Function - Maximize Ratio
    capAlloc.setObjective(maxMCD, GRB.MAXIMIZE)
    
    capAlloc.update()
    
    #Objective Function - Maximize Ratio
    capAlloc.setObjective(maxMCD, GRB.MAXIMIZE)
    
    capAlloc.update()
    capAlloc.optimize()
    
    
    #Uncomment to print the result of every variable
    #capAlloc.printAttr('x')
    
    #Returns the lowest MCD
    return capAlloc.getObjective().getValue()
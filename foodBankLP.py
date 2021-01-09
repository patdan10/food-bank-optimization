from gurobipy import *

def main(supply, capacity, demand, equalityLimit):
    foodDist = Model("lbp")
    
    #Make Decision Variables. A given one represents the amount of food given to a node
    nodeVars = []
    for i in range(len(demand)):
        nodeVars.append(foodDist.addVar(lb = 0, ub = capacity[i], vtype=GRB.INTEGER, name = "NODE "+str(i)))
    
    #Add ratio constraints
    for i in range(len(nodeVars)):
        foodDist.addConstr(nodeVars[i], GRB.LESS_EQUAL, sum(nodeVars[j] for j in range(len(nodeVars)))*(equalityLimit+(demand[i]/float(sum(demand)))), name="RATIO "+str(i))

    #Maximum food is supply
    foodDist.addConstr(sum(nodeVars), GRB.LESS_EQUAL, supply, name="SUPPLY")
    
    foodDist.update()
    
    #Objective Function - Minimize Waste
    foodDist.setObjective(sum(nodeVars[i] for i in range(len(nodeVars))), GRB.MAXIMIZE)
    
    foodDist.update()
    foodDist.optimize()
    
    #Uncomment to print the result of every variable
    #foodDist.printAttr('x')
    
    #Returns the amount of excess food
    return supply-foodDist.getObjective().getValue()
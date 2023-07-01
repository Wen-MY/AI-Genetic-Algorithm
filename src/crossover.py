def crossover(parent1, parent2):
    
    # Replace the dummy crossover function below with 
    # Partially Mapped Crossover approach.
   
    
    #define the crossover point 
    #first this using fixed crossover point which 3 and 6
    crossoverpoint1 = 3
    crossoverpoint2 = 9
    #second this using random crossover point which will sure not duplicate
    #rng = np.random.default_rng(seed=seed)
    #crossoverpoint1, crossoverpoint2 = np.sort(rng.choice(np.arange(len(parent1)-1), size=2, replace=False))
    
    #print (parent1) #debug purpose
    #print (parent2) #debug purpose
    
    #define the crossover function that will not duplicate the gene which purposely for TSP problem
    def PartialMappedCrossover(parent1,parent2):
        child = []
        count = 0
        for i in parent1:
            if(count == crossoverpoint1):
                break
            if(i not in parent2[crossoverpoint1:crossoverpoint2]):
                child.append(i)
                count= count+1

        #select the genes within the crossover points from parent2          
        child.extend(parent2[crossoverpoint1:crossoverpoint2])
        #fill in the remaining genes in order of parent1
        child.extend([x for x in parent1 if x not in child])
        return child
    child1 = PartialMappedCrossover(parent1,parent2)
    #print(child1) #debug purpose
    child2 = PartialMappedCrossover(parent2,parent1)
    #print(child2) #debug purpose
    
    return child1, child2

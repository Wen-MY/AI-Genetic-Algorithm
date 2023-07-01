def parentSelectionR(population, poolSize=None):
    
    # Replace the dummy parent selection function below with  
    # Proportional Selection.
       
    # compare the performance achieved by Random Selection, 
    # Proportional Selection during performance evaluation 
    
    if poolSize == None:
        poolSize = len(population)
        
    matingPool = []
    
    # Replacement starts here
    prbs = []
    sum = 0
    for i in range(len(population)):  # Computes the totallity of the population fitness
        sum += Fitness(population[i]).routeFitness() 
    for i in range(len(population)):      # Computes for each route the probability 
         prbs.append(Fitness(population[i]).routeFitness()/sum)
    winner = np.random.choice(len(population),2,replace=False,p = prbs)   # Making the probabilities for a minimization problem
    for x in range(0,2): #adding winners into matingPool
        matingPool.append(population[winner[x]])
    # Replacement ends here
    
    return matingPool

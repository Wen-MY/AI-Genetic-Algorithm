def parentSelectionT(population, poolSize=None):
    
    # Replace the dummy parent selection function below with  
    # Tournament Selection.
      
    
    # compare the performance achieved by Random Selection, 
    # Tournament Selection, during performance evaluation 
    # run either Random Selection, Tournament Selection, or
    
    if poolSize == None:
        poolSize = len(population)
        
    matingPool = []

    TournamentPool=population.copy()
    for x in range(0,2):
        tournament = random.choices(TournamentPool, k=5) #tournament size = 5
        max_fitness = Fitness(tournament[0]).routeFitness()
        winner = tournament[0]
        for i in range (1,len(tournament)):
            fitness = Fitness(tournament[i]).routeFitness()
            if max_fitness < fitness:
                max_fitness = Fitness(tournament[i]).routeFitness()
                winner = tournament[i]
        matingPool.append(winner) # append winner into mating pool
        TournamentPool.remove(winner) #remove the first winner to prevent duplicate parent selection
    
    return matingPool

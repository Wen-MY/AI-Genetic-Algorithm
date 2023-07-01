def survivorSelection(population, eliteSize):
    
    # Replace the dummy survival selection function below with  
    # Merge, Sort & Truncate.
      
    
    elites = []
    
    eliminations = population.copy()
    for i in range(eliteSize):
        max_fitness = Fitness(eliminations[0]).routeFitness()
        elite = eliminations[0]
        for x in range(1,len(eliminations)):
            fitness = Fitness(eliminations[x]).routeFitness()
            if max_fitness < fitness:
                max_fitness = Fitness(eliminations[x]).routeFitness()
                elite = eliminations[x]
        elites.append(elite)
        eliminations.remove(elite)
    
    return elites

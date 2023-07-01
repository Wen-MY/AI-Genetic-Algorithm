def genCityList(filename):
    cityList = []
    
    # Replace the following codes that generate 12 random cities.
    # an initial population.  
    
    

    df = pd.read_csv(filename,sep=" |\t",names=["number","X","Y"],engine="python") #extract data from text file
    rng = np.random.default_rng(seed=1) #use for make each randomize output to same , for evaluating the parent selection
    #rng = np.random.default_rng(seed=None) 
    random_index = rng.choice(len(df), replace = True, size = 12)
    temp = df.iloc[random_index]
    for i in range (12): #for 12 times
        cityList.append(City(x=temp.iloc[i,1],y=temp.iloc[i,2])) #assign the selected column to city and add it into city's list
    
    return cityList
def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route
def initialPopulation(popSize, cityList):
    population = []
    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population

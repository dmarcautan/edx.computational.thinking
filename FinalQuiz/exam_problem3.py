import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

MINRABBITPOP = 10
MINFOXPOP = 10

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    global MINRABBITPOP
    
    if CURRENTRABBITPOP < MINRABBITPOP:
        return
    
    for _ in range(CURRENTRABBITPOP):
        growth_chance = 1.0 - CURRENTRABBITPOP / float(MAXRABBITPOP)
        outcome = random.random()
        if growth_chance > outcome:
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    global MINRABBITPOP
    global MINFOXPOP

    for _ in range(CURRENTFOXPOP):
        eat = False
        if CURRENTRABBITPOP > MINRABBITPOP:
            eat = CURRENTRABBITPOP / float(MAXRABBITPOP) > random.random()
            
        if eat:
            CURRENTRABBITPOP -= 1
            if random.random() < 1 / 3.0 and CURRENTFOXPOP < CURRENTRABBITPOP:
                CURRENTFOXPOP += 1
        elif random.random() < 0.1 and CURRENTFOXPOP > MINFOXPOP:
            CURRENTFOXPOP -= 1
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbits = []
    foxes = []
    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    
    return (rabbits, foxes)
    
populationOverTime = runSimulation(200)
rabbitPopulationOverTime = populationOverTime[0]
foxPopulationOverTime = populationOverTime[1]

pylab.figure()
pylab.plot(range(200), rabbitPopulationOverTime, label="rabbits")
pylab.plot(range(200), foxPopulationOverTime, label="foxes")
pylab.legend()

pylab.figure("rabbit polyfit")
coeff = pylab.polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff, range(len(rabbitPopulationOverTime))))

pylab.figure("fox polyfit")
coeff = pylab.polyfit(range(len(foxPopulationOverTime)), foxPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff, range(len(foxPopulationOverTime))))

pylab.show()

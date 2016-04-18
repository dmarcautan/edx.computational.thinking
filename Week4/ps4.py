# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    pylab.figure()
    sim_options = [0, 75, 150, 300]
    for i in range(len(sim_options)):
        pylab.subplot(len(sim_options), 1, i+1)
        simulationDelayedTreatmentPlot(sim_options[i], numTrials)
     
    pylab.show()

def simulationDelayedTreatmentPlot(timesteps_before, numTrials, timesteps_after = 150):
    # Simulation constants
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances =  {'guttagonol': False}
    mutProb =  0.005
    
    timesteps = timesteps_before + timesteps_after
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)] * numViruses
    populations = []
    
    for _ in range(numTrials):
        patient = TreatedPatient(viruses, maxPop)
        for s in range(timesteps):
            if s == timesteps_before:
                patient.addPrescription('guttagonol')
            patient.update()
        populations.append(patient.getTotalPop())
    
    pylab.hist(populations, 20)
      
    pylab.xlabel('Total population after treatment')
    pylab.ylabel('#occurence')
    pylab.title('%d steps before' % timesteps_before)

##simulationDelayedTreatment(100)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    pylab.figure()
    sim_options = [0, 75, 150, 300]
    for i in range(len(sim_options)):
        pylab.subplot(len(sim_options), 1, i+1)
        simulationTwoDrugsDelayedTreatmentPlot(sim_options[i], numTrials)
     
    pylab.show()

def simulationTwoDrugsDelayedTreatmentPlot(timesteps_delay, numTrials, timesteps_startend = 150):
    # Simulation constants
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb =  0.005
    
    timesteps = timesteps_delay + timesteps_startend * 2
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)] * numViruses
    populations = []
    
    for _ in range(numTrials):
        patient = TreatedPatient(viruses, maxPop)
        for s in range(timesteps):
            if s == timesteps_startend:
                patient.addPrescription('guttagonol')
            if s == timesteps_startend + timesteps_delay:
                patient.addPrescription('grimpex')
            patient.update()
        populations.append(patient.getTotalPop())
    
    pylab.hist(populations, 20)
      
    pylab.xlabel('Total population after treatment')
    pylab.ylabel('#occurence')
    pylab.title('%d steps delay' % timesteps_delay)

##simulationTwoDrugsDelayedTreatment(100)
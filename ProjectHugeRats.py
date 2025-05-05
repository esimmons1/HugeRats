# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:32:42 2024

@author: simmo
"""
import time
import random
import statistics

print("initializing")

goal = random_number = random.randint(50000, 75000)                # Target weight in grams
numRats = 20                # Total number of adult rats your lab can support
initialMinWt = 200          # Minimum weight of adult rat, in grams, in initial population
initialMaxWt = 600          # Maximum weight of adult rat, in grams, in initial population
initialModeWt = 300         # Most common adult rat weight, in grams, in initial population
mutateOdds = 0.01           # Probability of a mutation occurring in a rat
mutateMin = 0.5             # Scalar on rat weight of least beneficial mutation
mutateMax = 1.2             # Scalar on rat weight of most beneficial mutation
litterSize = 8              # Number of pups per pair of mating rats
generationLimit = 50000       # Generational cutoff to stop breeding program
littersPerYear = 5          #How many generations per year

print(f"starting program. Goal weight is: {goal}")

if numRats % 2 != 0:
    numRats += 1

def populate(numRats, minWt, maxWt, modeWt):
    "Initialize a population for the distributuion of rats"
    return [int(random.triangular(minWt, maxWt, modeWt)) for i in range(numRats)]

def fitness(population, goal):
    "Measure population fitness based on mean vs. target"
    avg = statistics.mean(population)
    if goal == 0:
        return float('inf')  # To handle division by zero
    return avg / goal

def selection(population, toRetain):
    "Lower the population to a lower number"
    sortedPopulation = sorted(population)
    toRetainBySex = toRetain // 2
    membersPerSex = len(sortedPopulation) // 2
    females = sortedPopulation[:membersPerSex]
    males = sortedPopulation[membersPerSex:]
    selectedFemales = females[-toRetainBySex:]
    selectedMales = males[-toRetainBySex:]
    return selectedMales, selectedFemales

def breed(males, females, litterSize):
    "Breed members randomly across the chosen ones from the selection"
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        if male > female:
            male, female = female, male  # Swap if male weight is greater
        child = random.randint(male, female)
        children.append(child)
    return children


def mutate(children, mutateOdds, mutateMin, mutateMax):
    "Randomly mutate weight of the children"
    for index, rat in enumerate(children):
        if mutateOdds >= random.random():
            children[index] = round(rat * random.uniform(mutateMin, mutateMax))
    return children

def main():
    "Initialize population, select, breed, and mutate, display results."
    generations = 0
    parents = populate(numRats, initialMinWt, initialMaxWt, initialModeWt)
    print("initial population weights = {}".format(parents))
    poplFitness = fitness(parents, goal)
    print("initial population fitness = {}".format(poplFitness))
    print("number to retain = {}".format(numRats))

    aveWt = []

    while poplFitness < 1 and generations < generationLimit:
        selectedMales, selectedFemales = selection(parents, numRats)
        children = breed(selectedMales, selectedFemales, litterSize)
        children = mutate(children, mutateOdds, mutateMin, mutateMax)
        parents = selectedMales + selectedFemales + children
        poplFitness = fitness(parents, goal)
        if generations % 50 == 0:
            print("Generation {} fitness = {:.4f}".format(generations, poplFitness))
        generations += 1
        aveWt.append(int(statistics.mean(parents)))
    print("average weight per generation = {}".format(aveWt))
    print("\nnumber of generations = {}".format(generations))
    print("number of years = {}".format(int(generations / littersPerYear)))
    
    return parents

if __name__ == '__main__':
    startTime = time.time()
    parents = main()
    endTime = time.time()
    duration = endTime - startTime
    print("\nRuntime for this program was {} seconds.".format(duration))

    # Check if the goal weight was reached
    if fitness(parents, goal) >= 1:
        print("The goal weight was reached!")
    else:
        print("The goal weight was not reached.")

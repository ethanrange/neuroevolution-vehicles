from matrixLibrary import Matrix
import random, copy
from car import Car
from NeuralNetwork import NeuralNetwork

from parameters import *



def crossover(MatA, MatB):
    childA = Matrix(MatA.rows,MatA.cols)
    childB = Matrix(MatA.rows,MatA.cols)
    
    childA.matrix = copy.deepcopy(MatB.matrix)
    childB.matrix = copy.deepcopy(MatA.matrix)
    
    colRand = random.randint(0,MatA.cols-2)
    rowRand = random.randint(0,MatA.rows-2)

    for i in range(rowRand+1):
        for j in range(colRand+1):
            childA.matrix[i][j] = MatA.matrix[i][j]
            childB.matrix[i][j] = MatB.matrix[i][j]

    return [childA, childB]

def uniformCrossover(MatA, MatB):
    childA = Matrix(MatA.rows,MatA.cols)
    childB = Matrix(MatA.rows,MatA.cols)
    
    for i in range(MatA.rows):
        for j in range(MatA.cols):
            randomSelection = random.uniform(0,1)
            if randomSelection > 0.5:
                childA.matrix[i][j] = MatA.matrix[i][j]
                childB.matrix[i][j] = MatB.matrix[i][j]
            else:
                childA.matrix[i][j] = MatB.matrix[i][j]
                childB.matrix[i][j] = MatA.matrix[i][j]
                
    return [childA, childB]

def biasCrossover(MatA, MatB):
    childA = Matrix(MatA.rows,1)
    childB = Matrix(MatA.rows,1)
    
    childA.matrix = copy.deepcopy(MatB.matrix)
    childB.matrix = copy.deepcopy(MatA.matrix)
    
    randCut = random.randint(0, MatA.rows-2)
    
    for i in range(randCut+1):
        childA.matrix[i][0] = MatA.matrix[i][0]
        childB.matrix[i][0] = MatB.matrix[i][0]
        
    return [childA, childB]

def createPopulation(oldPop, GenCount):
    print([(i[0].id, i[0].fitness) for i in oldPop])
    oldPopSorted = sorted(copy.deepcopy(oldPop), key=lambda x: int(x[1]))
    
    fitnessSum = 0
    for i in oldPop:
        #i[1] += 1
        fitnessSum += i[1]
        
    if fitnessSum == 0:
        fitnessSum += POP_SIZE
        
        for i in oldPop:
            i[1] += 1
    
        
    for j in oldPop:
        j[1] = float(j[1]) / float(fitnessSum)
    
    newPop = []
    
    for i in range(1,SAVED_CARS+1):
        #print(oldPopSorted[-i][0].id)
        
        new_nn = NeuralNetwork(oldPopSorted[-i][0].nn.input_nodes, oldPopSorted[-i][0].nn.hidden_nodes_l1, oldPopSorted[-i][0].nn.hidden_nodes_l2, oldPopSorted[-i][0].nn.output_nodes)
        new_nn.IH1_Weights = copy.deepcopy(oldPopSorted[-i][0].nn.IH1_Weights)
        new_nn.H1H2_Weights = copy.deepcopy(oldPopSorted[-i][0].nn.H1H2_Weights)
        new_nn.H2O_Weights = copy.deepcopy(oldPopSorted[-i][0].nn.H2O_Weights)
        
        new_nn.H1_Bias = copy.deepcopy(oldPopSorted[-i][0].nn.H1_Bias)
        new_nn.H2_Bias = copy.deepcopy(oldPopSorted[-i][0].nn.H2_Bias)
        new_nn.O_Bias = copy.deepcopy(oldPopSorted[-i][0].nn.O_Bias)
        
        newCar = Car(initpos.x, initpos.y, True, [255,0,0], new_nn)
        newCar.id = oldPopSorted[-i][0].id
        
        newPop.append(newCar)
        
    #newPop[0].nn.saveNN()
        
    #if oldPopSorted[-1][0].id == 'UNDEFINED':
    #    newPop[0].id = 'TOP2: GEN {}'.format(GenCount)
    #else:
    #    newPop[0].id = oldPopSorted[-1][0].id
        
    #if oldPopSorted[-2][0].id == 'UNDEFINED':
    #    newPop[1].id = 'TOP2: GEN {}'.format(GenCount)
    #else:
    #    newPop[1].id = oldPopSorted[-2][0].id
    
    while len(newPop) < POP_SIZE: # POP SIZE
        parentA = selectMember(oldPop)
        parentB = selectMember(oldPop)
        
        if parentA != parentB:
            children_IH1 = crossover(parentA[0].nn.IH1_Weights, parentB[0].nn.IH1_Weights)
            children_H1H2 = crossover(parentA[0].nn.H1H2_Weights, parentB[0].nn.H1H2_Weights)
            children_H2O = crossover(parentA[0].nn.H2O_Weights, parentB[0].nn.H2O_Weights)

            children_H1B = biasCrossover(parentA[0].nn.H1_Bias, parentB[0].nn.H1_Bias)
            children_H2B = biasCrossover(parentA[0].nn.H2_Bias, parentB[0].nn.H2_Bias)
            children_OB = biasCrossover(parentA[0].nn.O_Bias, parentB[0].nn.O_Bias)
            
            children_nn = []
            for i in range(2):
                new_nn = NeuralNetwork(parentA[0].nn.input_nodes, parentA[0].nn.hidden_nodes_l1, parentA[0].nn.hidden_nodes_l2, parentA[0].nn.output_nodes)
                new_nn.IH1_Weights = children_IH1[i]
                new_nn.H1H2_Weights = children_H1H2[i]
                new_nn.H2O_Weights = children_H2O[i]
                
                new_nn.H1_Bias = children_H1B[i]
                new_nn.H2_Bias = children_H2B[i]
                new_nn.O_Bias = children_OB[i]
                
                new_nn.IH1_Weights = new_nn.IH1_Weights.mutate(MUTATION_RATE)
                new_nn.H1H2_Weights = new_nn.H1H2_Weights.mutate(MUTATION_RATE)
                new_nn.H2O_Weights = new_nn.H2O_Weights.mutate(MUTATION_RATE)
                
                #new_nn.H1_Bias.mutate(MUTATION_RATE)
                #new_nn.H2_Bias.mutate(MUTATION_RATE)
                #new_nn.O_Bias.mutate(MUTATION_RATE)
                
                children_nn.append(new_nn)
            
            randomSelection = random.uniform(0,1)
            if randomSelection < 0.5:
                newPop.append(Car(initpos.x, initpos.y, True, [255,0,0], children_nn[0]))
            else:
                newPop.append(Car(initpos.x, initpos.y, True, [255,0,0], children_nn[1]))
            
    for i in range(SAVED_CARS, len(newPop)):
        if newPop[i].id == 'UNDEFINED':
            newPop[i].id = '{}:{}'.format(GenCount+1, i+1-SAVED_CARS)
            
    return newPop
    
def selectMember(inputList):
    index = 0
    cumulative = random.uniform(0, 1)

    while cumulative > 0:
        cumulative -= inputList[index][1]
        index += 1
        
    return inputList[index-1]

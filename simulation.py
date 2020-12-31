from walls import *
from parameters import *
from car import Car, CarSensor, carPanel
from GeneticAlgorithm import createPopulation
from NeuralNetwork import NeuralNetwork

import visualisation as vc
import time as t

import json

class Simulation():
    def __init__(self):
        self.GenerationCount = 0
        self.population = []
        self.populationResults = []
        
        self.currentCar = self.bestCar = None
        self.currentCarNum = self.bestCarNum = 0

        self.NodeList = []
        self.WeightList = []

        self.walls = []
        self.checkpoints = []
        self.endLine = None

        self.steeringAmount = 0
        self.acceleratingForce = 0
        
        self.loadedFile = None
        self.currentTrack = 1
        
    def initialisePopulation(self):
        self.population = []
        self.populationResults = []
        
        for i in range(POP_SIZE):
            newCar = Car(initpos.x, initpos.y, False, [255,0,0])
            self.population.append(newCar)
            self.population[i].id = '1:{}'.format(i+1)
            self.populationResults.append([newCar, 0])
            
    def initialiseSingle(self, network):
        self.population = []
        self.populationResults = []
        
        newCar = Car(initpos.x, initpos.y, True, [255,0,0], network)
        newCar.id = '1:1'
        self.population.append(newCar)
        self.populationResults.append([newCar, 0])
        
    def initialiseValues(self):
        self.currentCar = self.bestCar = self.population[0]
        self.currentCarNum = self.bestCarNum = 0
        
        self.visualiseNetwork()
        
        self.steeringAmount = 0
        self.acceleratingForce = 0
        
    def genLevel(self):
        self.walls = []
        self.checkpoints = []
        self.endLine = None
        
        coordinates = CoordinatesData()
        
        if self.currentTrack == 1:
            for i in coordinates.walls:
                self.walls.append(wall(i[0], i[1]))
                
            for j in coordinates.checkpoints:
                self.checkpoints.append(checkpoint(j[0], j[1], j[2]))
        else:
            for i in coordinates.walls2:
                self.walls.append(wall(i[0], i[1]))
                
            for j in coordinates.checkpoints2:
                self.checkpoints.append(checkpoint(j[0], j[1], j[2]))
            
        self.endLine = finishLine(coordinates.finishLines[self.currentTrack-1][0], coordinates.finishLines[self.currentTrack-1][1])
        
    def visualiseNetwork(self):
        self.NodeList, self.WeightList = vc.visualise(self.currentCar.nn, NN_TOPOLOGY, NODE_DIAMETER, VIS_OFFSET[0], VIS_OFFSET[1])
        
    def drawNetwork(self):
        strokeWeight(5)
        stroke(0)
        fill(230)
        
        rect(1250, height/2, 470, height-30)
        
        fill(250)
        rect(1250, VIS_OFFSET[1]+VIS_DIM[1]/2, VIS_DIM[0], VIS_DIM[1])
        
        push()
        fill(0)
        textSize(30)
        textAlign(CENTER)
        text('Current Car:', 1250, 65)
        pop()
        
        push()
        textSize(25)
        fill(0)
        
        carNumText = 'Current car number: ' + str(self.currentCarNum+1)
        text(carNumText, 1070, 510)
        
        idText = 'Current car ID: ' + str(self.currentCar.id)
        text(idText, 1070, 550)
        
        line(1015, 580, 1485, 580)
        
        posText = 'Car Position: (' + str(int(self.currentCar.pos.x)) + ', ' + str(int(self.currentCar.pos.y)) + ')'
        text(posText, 1070, 630)
        
        scoreText = 'Car Score: ' + str(self.currentCar.score)
        text(scoreText, 1070, 670)
        
        fitnessText = 'Car Fitness: ' + str(self.currentCar.fitness)
        text(fitnessText, 1070, 710)
        
        timeText = 'Time: ' + str(round(self.currentCar.time, 4))
        text(timeText, 1070, 750)
        
        line(1015, 780, 1485, 780)
        
        pop()
            
        for weight in self.WeightList:
            weight.show()
                    
        for layer in self.NodeList:
            for node in layer:
                node.show()
                
    def drawGenerationInfo(self):
        push()
        
        rectMode(CORNER)
        strokeWeight(5)
        stroke(0)
        fill(230)
        
        rect(22, 935, 970, 50)
        pop()
        
        push()
        textSize(25)
        fill(0,0,0,255)
        
        GenText = 'Generation number: ' + str(self.GenerationCount+1)
        text(GenText, 35, 970)
        
        bestFitnessText = 'Best fitness: ' + str(self.bestCar.fitness) + ' (' + str(self.bestCar.id) + ')'
        text(bestFitnessText, 340, 970)
        pop()
        
        self.drawProgressBar()
        
    def drawSingleInfo(self):
        push()
        
        rectMode(CORNER)
        strokeWeight(5)
        stroke(0)
        fill(230)
        
        rect(22, 935, 970, 50)
        pop()
        
        push()
        textSize(25)
        fill(0,0,0,255)
        
        GenText = 'Single Car Mode: ({})'.format(self.currentCar.id)
        text(GenText, 35, 970)
        
        loadedFileText = 'Loaded Network: {}'.format(self.loadedFile)
        text(loadedFileText, 340, 970)
        
        bestFitnessText = ''
        text(bestFitnessText, 340, 970)
        pop()
        
    def setStartTime(self):
        self.currentCar.startTime = t.time()
        
    def drawText(self):
        push()
        textSize(25)
        fill(255)
        text(str(int(round(frameRate))), 5, 25)
        pop()
        textSize(12)
        
    def drawProgressBar(self):
        push()
        textSize(25)
        fill(0,255)
        progressText = 'Progress: '
        text(progressText, 640, 970)
        
        fill(0,0)
        stroke(0,255)
        rectMode(CORNER)
        rect(770, 948, 200, 25)
        
        fill(0,255)
        barWidth = (200.0 / POP_SIZE) * (self.currentCarNum+1)
        rect(770, 948, barWidth, 25)
        pop()
        
    def createNewPopulation(self):
        print('=================================================')
        print('Generation {} complete. Max Fitness: {}').format(self.GenerationCount+1, self.bestCar.fitness)
        
        fitnessArray = [i[1] for i in self.populationResults]
        print('Average fitness: {}').format(sum(fitnessArray)/float(POP_SIZE))
        print(fitnessArray)
        
        self.GenerationCount += 1
        newPop = createPopulation(self.populationResults, self.GenerationCount)
        self.population = []
        self.populationResults = []
        for i in newPop:
            self.population.append(i)
            self.populationResults.append([i,0])
            
        print([self.population[i].id for i in range(POP_SIZE)])
        print('=================================================\n')
        
    def loadNN(self, path):
        with open(path, 'r') as file:
            extractData = json.load(file)
        
            dimensions = [extractData['input_nodes'], extractData['hidden_nodes_l1'],
            extractData['hidden_nodes_l2'], extractData['output_nodes']]
        
            loadedNetwork = NeuralNetwork(*dimensions)
        
            loadedNetwork.IH1_Weights.matrix = extractData['IH1_Weights']['matrix']
            loadedNetwork.H1H2_Weights.matrix = extractData['H1H2_Weights']['matrix']
            loadedNetwork.H2O_Weights.matrix = extractData['H2O_Weights']['matrix']
                
            loadedNetwork.H1_Bias.matrix = extractData['H1_Bias']['matrix']
            loadedNetwork.H2_Bias.matrix = extractData['H2_Bias']['matrix']
            loadedNetwork.O_Bias.matrix = extractData['O_Bias']['matrix']
        
            return loadedNetwork
            

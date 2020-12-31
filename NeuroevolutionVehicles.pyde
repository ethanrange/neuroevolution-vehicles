import time as t
from button import *

from parameters import *
from simulation import Simulation

import os

def setup():
    size(1500, 1000)
    rectMode(CENTER)
    frameRate(60)
    
    global bg
    bg = loadImage("background.jpg")
    background(bg)
    
sim = Simulation()
sim.genLevel()

sim.initialisePopulation()
sim.initialiseValues()

sim.setStartTime()

btns = [button(1035, 800, 130, 165, 'Load', 35, 70, 'load'),
       button(1185, 800, 130, 165, 'Save', 40, 70, 'save'),
       button(1335, 800, 130, 165, 'Run', 42, 70, 'run'),
       button(872, 15, 120, 50, 'Track: 1', 10, 35, 'swtr')]

singleCarMode = False

def draw():
    background(bg) #200
    
    replaceCar = False

    sim.drawText()
    
    force = PVector(0, -sim.acceleratingForce)
    sim.currentCar.applyForce(force.rotate(sim.currentCar.angle))
    sim.currentCar.angle += sim.steeringAmount
    
    sim.currentCar.move()
    sim.currentCar.show()
    
    sim.currentCar.time = t.time() - sim.currentCar.startTime
    
    for panel in sim.currentCar.panels:
        panel.setParams(sim.currentCar.angle, sim.currentCar.pos)
        panel.show()
    
    for j in sim.currentCar.sensors:
        j.setParams(sim.currentCar.angle, sim.currentCar.pos)
        j.show()
            
    #for checkpoint in sim.checkpoints:
    #    checkpoint.show()
        
    sim.endLine.show()
    
    for wall in sim.walls:
        wall.show()
    
    sim.drawNetwork()
    if not singleCarMode:
        sim.drawGenerationInfo()
    else:
        sim.drawSingleInfo()
    
    for btn in btns:
        btn.show()
    
    stroke(0)
    strokeWeight(2)
    
    intersects = []
    sensorReadings = []
    
    for k in sim.currentCar.sensors:
        intersects = []
        
        for wall in sim.walls:
            intersect = k.sense(wall)
            if intersect:
                intersects.append(intersect)
        
        if intersects:
            shortestDistance = float('inf')
            shortestLine = PVector(0,0)
            
            carLoc = PVector(sim.currentCar.pos.x-sim.currentCar.w/2, sim.currentCar.pos.y-sim.currentCar.h/2)
            
            for i in intersects:
                if carLoc.dist(i) < shortestDistance:
                    shortestDistance = carLoc.dist(i)
                    shortestLine = i.copy()
                    
            strokeWeight(1)
            stroke(0, 0, 0, 100)
            line(sim.currentCar.pos.x-sim.currentCar.w/2, sim.currentCar.pos.y-sim.currentCar.h/2, shortestLine.x, shortestLine.y)
            fill(255, 0, 0)
            ellipse(shortestLine.x, shortestLine.y, 8, 8)
            
            distance = int(sim.currentCar.pos.dist(shortestLine))
            sensorReadings.append([sim.currentCar.pos.dist(shortestLine)/500])
            fill(0)
            text(str(distance), shortestLine.x+5, shortestLine.y+5)
    
    decMat = sim.currentCar.nn.feedforward(sensorReadings)
    
    turnValue = decMat.matrix[0][0]
    
    if turnValue <= (1.0/3):
        sim.steeringAmount = STEER_STRENGTH #Right
    elif turnValue >= (2.0/3):
        sim.steeringAmount = -STEER_STRENGTH #Left
    else:
        sim.steeringAmount = 0.00 # Straight
    
    sim.acceleratingForce = decMat.matrix[1][0] * ACC_FORCE
        
    if sim.currentCar.time > (TIME_LIMIT + sim.currentCar.score):
        replaceCar = True
    
    for i in sim.currentCar.panels:
        for wall in sim.walls:
            bodyInt = i.sense(wall)
            if bodyInt:
                replaceCar = True
                break
                    
    for i in sim.currentCar.panels:
        for checkpoint in sim.checkpoints:
            bodyInt = i.sense(checkpoint)
            if bodyInt:
                if checkpoint.id not in sim.currentCar.completedCheckpoints:
                    sim.currentCar.score += 1
                    sim.currentCar.fitness = (sim.currentCar.score)**2
                    sim.currentCar.completedCheckpoints.append(checkpoint.id)
        
    for i in sim.currentCar.panels:
        bodyInt = i.sense(sim.endLine)
        allCheckpoints = True if sim.currentCar.score == len(sim.checkpoints) else False
        if bodyInt:
            if allCheckpoints:
                timeFitness = 40000 / (sim.currentCar.time + 40)
                sim.currentCar.fitness += int(timeFitness)
                print('Success! Fitness: {} Time: {}'.format(sim.currentCar.fitness, sim.currentCar.time))
                replaceCar = True
                break
            else:
                replaceCar = True
                break
            
    if replaceCar:
        if sim.currentCar.fitness > sim.bestCar.fitness:
            sim.bestCar = sim.currentCar
            sim.bestCarNum = sim.currentCarNum
            
        sim.populationResults[sim.currentCarNum][1] = sim.currentCar.fitness
        
        if not singleCarMode:
            if sim.currentCarNum == POP_SIZE-1:
                sim.createNewPopulation()
                    
                sim.initialiseValues()
                sim.setStartTime()
            else:
                sim.currentCarNum += 1
                sim.currentCar = sim.population[sim.currentCarNum]
                
                sim.visualiseNetwork()
                
                sim.steeringAmount = 0.00
                sim.acceleratingForce = 0.00
                
                sim.setStartTime()
        else:
            currentNetwork = sim.currentCar.nn
            sim.initialiseSingle(currentNetwork)
            sim.initialiseValues()
            
            sim.setStartTime()
            
def keyPressed():
    if key == 'p':
        noLoop()
    elif key == 'r':
        loop()
        
def mousePressed():
    global singleCarMode
    
    for btn in btns:
        action = btn.handleEvent(mouseX, mouseY)
        if action == 'run':
            singleCarMode = False
            sim.GenerationCount = 0
            sim.initialisePopulation()
            sim.initialiseValues()
            sim.setStartTime()
        elif action == 'save':
            sim.currentCar.nn.saveNN(sim.GenerationCount+1, sim.currentCarNum+1)
        elif action == 'load':
            selectInput('Select a network to load', 'fileSelectHandle', this.dataFile(''))
        elif action == 'swtr':
            sim.currentTrack = 2 if sim.currentTrack == 1 else 1
            btn.text = 'Track: {}'.format(sim.currentTrack)
            sim.genLevel()
            
            if singleCarMode:
                currentNetwork = sim.currentCar.nn
                sim.initialiseSingle(currentNetwork)
            else:
                sim.initialisePopulation()
                sim.GenerationCount = 0
                
            sim.initialiseValues()
            sim.setStartTime()
                
        elif action:
            print(action)
            
def fileSelectHandle(selectedFile):
    global singleCarMode
    
    if selectedFile:
        extension = str(selectedFile).split('.')[-1]
        fileName = str(selectedFile.getName()).replace('.'+extension, '')
        
        if extension == 'json':
            loadedNetwork = sim.loadNN(selectedFile.getAbsolutePath())
            sim.loadedFile = fileName
            
            sim.initialiseSingle(loadedNetwork)
            sim.initialiseValues()
            sim.setStartTime()
            singleCarMode = True
        else:
            print('Please select a JSON File.')

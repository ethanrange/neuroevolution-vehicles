from NeuralNetwork import NeuralNetwork
from parameters import *

def lineAtAngle(x, y, angle, lineLength):
    line(x, y, x+sin(angle)*lineLength, y-cos(angle)*lineLength)



class Car():
    
    def __init__(self, x, y, nnDef, col=[255,0,0], nn=None):
        self.pos = PVector(x,y)
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
        
        self.velMax = MAX_VEL
        
        self.w = 20
        self.h = 30
        
        self.angle = radians(100)
        
        self.sensors = []
        sensor_spacing = PI / (SENSOR_NUM-1)

        for i in range(SENSOR_NUM):
            self.sensors.append(CarSensor(self.angle, i*sensor_spacing-PI/2, self.pos, self.w, self.h))
        
        self.panels = []
        
        carLeft = carPanel(PVector(-self.w/2, -self.h/2), PVector(-self.w/2, self.h/2), self.pos, self.w, self.h, self.angle)
        carRight = carPanel(PVector(self.w/2, self.h/2), PVector(self.w/2, -self.h/2), self.pos, self.w, self.h, self.angle)
        carTop = carPanel(PVector(-self.w/2, -self.h/2), PVector(self.w/2, -self.h/2), self.pos, self.w, self.h, self.angle)
        carBottom = carPanel(PVector(self.w/2, self.h/2), PVector(-self.w/2, self.h/2), self.pos, self.w, self.h, self.angle)

        self.panels = [carLeft, carRight, carTop, carBottom]
        
        self.col = col
        
        self.score = 0
        self.completedCheckpoints = []
        
        self.startTime = 0
        self.time = 0
        
        self.fitness = 0
        #self.bestFitness = 0 #Should be redundant
        
        if nnDef:
            self.nn = nn
        else:
            self.nn = NeuralNetwork(NN_TOPOLOGY[0], NN_TOPOLOGY[1], NN_TOPOLOGY[2], NN_TOPOLOGY[3])
            
        self.id = 'UNDEFINED'
        
    def show(self):
        
        stroke(0)
        smooth()
        strokeWeight(1)
        
        pushMatrix()
        translate(self.pos.x-self.w/2, self.pos.y-self.h/2)
        rotate(self.angle)
        popMatrix()
        
        strokeWeight(1)
        fill(255)
        lineAtAngle(self.pos.x-self.w/2, self.pos.y-self.h/2, self.angle, self.h/2+5)
        
    def move(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        
        self.acc.mult(0)
        
        self.vel.limit(self.velMax)
        
        drag = self.vel.copy()
        drag.mult(-0.05)
        
        self.applyForce(drag)
        
    def applyForce(self, force):
        self.acc.add(force)
        
class CarSensor():
    
    def __init__(self, angle, offset, pos, w, h):
        self.pos = PVector(pos.x-w/2, pos.y-h/2)
        self.length = 100
        
        self.offset = offset
        self.direction = PVector.fromAngle(angle-PI/2-self.offset)
        
        self.w = w
        self.h = h
        
    def setParams(self, angle, pos):
        self.direction = PVector.fromAngle(angle-PI/2-self.offset)
        self.direction.normalize()
        
        self.pos.x = pos.x - self.w/2
        self.pos.y = pos.y - self.h/2
        
    def show(self):
        stroke(0)
        strokeWeight(1)
        pushMatrix()
        translate(self.pos.x-self.w/2, self.pos.y-self.h/2)
        #line(0, 0, self.direction.x*self.length, self.direction.y*self.length)
        popMatrix()
        
    def sense(self, wall):
        x1 = wall.start.x
        y1 = wall.start.y
        x2 = wall.end.x
        y2 = wall.end.y
        
        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.direction.x
        y4 = self.pos.y + self.direction.y
        
        denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        if denom == 0:
            return

        t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / denom
        u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / denom
        
        if t > 0 and t < 1 and u > 0:
            xPos = x3 + u*(x4-x3)
            yPos = y3 + u*(y4-y3)
            return PVector(xPos, yPos)
        
class carPanel():
    
    def __init__(self, start, end, pos, w, h, angle):
        self.start = start
        self.end = end
        
        self.startFixed = start
        self.endFixed = end
        
        self.pos = pos
        self.w = w
        self.h = h
        self.angle = angle
        
        self.centre = PVector(self.pos.x-self.w/2, self.pos.y-self.h/2)
        
    def show(self):
        stroke(0)
        strokeWeight(1)
        
        pushMatrix()
        self.centre = PVector(self.pos.x-self.w/2, self.pos.y-self.h/2)
        translate(self.centre.x, self.centre.y)
        line(self.start.x, self.start.y, self.end.x, self.end.y)
        popMatrix()
        
    def setParams(self, angle, pos):
        self.angle = angle
        self.pos = pos
        
    def sense(self, wall):
        x1 = wall.start.x
        y1 = wall.start.y
        x2 = wall.end.x
        y2 = wall.end.y
        
        self.start = self.startFixed.copy()
        self.end = self.endFixed.copy()
        
        pushMatrix()
        translate(self.centre.x, self.centre.y)
        self.start.rotate(self.angle)
        self.end.rotate(self.angle)
        popMatrix()
        
        #self.centre = PVector(carObj.pos.x-carObj.w/2, carObj.pos.y-carObj.h/2)
        
        x3 = self.centre.x + self.start.x
        y3 = self.centre.y + self.start.y
        x4 = self.centre.x + self.end.x
        y4 = self.centre.y + self.end.y
        
        denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        if denom == 0:
            return

        t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / denom
        u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / denom
        
        if t > 0 and t < 1 and u > 0 and u < 1:
            xPos = x3 + u*(x4-x3)
            yPos = y3 + u*(y4-y3)
            return PVector(xPos, yPos)

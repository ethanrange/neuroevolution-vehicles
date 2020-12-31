import random, math, copy
from parameters import *

class Matrix():
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def applyFunc(self, function):
        result = Matrix(self.rows, self.cols)
        
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = function(self.matrix[i][j])
        
        return result

    def addCon(self, constant):
        func = lambda x: x+constant
        result = Matrix.applyFunc(self, func)
        return result

    def addMat(self, matrix):
        result = Matrix(self.rows, self.cols)
        
        if self.rows == matrix.rows and self.cols == matrix.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    result.matrix[i][j] = self.matrix[i][j] + matrix.matrix[i][j]

        return result

    def multMat(self, matrix):
        result = Matrix(self.rows, matrix.cols)
        
        if self.cols == matrix.rows:
            for i in range(self.rows):
                for j in range(matrix.cols):
                    total = 0
                    for k in range(self.cols):
                        total += self.matrix[i][k]*matrix.matrix[k][j]
                    result.matrix[i][j] = total

            return result

        else:
            print('dimension error')

    def randFill(self):
        func = lambda _: 2*random.uniform(0,1)-1
        self.matrix = Matrix.applyFunc(self, func).matrix
        
    def fillOnes(self):
        func = lambda _: 1
        self.matrix = Matrix.applyFunc(self, func).matrix
        
    def fromArray(self, arrayInput):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = arrayInput[i][j]

    def sigmoid(self):
        sigmoidFunc = lambda x: 1 / (1+(math.e**-x))
        result = Matrix.applyFunc(self, sigmoidFunc)
        return result
    
    def leakyReLu(self):
        ReLuFunc = lambda x: x if x >= 0 else x/20.0
        result = Matrix.applyFunc(self, ReLuFunc)
        return result
    
    def mutate(self, rate):
        result = Matrix(self.rows, self.cols)
        result.matrix = copy.deepcopy(self.matrix)

        for i in range(self.rows):
            for j in range(self.cols):
                randomVal = random.uniform(0,1)
                if randomVal < rate:
                    #delta = result.matrix[i][j] * (random.uniform(0,1) - 0.5) * 3 + (random.uniform(0,1) - 0.5)
                    #print(result.matrix[i][j], '|', (result.matrix[i][j]+delta))
                    delta = MUTATION_CONSTANT * random.gauss(0,1)
                    #print(delta, result.matrix[i][j] * (random.uniform(0,1) - 0.5) * 3 + (random.uniform(0,1) - 0.5))
                    result.matrix[i][j] += delta

        return result

#newMatrix = Matrix(2,3)
#newMatrix2 = Matrix(3,2)

#newMatrix.matrix = [[2, 4, 5], [6, 1, 2]]
#newMatrix2.matrix = [[1, 2], [3, 4],[ 5, 6]]

#print(newMatrix.matrix)
#newMatrix.randFill()
#print(newMatrix.matrix)

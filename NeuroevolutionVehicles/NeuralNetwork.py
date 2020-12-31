from matrixLibrary import *
import math, json, time, datetime

class NeuralNetwork():

    def __init__(self, input_nodes, hidden_nodes_l1, hidden_nodes_l2, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes_l1 = hidden_nodes_l1
        self.hidden_nodes_l2 = hidden_nodes_l2
        self.output_nodes = output_nodes
        
        self.IH1_Weights = Matrix(self.hidden_nodes_l1, self.input_nodes)
        self.IH1_Weights.randFill()
        
        self.H1H2_Weights = Matrix(self.hidden_nodes_l2, self.hidden_nodes_l1)
        self.H1H2_Weights.randFill()
        
        self.H2O_Weights = Matrix(self.output_nodes, self.hidden_nodes_l2)
        self.H2O_Weights.randFill()
        
        self.H1_Bias = Matrix(self.hidden_nodes_l1, 1)
        #self.H1_Bias.randFill()
        self.H1_Bias.fillOnes()
        
        self.H2_Bias = Matrix(self.hidden_nodes_l2, 1)
        #self.H2_Bias.randFill()
        self.H2_Bias.fillOnes()
        
        self.O_Bias = Matrix(self.output_nodes, 1)
        #self.O_Bias.randFill()
        self.O_Bias.fillOnes()

    def feedforward(self, inputValues):
        inputs = Matrix(self.input_nodes, 1)
        inputs.fromArray(inputValues)

        hiddenValues_l1 = Matrix(self.hidden_nodes_l1, 1)
        hiddenValues_l1 = self.IH1_Weights.multMat(inputs)
        hiddenValues_l1 = hiddenValues_l1.addMat(self.H1_Bias)
        hiddenValues_l1 = hiddenValues_l1.leakyReLu()
        
        hiddenValues_l2 = Matrix(self.hidden_nodes_l2, 1)
        hiddenValues_l2 = self.H1H2_Weights.multMat(hiddenValues_l1)
        hiddenValues_l2 = hiddenValues_l2.addMat(self.H2_Bias)
        hiddenValues_l2 = hiddenValues_l2.leakyReLu()

        outputValues = Matrix(self.output_nodes, 1)
        outputValues = self.H2O_Weights.multMat(hiddenValues_l2)
        outputValues = outputValues.addMat(self.O_Bias)
        outputValues = outputValues.sigmoid()
        
        return outputValues
    
    def saveNN(self, gen, num):
        defaultMethod = lambda o: o.__dict__
        data = json.loads(json.dumps(self, default = defaultMethod, indent=4))
        fileName = "G{}N{}_{}_{}.json".format(gen, num, datetime.date.today(), int(time.time()))
        print('Saved current network to /SavedNetworks/{}'.format(fileName))
        with open("SavedNetworks/{}".format(fileName), 'w') as file:
            json.dump(data, file, indent=4)
    

    
    
    

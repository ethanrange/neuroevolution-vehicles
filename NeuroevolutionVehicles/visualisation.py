class Node():
    
    def __init__(self, x, y, NodeDiameter):
        self.x = x
        self.y = y
        self.diameter = NodeDiameter
        
    def show(self):
        fill(150,150,150,255)
        stroke(150,150,150,255)
        strokeWeight(1)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
class Weight():
    
    def __init__(self, x1, y1, x2, y2, col, opacity):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.colConfig = col + [opacity]
        
    def show(self):
        strokeWeight(2)
        stroke(*self.colConfig)
        line(self.x1, self.y1, self.x2, self.y2)

def visualise(NeuralNetwork, NN_TOPOLOGY, NodeDiameter, xOffset, yOffset):
    Weights = [NeuralNetwork.IH1_Weights, NeuralNetwork.H1H2_Weights, NeuralNetwork.H2O_Weights]
    NodeList = []
    WeightList = []
    maxNodes = max(NN_TOPOLOGY)
        
    for i in range(len(NN_TOPOLOGY)):
        nodes = NN_TOPOLOGY[i]
        extraPad = ((2*maxNodes+1)*NodeDiameter - ((2*nodes+1)*NodeDiameter))/2
        layer = []
        
        for j in range(NN_TOPOLOGY[i]):
            xPos = (2*NodeDiameter) + i*(4*NodeDiameter) + xOffset
            yPos = (1.5 * NodeDiameter) + j*(NodeDiameter*2) + extraPad + yOffset
            layer.append(Node(xPos, yPos, NodeDiameter))
            
        NodeList.append(layer)
        
    for i in range(len(NodeList)-1):
        for j in range(len(NodeList[i])):
            for k in range(len(NodeList[i+1])):
                WeightMatrix = Weights[i].matrix
                opacity = abs(WeightMatrix[k][j]) * 255
                if WeightMatrix[k][j] > 0:
                    WeightList.append(Weight(NodeList[i][j].x, NodeList[i][j].y, NodeList[i+1][k].x, NodeList[i+1][k].y, [0,0,255], opacity))
                elif WeightMatrix[k][j] < 0:
                    WeightList.append(Weight(NodeList[i][j].x, NodeList[i][j].y, NodeList[i+1][k].x, NodeList[i+1][k].y, [255,0,0], opacity))
                else:
                    WeightList.append(Weight(NodeList[i][j].x, NodeList[i][j].y, NodeList[i+1][k].x, NodeList[i+1][k].y, [0,0,0], opacity))
    
    return NodeList, WeightList

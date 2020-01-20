import math
import random
 
def createMatrix(numRows, numCols):
    
		matrix = []
    
		for i in range(numRows):
			matrix.append([0]*numCols)
    
		return matrix 
		
def activationFunction(x):
	return 1 / (1 + math.exp(-x))
 
def dActivationFunction(y):
	return y*(1-y)
	
def rand(min, max):
	return min + (max-min)*random.random()
 
class NeuralNetwork:
    
	def __init__(self, numInputNeurons, numHiddenNeurons, numOutputNeurons):
    
		self.numInputNeurons = numInputNeurons + 1 
		self.numHiddenNeurons = numHiddenNeurons + 1
		self.numOutputNeurons = numOutputNeurons
         
		self.inputActivations = [1.0]*self.numInputNeurons
		self.hiddenActivations = [1.0]*self.numHiddenNeurons
		self.outputActivations = [1.0]*self.numOutputNeurons
       
		self.inputWeights = createMatrix(self.numInputNeurons, self.numHiddenNeurons)
		self.outputWeights = createMatrix(self.numHiddenNeurons, self.numOutputNeurons)
        
		for i in range(self.numInputNeurons):
			for j in range(self.numHiddenNeurons):
				self.inputWeights[i][j] = rand(-0.2, 0.2)

		for j in range(self.numHiddenNeurons):
			for k in range(self.numOutputNeurons):
				self.outputWeights[j][k] = rand(-0.2, 0.2)
     
        # last change in weights for momentum
		self.momentumInputChange = createMatrix(self.numInputNeurons, self.numHiddenNeurons)
		self.momentumOutputChange = createMatrix(self.numHiddenNeurons, self.numOutputNeurons)
     
		self.inputActivations[self.numInputNeurons-1] = 1
		self.hiddenActivations[self.numHiddenNeurons-1] = 1     
	
	def feedforward(self, inputs):
   
        #input layer
		for i in range(self.numInputNeurons-1):
			self.inputActivations[i] = inputs[i]
              
        #hidden layer
		for j in range(self.numHiddenNeurons):
			sum = 0.0
			for i in range(self.numInputNeurons):
				sum = sum + self.inputActivations[i] * self.inputWeights[i][j]
				self.hiddenActivations[j] = activationFunction(sum)
         
        #output layer
		for k in range(self.numOutputNeurons):
			sum = 0.0
			for j in range(self.numHiddenNeurons):
				sum = sum + self.hiddenActivations[j] * self.outputWeights[j][k]
				self.outputActivations[k] = activationFunction(sum)
         
		return self.outputActivations[:]
     
     
	def backPropagation(self, targets, learningRate, momentum):
    
		output_deltas = [0.0] * self.numOutputNeurons

		for k in range(self.numOutputNeurons):
			error = targets[k] - self.outputActivations[k]
			output_deltas[k] = error * dActivationFunction(self.outputActivations[k]) 
     
        #hidden layer error
		hidden_deltas = [0.0] * self.numHiddenNeurons
		for j in range(self.numHiddenNeurons):
			error = 0.0
			for k in range(self.numOutputNeurons):
				error = error + output_deltas[k]*self.outputWeights[j][k]
				hidden_deltas[j] = dActivationFunction(self.hiddenActivations[j]) * error
     
        #update output weights
		for j in range(self.numHiddenNeurons):
			for k in range(self.numOutputNeurons):
				change = output_deltas[k]*self.hiddenActivations[j]
				self.outputWeights[j][k] = self.outputWeights[j][k] + learningRate*change + momentum*self.momentumOutputChange[j][k]
				self.momentumOutputChange[j][k] = change
     
        #update input weights
		for i in range(self.numInputNeurons):
			for j in range(self.numHiddenNeurons):
				change = hidden_deltas[j]*self.inputActivations[i]
				self.inputWeights[i][j] = self.inputWeights[i][j] + learningRate*change + momentum*self.momentumInputChange[i][j]
				self.momentumInputChange[i][j] = change
     
    # calculate error
	def calculateError(self, targets):
		error = 0.0
		for k in range(len(targets)):
			error = error + (targets[k] - self.outputActivations[0])**2
        
		return error / len(targets)
     
	def testNetwork(self, patterns):
		for pattern in patterns:
			print('Input is: ',pattern[0],' and output is: ',self.feedforward(pattern[0]))
     
	def trainNetwork(self, patterns, learningRate=0.1, momentum=0.45):
        
		error = 100
		iterations = 0
   
		while iterations < 10000:
            
			iterations = iterations + 1

			for pattern in patterns:
				inputs = pattern[0]
				targets = pattern[1]
				self.feedforward(inputs)
				self.backPropagation(targets, learningRate, momentum)
				error = self.calculateError(targets)
                
				if iterations % 1000 == 0:
					print('Actual error is: %-.5f' % error)
      
 
if __name__ == '__main__':
    
	trainingData = [
		[[0,0], [0]],
		[[0,1], [0]],
		[[1,0], [0]],
		[[1,1], [0]]
	]
    
	neuralNetwork = NeuralNetwork(2, 3, 1)
	neuralNetwork.trainNetwork(trainingData)
	neuralNetwork.testNetwork(trainingData)
	

class ColoringProblem:

	def __init__(self, numOfVertices, numOfColors, graphMatrix):
		self.numOfVertices = numOfVertices
		self.numOfColors = numOfColors
		self.colors = [0]*numOfVertices
		self.graphMatrix = graphMatrix
	
	def solveColoringProblem(self):
		
		if self.solve(0):		
			self.showResult()
		else:
			print('No feasible solution with the given parameters...')

	def solve(self, nodeIndex):
	
		if nodeIndex == self.numOfVertices:
			return True
		
		#try all colors
		for colorIndex in range(1,self.numOfColors+1):
			
			if self.isColorValid(nodeIndex, colorIndex):
				#assign and proceed with next vertex
				self.colors[nodeIndex] = colorIndex
		
				if self.solve(nodeIndex+1):
					return True
				
				#BACKTRACK !!!

		return False
		
	def isColorValid(self, nodeIndex, colorIndex):
		
		for i in range(self.numOfVertices):
			if self.graphMatrix[nodeIndex][i] == 1 and colorIndex == self.colors[i]:
				return False
				
		return True

	def showResult(self):
	
		for i in range(self.numOfVertices):
			print('Node %d has color index: %d' % (i,self.colors[i]) )

		
if __name__ == "__main__":	

	graphMatrix = [[0,1,0,1,0],
				   [1,0,1,0,1],
				   [0,1,0,1,0],
				   [1,1,1,0,1],
				   [0,0,0,1,0]
				  ]
     
	numOfColors = 3
	numOfVertices = 5
	

	coloringProblem = ColoringProblem(numOfVertices,numOfColors,graphMatrix)
	coloringProblem.solveColoringProblem()
		
	
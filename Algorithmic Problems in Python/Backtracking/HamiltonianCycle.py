
class HamiltonianProblem:
	
	def __init__(self, adjacencyMatrix):
		self.numOfVertexes = len(adjacencyMatrix)
		self.hamiltonianPath = [None]*self.numOfVertexes
		self.adjacencyMatrix = adjacencyMatrix
		
	def hamiltonianCycle(self):
		
		self.hamiltonianPath[0] = 0;
		
		if not self.findFeasibleSolution(1):
			print('No feasible solution found...')
		else:
			self.showHamiltonianPath()
		
	def findFeasibleSolution(self, position):
	
		# check whether if we are done -> the last node can be connected to the first in order to form a cycle?
		if (position == self.numOfVertexes):
			x = self.hamiltonianPath[position - 1]
			y = self.hamiltonianPath[0]
			if ( self.adjacencyMatrix[x][y]  == 1): return True
			else: return False
		
		for vertexIndex in range(1,self.numOfVertexes):
			
			if self.isFeasible(vertexIndex, position):
				
				self.hamiltonianPath[position] = vertexIndex
				
				if self.findFeasibleSolution(position+1):
					return True
					
				# BACKTRACK
					
		return False
		
	def isFeasible(self, vertex, actualPosition):
	
		# first criteria: whether the two nodes are connected?
		if self.adjacencyMatrix[self.hamiltonianPath[actualPosition - 1]][vertex] == 0:
			return False;
		
		# second criteria: whether we have already added this given node?
		for i in range(actualPosition):
			if self.hamiltonianPath[i] == vertex:
				return False;
		
		return True;
	
	def showHamiltonianPath(self):
	
		print('Hamiltonian cycle exists: ')
		
		for i in range(self.numOfVertexes):
			print(self.hamiltonianPath[i]),
			
		print(self.hamiltonianPath[0])
		
if __name__ == "__main__":

	adjacencyMatrix = [[0,1,0],
					   [1,0,1],
					   [1,1,0]
					  ]

	hamiltonian = HamiltonianProblem(adjacencyMatrix)
	hamiltonian.hamiltonianCycle()
		
	
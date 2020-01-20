
class QueensProblem:
	
	def __init__(self, numOfQueens):
		self.numOfQueens = numOfQueens
		self.chessTable = [[None for i in range(numOfQueens)] for j in range(numOfQueens)]
		
	def solveQueensProblem(self):
		
		if self.solve(0):
			self.printQueens()
		else:
			print('There is no solution...')
	
	def solve(self, colIndex):
		
		if colIndex == self.numOfQueens:
			return True
		
		for rowIndex in range(self.numOfQueens):
		
			if self.isPlaceValid(rowIndex, colIndex):
				
				self.chessTable[rowIndex][colIndex] =  1
				
				if self.solve(colIndex+1):
					return True

				# BACKTRACK
				self.chessTable[rowIndex][colIndex] = 0
				
		return False
			
	def isPlaceValid(self, rowIndex, columnIndex):
		
		#same row
		for i in range(columnIndex):
			if self.chessTable[rowIndex][i] == 1:
				return False
				
		#from top left to bottom right
		j = columnIndex
		for i in range(rowIndex,-1,-1):
			
			if j < 0:
				break
				
			if self.chessTable[i][j] == 1:
				return False
			
			j = j -1
			
		#from bottom left to top right
		j = columnIndex
		for i in range(rowIndex,len(self.chessTable)):
			
			if j < 0:
				break
				
			if self.chessTable[i][j] == 1:
				return False
			
			j = j -1
			
		return True	
		
	def printQueens(self):

		for i in range(self.numOfQueens):
			for j in range(self.numOfQueens):
			
				if self.chessTable[i][j] == 1:
					print(' * ', end=""),
				else:
					print(' - ', end=""),
				
			print('\n')
		
if __name__ == "__main__":

	queensProblem = QueensProblem(100)
	queensProblem.solveQueensProblem()
		


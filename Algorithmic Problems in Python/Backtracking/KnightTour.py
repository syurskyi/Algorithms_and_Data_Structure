
class KnightTour:
	
	def __init__(self, boardSize):
		self.boardSize = boardSize
		self.xMoves = [2, 1, -1, -2, -2, -1, 1, 2]
		self.yMoves = [1, 2, 2, 1, -1, -2, -2, -1]
		self.solutionMatrix = [[-1 for x in range(boardSize)] for x in range(boardSize)]
		
	def solveKnightTourProblem(self):
		
		self.solutionMatrix[0][0] = 0;

		if self.solveProblem(1, 0, 0):
			self.showSolution()	
		else:
			print('No feasible solution found...')	
	
	def solveProblem(self, stepCount, x, y):
		
		if stepCount == (self.boardSize * self.boardSize):
			return True
		
		for i in range(self.boardSize):
		
			nextX = x + self.xMoves[i]
			nextY = y + self.yMoves[i]
		
			if self.isValidMove(nextX, nextY):
				
				self.solutionMatrix[nextX][nextY] =  stepCount
				
				if self.solveProblem(stepCount+1, nextX, nextY):
					return True
				
				self.solutionMatrix[nextX][nextY] = -1
	
		return False
		
	def isValidMove(self, x, y):
	
		if x < 0 or x >= self.boardSize: 
			return False
			
		if y < 0 or y >= self.boardSize:
			return False
			
		if self.solutionMatrix[x][y] > -1:
			return False
			
		return True
		
	def showSolution(self):
	
		for i in range(self.boardSize):
			for j in range(self.boardSize):
				print(self.solutionMatrix[i][j],end=" "),
				
			print('\n')
		
if __name__ == "__main__":

	knightTour = KnightTour(7)
	knightTour.solveKnightTourProblem()
		
	
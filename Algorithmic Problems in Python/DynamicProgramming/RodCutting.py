
class RodCutting:
	
	def __init__(self, lengthOfRod, prices):
		self.lengthOfRod = lengthOfRod
		self.prices = prices
		self.dpTable = [ [0]*(lengthOfRod+1) for x in range(len(prices)) ]
	
	def dynamicProgrammingApproach(self, lengthOfRod, prices):
		
		# 2 for loops to make sure the first row / column have all zeros !!!
	
		for i in range(1,len(self.prices)):
			for j in range(1,self.lengthOfRod+1):
			
				if i <= j:
					self.dpTable[i][j] = max(self.dpTable[i-1][j], self.prices[i]+self.dpTable[i][j-i]);
				else:
					self.dpTable[i][j] = self.dpTable[i-1][j];
		
	def showResults(self):
	
		print("Max profit is: $%d" % self.dpTable[len(self.prices)-1][self.lengthOfRod])
	
		columnIndex = self.lengthOfRod
		rowIndex = len(self.prices)-1
		
		while columnIndex > 0 or rowIndex > 0:
			
			if self.dpTable[rowIndex][columnIndex] == self.dpTable[rowIndex-1][columnIndex]:
				rowIndex = rowIndex - 1
			else:
				print("We make cut: ", rowIndex,"m")
				columnIndex = columnIndex - rowIndex
		
if __name__ == "__main__":

	lengthOfRod = 5
	prices = [0,2,5,7,3]

	rodCutting = RodCutting(lengthOfRod, prices)
	rodCutting.dynamicProgrammingApproach(lengthOfRod, prices)
	rodCutting.showResults()
	
	
	
		
	
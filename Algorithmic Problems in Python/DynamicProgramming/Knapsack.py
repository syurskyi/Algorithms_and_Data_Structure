
class Knapsack:
	
	def __init__(self, numOfItems, capacityOfKnapsack, weightOfItems, profitOfItems):
		self.numOfItems = numOfItems
		self.capacityOfKnapsack = capacityOfKnapsack
		self.weightOfItems = weightOfItems
		self.profitOfItems = profitOfItems
		self.dpTable = [[0 for x in range(capacityOfKnapsack+1)] for x in range(numOfItems+1)]
	
	def dynamicProgrammingApproach(self):
	
		# no need to initialize because there are 0s by default !!!
	
		for i in range(1,self.numOfItems+1):
			for w in range(1,self.capacityOfKnapsack+1):
				
				notTakingItem = self.dpTable[i-1][w]
				takingItem = 0
				
				if self.weightOfItems[i] <= w:
					takingItem = self.profitOfItems[i] + self.dpTable[i-1][w-self.weightOfItems[i]]
				
				self.dpTable[i][w] = max( notTakingItem, takingItem )
		
	def showResult(self):

		print("Total benefit: %d" % self.dpTable[self.numOfItems][self.capacityOfKnapsack])
		
		w = self.capacityOfKnapsack		
		for n in range(self.numOfItems,0,-1):

			if self.dpTable[n][w] !=0 and self.dpTable[n][w] != self.dpTable[n-1][w]:
				print("We take item #%d" % n )
				w = w - self.weightOfItems[n]

if __name__ == "__main__":

	numOfItems = 4
	capacityOfKnapsack = 7
	weightOfItems = [0,1,3,4,5]
	profitOfItems = [0,1,4,5,7]
	

	knapsack = Knapsack(numOfItems, capacityOfKnapsack, weightOfItems, profitOfItems)
	knapsack.dynamicProgrammingApproach()
	knapsack.showResult()
	
	
	
		
	
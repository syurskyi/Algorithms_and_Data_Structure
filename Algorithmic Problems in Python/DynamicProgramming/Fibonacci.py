
class Fibonacci:
	
	def __init__(self):
		self.memoizeTable = {}  # O(1)
		self.memoizeTable[0] = 0
		self.memoizeTable[1] = 1
	
	def fibonacciMemoize(self, n):
	
		if n in self.memoizeTable:
			return self.memoizeTable[n]
			
		self.memoizeTable[n-1] = self.fibonacciMemoize(n-1)
		self.memoizeTable[n-2] = self.fibonacciMemoize(n-2)
		
		calculatedNumber = self.memoizeTable[n-1] + self.memoizeTable[n-2] # O(1)
		self.memoizeTable[n] = calculatedNumber
	
		return calculatedNumber
	
	def naiveApproach(self, n):
		
		# f(n) = f(n-1) + f(n-2) where f(0) = 0 and f(1) = 1
		
		if n == 0: return 0
		if n == 1: return 1
		
		return self.naiveApproach(n-1) + self.naiveApproach(n-2)
		
if __name__ == "__main__":

	fibonacci = Fibonacci()
	print( fibonacci.naiveApproach(100) )
	
		
	
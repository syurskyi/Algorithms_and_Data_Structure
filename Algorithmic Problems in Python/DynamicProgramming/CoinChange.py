class CoinChange:
	
	# M - total amount and v[] coins
	def naiveApproach(self, M, v, index):
		
		if M < 0: return 0
		if M == 0: return 1
	
		if index == len(v): return 0
		
		return self.naiveApproach(M-v[index], v, index) + self.naiveApproach(M, v, index+1)
	
	# M - total amount and v[] coins
	def dynamicProgrammingApproach(self, v, M):
	
		dpTable = [ [0]*(M+1) for x in range(len(v)+1) ]
		
		#for j in range(M+1):
		#	dpTable[0][j] = 0
		
		for i in range(len(v)+1):
			dpTable[i][0] = 1
	
		for i in range(1,len(v)+1):
			for j in range(1,M+1):
			
				if v[i-1] <= j:
					dpTable[i][j] = dpTable[i-1][j] + dpTable[i][j-v[i-1]]
				else:
					dpTable[i][j] = dpTable[i - 1][j];
					
		print("Solution is: %d" % dpTable[len(v)][M] )
		
if __name__ == "__main__":

	M = 1000
	coins = [1,2,3]

	coinChange = CoinChange()
	coinChange.dynamicProgrammingApproach(coins,M)
	
	
	
		
	
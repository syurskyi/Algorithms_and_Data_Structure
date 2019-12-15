class PrivateClass:
	def __init__(self,name):
		self.name = name
	def __privatemethod(self):
		print "Hi i am a private method"
	def callprivate(self):
		print "In call private public method, and going to call private method ",self.name
		self.__privatemethod()

	
	#def __privatemethod(self): #can declare two methods with same signature but the lastly defined will be called
	#	print "private call complete\n\n"
	

obj = PrivateClass("praveen")

obj.callprivate()

#print "now call using __private"
#obj.__privatemethod() #raises error

print "use trick to call private method"
obj._PrivateClass__privatemethod()

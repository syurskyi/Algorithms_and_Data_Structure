#to check the working of self

class Praveen:
	def __init__(self,a,b):
		self.a = a
		self.b = b
		#self["name"] = "praveen" #self acts like a dictionary not working


	def test_self(self):
		print "in method with self"
		print "a = %d, b = %d"%(self.a,self.b)

	def test_without_self():
		print "in method without self"
		print "a = %d, b = %d"%(self.a,self.b)


obj  = Praveen(10,20)
print dir(obj)
print obj.__class__
#print obj.__bases__
#print obj.__name__
obj.test_self()
obj.test_without_self()  
print obj		

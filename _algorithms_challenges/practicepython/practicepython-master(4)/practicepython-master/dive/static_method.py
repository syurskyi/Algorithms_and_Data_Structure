import datetime
class Praveen(object):
	def __init__(self,name,a,b):
		print self #notice that instance in self is created already by new
		self.name=name
		self.a = a
		self.b = b
		print "In init"
		print self.name
		print "created at",self.created_at
		#print self
		print "\n"
	def __new__(cls, *args, **kwargs):
		print cls
		print "args is ",args
		print "kwargs is ",kwargs

		#to return the object created we should implement the details in depth or call the object class __new to take care of it
		new_instance = 	object.__new__(cls, *args, **kwargs)
		
		#here we set attribute created time for our identification
		setattr(new_instance,'created_at',datetime.datetime.now())
		return new_instance

	def nonstatic_method(self,a,b):
		print "In non static method"
		print "a = %d, b= %d "%(a,b)
		print "\n"

	def nonstatic_without_self(a,b):
		print "In non static without self"
		print "a= %d, b=%d "%(a,b)
		print "\n"

	@staticmethod
	def static_method(a,b):
		print "In static method"
		print "a = %d, b=%d"%(a,b)
		print "\n"




x = Praveen("praveen",10,b=20)
print x #to check whether the object gets actually created
x.nonstatic_method(10,20)
#Praveen.nonstatic_without_self(x,10,20)
x.static_method(10,20)
y = Praveen("praveen2",100,200)		

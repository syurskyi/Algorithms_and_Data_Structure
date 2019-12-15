#used to differentiate class attribute and data attribute


class Praveen:
	class_attribute = 0
	def __init__(self,data_attribute):
		self.data_attribute = data_attribute
		#class_attribute += 1 fails because it is considered as local without self keyword
		Praveen.class_attribute+=1 #considers it as Praveen class variable so count is 2 when using Class.class_attr. count is 1  if we use self.class_attr , also we can use self.__class__.classattr instead of Praveen.classattr


print Praveen.class_attribute #can be accessed with class name also
x = Praveen("praveen1")
print x.class_attribute #can be accessed with obj ref
print x.data_attribute


y = Praveen("praveen2")
print y.class_attribute
print y.data_attribute

print x.class_attribute
	

#this is to demonstrate the renaming of self keyword


class Praveen:
	def __init__(myownself,a,b): #always the first argument acts as this. for convention we use self
		myownself.a = a
		myownself.b = b
	def myfunc(myanotherself):
		print myanotherself.a+myanotherself.b


pobj = Praveen(10,20)

pobj.myfunc()

class Dog:
	def __init__(self,legs,colour):
		self.legs = legs
		self.colour = colour
	def __str__(self):
		return self.colour+" "+str(self.legs)

fido = Dog(4,"Brown")
spot = Dog(3,"Mostly yellow")

	
print repr(fido)

print spot

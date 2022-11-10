class Node:
	def __init__(self, data):
		self.data = data

		self.next = None


class Stack:
	def __init__(self):
		self.root = None

	def push(self, data):
		newnode = Node(data)
		newnode.next = self.root
		self.root = newnode

	def pop(self):
		if (self.isempty()):
			print("stack is empty")
			return "-1"
		temp = self.root
		self.root = self.root.next
		popped = temp.data
		return popped

	def isempty(self):
		return True if self.root is None else False


stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

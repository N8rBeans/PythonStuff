class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()
		raise IndexError("Stack Underflow:")

	def peek(self):
		return self.items[-1]
		raise IndexError("Stack Underflow:")

	def size(self):
		return len(self.items)
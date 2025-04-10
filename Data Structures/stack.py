class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)

class Stack:
	def __init__(self):
		"""Initialize an empty stack."""
		self.top = None
		self.length = 0

	def push(self, item):
		"""Push an item onto the stack."""
		newNode = Node(item)
		# check if stack is empty
		if(self.length == 0):
			self.top = newNode
		else:
			newNode.next = self.top
			self.top = newNode
		self.length += 1
		return True

	def pop(self):
		"""Remove and return the top item from the stack. Raise an error if empty."""
		if (self.length == 0):
			raise IndexError("Stack Underflow")
		temp = self.top
		self.top = self.top.next
		temp.next = None
		self.length -= 1
		if (self.length == 0):
			self.top = None
		return temp

	def peek(self):
		"""Return the top item without removing it. Raise an error if empty."""
		# check if the stack is empty
		if (self.length == 0):
			raise IndexError("Stack Underflow")
		return self.top

	def is_empty(self):
		"""Return True if the stack is empty, False otherwise."""
		return self.length == 0

	def size(self):
		"""Return the number of items in the stack."""
		return self.length

myStack = Stack()

# test error (it works but stops code so its commented)
#myStack.pop()

# test empty stack
print(myStack.is_empty())
# expected: is empty = True

myStack.push(5000)
myStack.push(4000)
myStack.push(3000)
myStack.push(2000)
myStack.push(1000)
# expected: 1000, 2000, 3000, 4000, 5000

print(myStack.size())
print(myStack.is_empty())
print(myStack.peek())
# expected: size = 5, is empty = False, peek = 1000

myStack.pop()
# expected: 2000, 3000, 4000, 5000

print(myStack.size())
print(myStack.is_empty())
print(myStack.peek())
# expected: size = 4, is empty = False, peek = 2000
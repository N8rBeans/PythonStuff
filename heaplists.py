class MinHeap:
	def __init__(self):
		self.heap = []

	def swap(self, i, j):
		self.heap[i], self.heap[j] = (self.heap[j], self.heap[i])

	def display(self):
		print(self.heap)

	def heapify_up(self, i):
		parent = (i - 1) // 2 # floor division
		if((i > 0) and (self.heap[i] < self.heap[parent])):
			self.swap(parent, i)
			self.heapify_up(parent) # recursion

	def heapify_down(self, i):
		minimum = i
		left = (2 * i) + 1
		right = (2 * i)  + 2
		if((left < len(self.heap)) and (self.heap[left] < self.heap[minimum])):
			minimum = left
		if((right < len(self.heap)) and (self.heap[right] < self.heap[minimum])):
			minimum = right
		if(minimum != i):
			self.swap(minimum, i)
			self.heapify_down(minimum)

	def insert(self, data):
		self.heap.append(data)
		self.heapify_up(len(self.heap))

	def remove_min(self):
		if(len(self.heap) > 1):
			self.swap(0, len(self.heap) - 1)
			minimum = self.heap.pop()
			self.heapify_down(0)
			print(min)
			return min
		elif(len(self.heap) == 1):
			minimum = self.heap.pop()
			return min
		else:
			print("Heap is empty")
			return None
class ArrayStack:
	'''FIFO stack implementation using python's List as storage.'''
	def __init__(self):
		self._data=[]

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return len(self._data)==0

	def top(self):
		if sel.is_empty():
			raise Empty("Stack is Empty")
		return self._data[-1]

	def push(self,e):
		self._data.append(e)
		self._size += 1

	def pop(self):
		if self.is_empty():
			raise Empty("Stack is Empty")
		self._data.pop()
		self._size -= 1
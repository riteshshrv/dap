class ArrayQueue():
	'''FIFO Queue implementation using Python's List as storage
	   and change its size dynamically (explicit).
	---------------------------------------------------------------------------
	Author: 	Ritesh Shrivastav
	email:  	ritesh.shrv@outlook.com
	@github: 	riteshshrv
	---------------------------------------------------------------------------'''
	
	DEFAULT_CAPACITY = 10
	
	def __init__(self):
		self._data=[None]*ArrayQueue.DEFAULT_CAPACITY
		self._size=0
		self._front=0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size==0

	def first(self):
		if self.is_empty():
			raise Empty("Queue is Empty")
		return self._data[self._front]

	def enqueue(self,e):
		if self._size==len(self._data):
			self._resize(2*(len(self._data)))	#double array size
		avail=(self._front+self._size)%len(self._data)
		self._data[avail]=e
		self._size += 1

	def dequeue(self):
		if self.is_empty():
			raise Empty("Queue is Empty")
		answer=self._data[self._front]
		self._data=None
		self._front=(1+self._front)%len(self._data)
		self._size -= 1
		if 0<self._size<len(self._data)//4:		#if size<1/4th then 
			self._resize((len(self._data)/2))	#half the array length
		return answer

	def _resize(cap):
		old=self._data
		self._data=[None]*cap
		walk=self._front
		for i in (len(self._data)):
			self._data[i]=old[walk]
			walk=(1+walk)%len(old)
		self._front=0

if __name__ == '__main__':
	raise Empty("""This is a Base Class for implementing ArrayQueue.\n
	---------------------------------------------------------------------------
	Author: 	Ritesh Shrivastav
	email:  	ritesh.shrv@outlook.com
	@github: 	riteshshrv
	---------------------------------------------------------------------------""")

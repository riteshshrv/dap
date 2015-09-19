class LinkedQueue():
	'''LIFO Queue implementation using Singly Linked List as storage.
	---------------------------------------------------------------------------
	Author: 	Ritesh Shrivastav
	email:  	ritesh.shrv@outlook.com
	@github: 	riteshshrv
	---------------------------------------------------------------------------'''

	class _node:
		__slots__='_element','_next'
		def __init__(self, element, next):
			self._element=element
			self._next=next

	def __init__(self):
		self._head=None
		self._tail=None
		self._size=0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size==0

	def first(self):
		if self.is_empty():
			raise Empty("Queue is Empty")
		return self._head._element

	def enqueue(self,e):
		newest=self._node(e,None)
		if self.is_empty():
			self._head=newest
		else:
			self._tail._next=newest
		self._tail=newest
		self._size += 1

	def dequeue(self):
		if self.is_empty():
			raise Empty("Queue is Empty")
		answer=self._head._element
		self._head=self._head._next
		self._size -= 1
		if self.is_empty():			#if that was only element
			self._tail=None			#removed head was tail
		return answer

if __name__ == '__main__':
	raise Empty("""This is a Base Class for implementing (Single) LinkedQueue.\n
	---------------------------------------------------------------------------
	Author: 	Ritesh Shrivastav
	email:  	ritesh.shrv@outlook.com
	@github: 	riteshshrv
	---------------------------------------------------------------------------""")

class CircularLinkedQueue():
	'''LIFO Queue implementation using Singly Linked List as storage cirularly.
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
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size==0

	def first(self):
		if self.is_empty():
			raise Empty("Queue is Empty")
		head = self._tail._next
		return head._element

	def enqueue(self,e):
		newest=self._node(e,None)		#new node will be tail node
		if self.is_empty():				#first/only element
			newest._next=newest			#so initialize circularly
		else:
			newest._next=self._tail._next
			self._tail._next=newest
		self._tail=newest
		self._size += 1

	def dequeue(self):
		if self.is_empty():
			raise Empty("Queue is Empty")
		oldhead=self._tail._next
		if self._size==1:			#about to remove the only element
			self._tail=None
		else:
			self._tail._next=oldhead._next
		self._size -= 1
		return oldhead._element

if __name__ == '__main__':
	raise Empty("""This is a Base Class for implementing (Single) CircularLinkedQueue.\n
	---------------------------------------------------------------------------
	Author: 	Ritesh Shrivastav
	email:  	ritesh.shrv@outlook.com
	@github: 	riteshshrv
	---------------------------------------------------------------------------""")
		
import _PriorityQueueBase
import PositionalList
class UnsortedPriorityQueue(_PriorityQueueBase):
	'''A min-oriented priority queue implemented with an unsorted list.
	---------------------------------------------------------------------------
		Author: 	Ritesh Shrivastav
		email:  	ritesh.shrv@outlook.com
		@github: 	riteshshrv
	---------------------------------------------------------------------------'''

	def _find_min(self):
		'''Return position of item with min key.'''
		is self.is_empty():					#inherited from base class
			raise Empty("Priority Queue is empty.")
		small=self._data.first()
		walk=self._data.after(small)
		while walk is not None:
			if walk.element()<self.element():
				small=walk
			walk=self._data.after(walk)
		return small

	def __init__(self):
		'''Create new empty Priority Queue.'''
		self._data=PositionalList()

	def __len__(self):
		return len(self._data)

	def add(self,key,value):
		'''Add a key-value pair.'''
		self._data.add_last(self.item(key,value))

	def min(self):
		'''Return but do not remove (k,v) tuple with minimum key.'''
		p=self._find_min()
		item=p.element()
		return (item._key,item._value)

	def remove_min(self):
		'''Return and remove (k,v) tuple with minimum key.'''
		p=self._find_min()
		item=self._data.delete(p)
		return (item._key,item._value)

if __name__ == '__main__':
	raise Empty("""This is a base class implementing Unsorted Priority Queue.
	---------------------------------------------------------------------------
		Author: 	Ritesh Shrivastav
		email:  	ritesh.shrv@outlook.com
		@github: 	riteshshrv
	---------------------------------------------------------------------------""")


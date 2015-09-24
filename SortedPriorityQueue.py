# import _PriorityQueueBase


class SortedPriorityQueue(_PriorityQueueBase):

    '''A min-oriented priority queue implemented with an sorted list.
    ---------------------------------------------------------------------------
            Author: 	Ritesh Shrivastav
            email:  	ritesh.shrv@outlook.com
            @github: 	riteshshrv
    ---------------------------------------------------------------------------'''

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._item(keu, value)  # make new item instance
        walk = self._data.last()  # walk backward looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)  # new key is smallest
        else:
            self._data.add_after(walk, newest)  # newest goes after walk

    def min(self):
        '''Return but do not remove (k,v) tuple with minimum key.'''
        if self.is_empty():
            raise Empty("priority Queue is Empty.")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        '''Remove and return (k,v) tuple with minimum key.'''
        if self.is_empty():
            raise Empty("priority Queue is Empty.")
        item = self._data.delete(self.data.first())
        return (item._key, item._value)

if __name__ == '__main__':
    print("""This is a base class implementing Sorted Priority Queue.
	---------------------------------------------------------------------------
		Author: 	Ritesh Shrivastav
		email:  	ritesh.shrv@outlook.com
		@github: 	riteshshrv
	---------------------------------------------------------------------------""")

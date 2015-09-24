class _PriorityQueueBase:

    '''Abstract Base Class for Priority Queue.
    ---------------------------------------------------------------------------
            Author: 	Ritesh Shrivastav
            email:  	ritesh.shrv@outlook.com
            @github: 	riteshshrv
    ---------------------------------------------------------------------------'''
    class _item:

        '''Light weight composite to store Priority Queue items.'''
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key  # comapare items based on their key

    def is_empty(self):
        return len(self) == 0

if __name__ == '__main__':
    print("""This is an abstract base class for implementing Priority Queue.
	---------------------------------------------------------------------------
		Author: 	Ritesh Shrivastav
		email:  	ritesh.shrv@outlook.com
		@github: 	riteshshrv
	---------------------------------------------------------------------------""")

class _DoublyLinkedListBase():

    '''Base class to support further Doubly Linked Lists.
    ---------------------------------------------------------------------------
            Author: 	Ritesh Shrivastav
            email:  	ritesh.shrv@outlook.com
            @github: 	riteshshrv
    ---------------------------------------------------------------------------'''

    class _node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._node(None, None, None)  # header Sentinel
        self._tailer = self._node(None, None, None)  # trailer Sentinel
        self._header._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        new = self._node(e, predecessor, successor)
        predecessor._next = new
        successor._prev = new
        self._size += 1
        return new

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        answer = node._element
        node._prev = node._next = node._element = None
        return answer

if __name__ == '__main__':
    print("""This is a Base class to support further Doubly Linked Lists.
	---------------------------------------------------------------------------
		Author: 	Ritesh Shrivastav
		email:  	ritesh.shrv@outlook.com
		@github: 	riteshshrv
	---------------------------------------------------------------------------""")

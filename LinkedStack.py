class LinkedStack():

    '''LIFO stack implementation using Singly Linked List as storage.
    ---------------------------------------------------------------------------
    Author: 	Ritesh Shrivastav
    email:  	ritesh.shrv@outlook.com
    @github: 	riteshshrv
    ---------------------------------------------------------------------------'''

    class _node():

        '''Nested 'node' class to implement Linked List'''
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._head._element

    def push(self, e):
        self._head = self._node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

if __name__ == '__main__':
    print("""This is a Base Class for implementing (Sinlge) LinkedStack.
	---------------------------------------------------------------------------
	Author: 	Ritesh Shrivastav
	email:  	ritesh.shrv@outlook.com
	@github: 	riteshshrv
	---------------------------------------------------------------------------""")

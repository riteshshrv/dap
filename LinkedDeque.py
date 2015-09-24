# import _DoublyLinkedBase


class LinkedDeque(_DoublyLinkedBase):

    '''(my)Deque Implementation which inherits from _DoublyLinkedBase
            using DoublyLinkedList. Built-in Implementation available in 
            class: 	collections.deque 
    ---------------------------------------------------------------------------
            Author: 	Ritesh Shrivastav
            email:  	ritesh.shrv@outlook.com
            @github: 	riteshshrv
    ---------------------------------------------------------------------------'''

    def first(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self._delete_node(self._trailer._prev)

if __name__ == '__main__':
    print("""This is a Base class to support (my) implementation of Deque using DoublyLinkedList.
	---------------------------------------------------------------------------
		Author: 	Ritesh Shrivastav
		email:  	ritesh.shrv@outlook.com
		@github: 	riteshshrv
	---------------------------------------------------------------------------""")

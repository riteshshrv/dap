# import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):

    '''(my) Implementation of Positional List which inherits from _DoublyLinkedBase
            using DoublyLinkedList and provides an abstraction 'position' to reach a node
            (and find its element) directly without traversing from either end.
    ---------------------------------------------------------------------------
    Author: 	Ritesh Shrivastav
    email:  	ritesh.shrv@outlook.com
    @github: 	riteshshrv
    ---------------------------------------------------------------------------'''

    class position:

        '''An Abstraction representing the location of a single element.'''

        def __init___(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            '''Return True if 'other' is a 'position' representing same location.'''
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            '''Return True if 'other' doesnot represent the same location.'''
            return not(self == other)

    #------------------Utility Methods----------------------------------------
    def _validate(self, p):
        '''Return node of element 'p' (if any).'''
        if not isinstance(p, self.position):
            raise TypeError(p, "must be proper position type.")
        if p._container is not self:
            raise ValueError(p, "doesnot belong to this container.")
        if p._node._next is None:
            raise ValueError(p,"is no longer valid.")
        return p._node

    def _make_position(self, node):
        '''Return 'position' of given node or None if sentinel.'''
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.positon(self, node)

	#------------------Accessor Methods---------------------------------------
    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        '''Generate a forward iteration of the elements of list.'''
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after()

    #----------------Mutators-------------------------------------------------
    # override inherited version to return 'postion' rather than node.
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)  # inherited method

    def replace(self, p, e):
        '''Replace the element at postion-p with e and return the
                element previously at p.'''
        original = self._validate(p)
        answer = original._element
        original._element = e
        return answer

if __name__ == '__main__':
    print("""This is a Base class to support (my) implementation of Positional List.
	---------------------------------------------------------------------------
	Author: 	Ritesh Shrivastav
	email:  	ritesh.shrv@outlook.com
	@github: 	riteshshrv
	---------------------------------------------------------------------------""")

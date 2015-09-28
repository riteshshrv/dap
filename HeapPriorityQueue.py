# import _PriorityQueueBase
# flake8: noq


class HeapPriorityQueue(_PriorityQueueBase):

    '''Heap Implementation of Priority Queue.
    ---------------------------------------------------------------------------
        Author: 	Ritesh Shrivastav
        email:  	ritesh.shrv@outlook.com
        @github: 	riteshshrv
    ---------------------------------------------------------------------------'''

    #----------non-public behaviours------------------------------------
    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j+1

    def _right(self, j):
        return 2*j+2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(parent, j)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left_child = self._left(j)
            small_child = left_child
            if self._has_right(j):
                right_child = self._right(j)
                if self._data[right_child] < self._data[left_child]:
                    small_child = right_child
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

# ----------------public behaviours------------------------------------
            def __init__(self, contents=()):
                self._data = [self._item(k, v) for k, v in contents]
                if len(self._data) > 1:
                    self._heapify()

            def _heapify(self):
                start = self._parent(len(self._data)-1)
                for i in range(start, -1, -1):
                    self._downheap(j)

            def __len__(self):
                return len(self._data)

            def add(self, k, v):
                newest = self._item(k, v)
                self._data.append(newest)
                self._upheap(len(self._data)-1)

            def min(self):
                if self.is_empty(self):
                    raise Empty("Priority Queue is Empty.")
                item = self._data[0]
                return (item._key, item._value)

            def remove_min(self):
                if self.is_empty(self):
                    raise Empty("Priority Queue is Empty.")
                self._swap(0, len(self._data)-1)
                p = self._data.pop()
                self._downheap(0)
                return (p._key, p._value)

if __name__ == '__main__':
    print("""This is a Base Class for implementing ArrayStack.
	---------------------------------------------------------------------------
	   Author: 	Ritesh Shrivastav
	   email:  	ritesh.shrv@outlook.com
	   @github: 	riteshshrv
	---------------------------------------------------------------------------""")

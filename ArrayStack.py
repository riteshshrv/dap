class ArrayStack:

    '''LIFO stack implementation using python's List as storage.
    ---------------------------------------------------------------------------
        Author: 	Ritesh Shrivastav
        email:  	ritesh.shrv@outlook.com
        @github: 	riteshshrv
    ---------------------------------------------------------------------------'''

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data[-1]

    def push(self, e):
        self._data.append(e)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        self._data.pop()
        self._size -= 1

if __name__ == '__main__':
    print("""This is a Base Class for implementing ArrayStack.
	---------------------------------------------------------------------------
	   Author: 	Ritesh Shrivastav
	   email:  	ritesh.shrv@outlook.com
	   @github: 	riteshshrv
	---------------------------------------------------------------------------""")

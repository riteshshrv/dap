class Tree:

    '''Abstract base class representing a tree structure.
    ---------------------------------------------------------------------------
    	Author:     Ritesh Shrivastav
    	email:      ritesh.shrv@outlook.com
    	@github:    riteshshrv
	---------------------------------------------------------------------------'''

    #----------nested Position class------------------------------------------
    class Position:

        '''An abstaction representing the location of a single element.'''

        def element(self):
            '''Return the element stored at this Position.'''
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            '''Return True if other Position represents the same location.'''
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            '''Return True if other does not represent the same location.'''
            return not (self == other)

    def root(self):
        '''Return the Positon representing the tree's root (or None if empty).'''
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        '''Return the Position representing p's parent (or None if p is root).'''
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        '''Return number of childrens that Positon p has.'''
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        '''Generate an iteration of Positions representing p's children.'''
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        '''Return the total number of elements in the tree.'''
        raise NotImplementedError('must be implemented by subclass')

    #-----------------concrete methods imolemented in this class--------------
    def is_root(self, p):
        '''Return True if Position p represents the root of the tree.'''
        return self.root() == p

    def is_leaf(self, p):
        '''Return True of Positon p does not have any children.'''
        return self.num_children == 0

    def is_empty(self):
        '''Return True if Tree is empty.'''
        return len(self) == 0

    def depth(self, p):
        '''Return the number of levels separating a Positon p from root.'''
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        '''Non-Public method for height of the subtree rooted at Positon p.'''
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        '''Return the height of the subtree rooted at Positon p.
                If p is None, return the height of the entire tree.'''
        if p is None:
            p = self.root()
        return self._height(p)


if __name__ == '__main__':
    print(
        "This is an Abstract Base Class for a implementing a Tree Structure.")

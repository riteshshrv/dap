from Tree import Tree


class BinaryTree(Tree):

    '''Abstract base class for representing a binary tree structure.
    ---------------------------------------------------------------------------
    	Author:     Ritesh Shrivastav
    	email:      ritesh.shrv@outlook.com
    	@github:    riteshshrv
	---------------------------------------------------------------------------'''

    #-------------additional abstract methods-------------------------------

    def left(self, p):
        '''Return a Position representing p's left child.
                Return None if p does not have a left child.'''
        raise NotImplemented("must be implemented by subclass")

    def right(self, p):
        '''Return a Position representing p's right child.
                Return None if p does not have a right child.'''
        raise NotImplemented("must be implemented by subclass")

    #---------------concrete methods implemented in this class.---------------
    def sibling(self, p):
        '''Return a Position representing p's sibling (or None if no sibling).'''
        parent = self.parent(p)
        if parent is None:						# p must be root
            return None 						# root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)		# possibly None
            else:
                return self.left(parent)		# possibly None

    def children(self, p):
        '''Generate an iteration of Positions representing p's children.'''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


if __name__ == '__main__':
    print("This is an Abstract Base Class for implementing Binary Tree Structure.")

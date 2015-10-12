class BinarySearchTree:

    '''My implementation of Binary Search Tree which creates a BST from given
        array of integers and also has implementaions of Depth First Traversal
        Algorithms viz. Preorder, Inorder and Postorder.
    ---------------------------------------------------------------------------
        Author:     Ritesh Shrivastav
        email:      ritesh.shrv@outlook.com
        @github:    riteshshrv
    ---------------------------------------------------------------------------'''

    class _node:
        __slots__ = '_element', '_left', '_right'

        def __init__(self, element, left, right):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None

    def insert(self, x):
        '''Public function to insert elements in BST.'''
        if self._root is None:
            self._root = self._node(x, None, None)
        else:
            current = self._root
            while True:
                if x < current._element:
                    if current._left:
                        current = current._left
                    else:
                        current._left = self._node(x, None, None)
                        break
                elif x > current._element:
                    if current._right:
                        current = current._right
                    else:
                        current._right = self._node(x, None, None)
                        break
                # does not permit duplicates
                else:
                    break

    def preorder(self, node=None):
        if node is None:
            node = self._root
        return self._preorder(node)

    def _preorder(self, node):
        if node is not None:
            print(node._element)
            self._preorder(node._left)
            self._preorder(node._right)

    def inorder(self, node=None):
        if node is None:
            node = self._root
        return self._inorder(node)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node._left)
            print (node._element)
            self._inorder(node._right)

    def postorder(self, node=None):
        if node is None:
            node = self._root
        return self._postorder(node)

    def _postorder(self, node):
        if node is not None:
            self._postorder(node._left)
            self._postorder(node._right)
            print(node._element)


def main():
    b = BinarySearchTree()
    a = [15, 10, 20, 25, 8, 12, 6, 22]
    for i in a:
        b.insert(i)
    print("Preorder Traversal")
    b.preorder()
    print("Inorder Traversal")
    b.inorder()
    print("Postorder Traversal")
    b.postorder()

if __name__ == '__main__':
    main()

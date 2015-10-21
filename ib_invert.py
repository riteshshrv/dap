'''A Program to invert a binary tree in-palce.'''
def _invertTree(self,root):
        root.left,root.right=root.right,root.left
        if root.left != None:
            self._invertTree(root.left)
        if root.right != None:
            self._invertTree(root.right)
            
    def invertTree(self, root):
        if root is not None:
            self._invertTree(root)
        return root
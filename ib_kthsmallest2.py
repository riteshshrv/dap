'''Given a binary search tree, write a function to find the kth smallest element in the tree.'''
class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    a=[]
    def _inorder(self,root):
        if root is not None:
            self._inorder(root.left)
            self.a.append(root.val)
            self._inorder(root.right)
        
    def kthsmallest(self, root, k):
        if root is None:
            return -1
        self.a=[]
        self._inorder(root)
        return self.a[k-1]
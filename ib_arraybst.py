'''Given an array where elements are sorted in ascending order, convert it to a height balanced BST'''
class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    head=None
    def _insert(self,a,start,end):
        if start>end:
            return None
        mid=(start+end)//2
        node=TreeNode(a[mid])
        node.left=self._insert(a,start,mid-1)
        node.right=self._insert(a,mid+1,end)
        return node
        
    def sortedArrayToBST(self, a):
        return self._insert(a,0,len(a)-1)
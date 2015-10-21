'''A Program to check whether to given trees are same.'''
def isSameTree(self, a, b):
        if a is None and b is None:
            return 1
        if (a is None and b is not None) or (a is not None and b is None):
            return 0
        if a.val != b.val:
            return 0
        return self.isSameTree(a.left,b.left) and self.isSameTree(a.right,b.right)
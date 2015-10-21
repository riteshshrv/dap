'''A program to check whether the tree is balanced or not'''
class Solution:
    # @param A : root node of tree
    # @return an integer
    ans=True
    def find_depth(self,a,d):
        if a is None:
            return d-1
        lt_d=self.find_depth(a.left,d+1)
        rt_d=self.find_depth(a.right,d+1)
        if abs(lt_d-rt_d)>1:
            self.ans=False
        return max(lt_d,rt_d)
    def isBalanced(self, a):
        self.find_depth(a,0)
        return self.ans
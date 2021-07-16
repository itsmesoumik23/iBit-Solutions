# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    
    def getMaxNode(self,A):
        maxInd = -1
        maxNum = -1*float("inf")
        if(len(A) == 0):
            return None
        for i in range(len(A)):
            if(A[i] > maxNum):
                maxInd = i
                maxNum = A[i]
        left = A[:maxInd]
        right = A [maxInd+1:]
        currNode = TreeNode(maxNum)
        currNode.left = self.getMaxNode(left)
        currNode.right = self.getMaxNode(right)
        return currNode
    
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        return self.getMaxNode(A)

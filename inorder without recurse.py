# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, root):
        current = root
        stack = []
        res = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if stack:
                    current = stack.pop()
                    res.append(current.val)
                    current = current.right
                else:
                    return res

        return res

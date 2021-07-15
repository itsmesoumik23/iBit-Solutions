# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reorderList(self, A):
        length = 0
        stack =[]
        temp = A
        while temp:
            length += 1
            stack.append(temp)
            temp = temp.next
        
        # we will perform only upto half of the length
        count = 0
        temp = A
        while count < length // 2:
            newNode = stack.pop()
            newNode.next = temp.next
            temp.next = newNode
            count += 1
            temp = newNode.next
        temp.next = None
        return A

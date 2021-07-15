# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def rotateRight(self, head, k):
        if head.next is None:
            return head
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        rotate = k % length
        count = 1
        temp  = head
        while True:
            if count == length - rotate:
                secondHalf = temp.next
                temp.next = None
                dummy = secondHalf
                if not dummy:
                    return head
                while True:
                    if dummy.next is None:
                        dummy.next = head
                        return secondHalf
                    else:
                        dummy = dummy.next
            else:
                temp = temp.next
                count += 1
        

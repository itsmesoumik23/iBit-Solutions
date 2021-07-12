# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:

	def lPalin(self, A):
        count = 1
        temp = A
        arr = []
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        p, q = 0, len(arr)-1
        while True:
            if p > q:
                break
            if arr[p] == arr[q]:
                p += 1
                q -= 1
            else:
                return 0
        return 1

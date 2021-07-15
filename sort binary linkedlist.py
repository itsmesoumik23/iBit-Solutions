# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        zero, one = 0, 0
        temp = A
        while temp is not None:
            if temp.val == 0: zero += 1
            else: one += 1
            temp = temp.next
        temp = A
        while temp is not None:
            if zero > 0:
                temp.val = 0
                zero -= 1
            else:
                temp.val = 1
            temp = temp.next
        return A

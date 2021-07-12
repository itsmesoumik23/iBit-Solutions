# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def solve(self, A):
        if A is None:
            return
        temp = A.next
        stack = []
        while True:
            if temp is None:
                break
            stack.append(temp.val)
            if temp.next is None:
                break
            temp = temp.next.next
        temp = A.next
        while stack:
            if temp is None:
                break
            temp.val = stack.pop()
            if temp.next is None:
                break
            temp = temp.next.next
        return A

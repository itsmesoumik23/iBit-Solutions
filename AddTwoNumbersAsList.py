# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
class Solution:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, data):
        if self.head is None:
            self.head = ListNode(data)
        else:
            newNode = ListNode(data)
            newNode.next = self.head
            self.head = newNode

	def addTwoNumbers(self, A, B):
        head1 = A
        head2 = B
        num1, num2 = "", ""
        temp = head1
        while temp is not None:
            num1 += str(temp.val)
            temp = temp.next
        temp = head2
        while temp is not None:
            num2 += str(temp.val)
            temp = temp.next
        
        final = str(int(num1[::-1]) + int(num2[::-1]))
        final = final.lstrip("0")
        for nums in final:
            self.insertAtBeginning(int(nums))
        return self.head

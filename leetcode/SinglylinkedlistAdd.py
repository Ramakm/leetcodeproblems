# You are given two non-empty linked lists representing two non-negative integers.
# # The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# # You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = None
        a = 0
        while l1 or l2 or a:
            if l1:
                a += l1.val
                l1 = l1.next

            if l2:
                a += l2.val
                l2 = l2.next

            if l3:
                l3.next = ListNode(a % 10)
                l3 = l3.next
            else:
                l0 = ListNode(a % 10)
                l3 = l0

            a = a // 10

        return l0

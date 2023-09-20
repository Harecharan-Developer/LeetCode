#92. Reverse Linked List II

#Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        l1 = []  # List to store the values of the linked list
        while head:
            l1.append(head.val)
            head = head.next
        
        # Reverse the sublist within the list
        while left <= right:
            l1[left - 1], l1[right - 1] = l1[right - 1], l1[left - 1]
            left += 1
            right -= 1
        
        # Reconstruct the linked list with reversed values
        dummy = ListNode()
        current = dummy
        for val in l1:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next

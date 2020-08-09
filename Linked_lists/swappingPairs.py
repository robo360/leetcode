"""
Level: Medium

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        first_node = head 
        if(head is None):
            return None
        if (head.next is None):
            return head
        second_node = head.next
        if(second_node.next is None):
            next_pair = None
        else:
            next_pair = self.swapPairs(second_node.next)
        first_node.next = next_pair
        second_node.next = first_node
        return second_node 
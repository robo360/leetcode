# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        two_finger = head
        one_finger = head
        previous_node = head
        i = 1
        while two_finger.next:
            if(i < n):
                two_finger = two_finger.next
            else:
                previous_node = two_finger
                two_finger = two_finger.next
                one_finger = one_finger.next
                if(two_finger.next is None and n != 1):
                    one_finger.val = one_finger.next.val
                    one_finger.next = one_finger.next.next

                if(two_finger.next is None and (n == 1)):
                    previous_node.next = None
            i += 1

        if(i==n):
            if(head.next):
                head = head.next
            else:
                head = None

        return head

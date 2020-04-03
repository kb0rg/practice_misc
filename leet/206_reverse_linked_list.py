"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:

        if head == None:
            return None
        if head.next == None:
            return head

        prev = None
        current = head
        old_next = current.next

        while old_next:
            # set new next for out list
            current.next = prev
            # reset prev to current
            prev = current
            current = old_next
            # store "next" from input list
            old_next = old_next.next

        current.next = prev
        return current

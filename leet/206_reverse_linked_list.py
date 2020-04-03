import unittest
from typing import List

"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

(Note: The tests on leetcode use regular lists as input and output values)
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

class Tests(unittest.TestCase):

    sol = Solution()

    def make_linked_list_from_list(self, input: List) -> ListNode:

        i = 0
        head = ListNode(input[i])
        current = head

        while i < (len(input) - 1):
            next_node = ListNode(input[i+1])
            current.next = next_node
            current = next_node
            i += 1
        current.next = None

        return head

    def make_list_from_linked_list(self, linked_list_head: ListNode) -> List:
        output_list = []
        current = linked_list_head

        while current.next != None:
            output_list.append(current.val)
            current = current.next
        output_list.append(current.val)
        return output_list

    def test_setup_functions(self):
        # Verify the list conversion functions work as advertised.
        test_input = [1,2,3,4,5]
        expected_output = [5,4,3,2,1]

        self.assertEqual(
            self.make_list_from_linked_list(
                self.make_linked_list_from_list(test_input)
                ),
            test_input)

    def test_base_case(self):
        test_input = [1,2,3,4,5]
        expected_output = [5,4,3,2,1]

        input_head = self.make_linked_list_from_list(test_input)
        reversed_linked_list = self.sol.reverseList(input_head)

        self.assertEqual(
            self.make_list_from_linked_list(reversed_linked_list),
            expected_output
            )


if __name__ == '__main__':
    unittest.main()
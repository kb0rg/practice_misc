"""
1490. Clone N-ary Tree
Medium

Given a root of an N-ary tree, return a deep copy (clone) of the tree.

Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its
children.

class Node {
    public int val;
    public List<Node> children;
}

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Follow up: Can your solution work for the graph problem?
https://leetcode.com/problems/clone-graph/


Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]


Constraints:

The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 10^4].
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
from collections import deque

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        self.traverse_tree(root)

    # DFS
    def traverse_tree(self, node: 'Node') -> 'Node':
        # pre-order
        # print(node.val)

        for child in node.children:
            self.traverse_tree(child)
        # post-order
        # print(node.val)

    # BFS
#     def traverse_tree(self, node: 'Node') -> 'Node':

#         q = deque()
#         q.append(node)

#         while q:
#             curr = q.popleft()
#             print(curr.val)
#             for child in curr.children:
#                 q.append(child)


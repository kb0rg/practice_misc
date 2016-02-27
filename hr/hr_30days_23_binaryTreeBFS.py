#!/bin/python
# -*- coding: utf-8 -*-
"""
hackerrank: 30 Days of Code: Day 23: Review+Binary Trees!
*same problem also in Data Structures: Trees:  Tree: Level Order Traversal
but not avail to solve in python

Problem Statement:
You are given a pointer root pointing to the root of a binary tree. You need to 
print the level order traversal of this tree. In level order traversal, we visit 
the nodes level by level from left to right. 

For example:
         3
       /   \
      5     2
     / \    /
    1   4  6

For the above tree, the level order traversal is 3 -> 5 -> 2 -> 1 -> 4 -> 6.

HINT: A queue could be helpful.

The code for input/output is already handled in the editor. You only have to 
complete the function levelOrder given in the editor.

Input Format:
First line contains T, the number of test cases. Next T lines contain an integer 
data to be added to the binary search tree.

Output Format:
Print the values of the level order traversal separated by spaces.

Sample Input:
6
3
5
4
7
2
1

Sample Output:
3 2 5 1 4 7 

Explanation:
Level 1:        3
              /   \
Level 2:     2     5
            /     /\
Level 3:   1     4  7 

We need to print the nodes level by level. We process each level from left to 
right. Level Order Traversal: 3 -> 2 -> 5 -> 1 -> 4 -> 7

"""
# given by HR:
import sys
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        ### end given by HR
        import Queue
        q = Queue.Queue()
         
        q.put(root)
        
        while not q.empty():
            curr = q.get()
            print curr.data,
            if curr.left:
                q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
                curr = curr.left
            elif curr.right:
                q.put(curr.right)
                curr = curr.right

# given by HR:
T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)


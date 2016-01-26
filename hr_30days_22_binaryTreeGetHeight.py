#!/bin/python
# -*- coding: utf-8 -*-
"""
hackerrank: 30 Days of Code: Day 22: Binary Search Trees
*same problem also in Data Structures: Trees: Tree: Height of a binary tree
but not avail to solve in python

Problem Statement:
The height of a binary tree is the number of nodes on the largest path from root 
to any leaf. You are given a pointer root pointing to the root of a binary 
search tree. Return the height of the tree. 
You only have to complete the function getHeight given in the editor.

Input Format:
First line contains T, the number of test cases. Next T lines contain an integer 
data to be added to the binary search tree.

Output Format:
Output the height of the binary search tree.

Sample Input:
7
3
5
2
1
4
6
7

Sample Output:
4

Explanation:
The Binary Search tree formed with the given values is

      3  
     /  \
    2    5
   /    /  \
  1    4    6
             \
              7

The maximum length root to leaf path is 3->5->6->7. There are 4 nodes in this 
path. Therefore the height of the binary tree = 4.

"""
# given by HR:
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

    def getHeight(self,root):
        ### end given by HR


# given by HR:
T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height  


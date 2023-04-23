from binarytree import Node
from binarytree import BinaryTree
from binarytree import Node
from bst import BinarySearchTree
""" 
Find out the smallest node in the binary tree
IDEA: 
 + Use any of the Traverses -> will go through all the nodes of the tree. 
 + For every node that goes through. Save them into a variable (prev) and check them with the next one
 + Start by prev = root  -> Use preorder
"""


class Tree2(BinarySearchTree):
    def minNode(self, node):
        if node.left is None:
            return node.elem
        if node.right is None:
            return node.elem
        return min(node.elem, min(self.minNode(node.left), self.minNode(node.Left)))



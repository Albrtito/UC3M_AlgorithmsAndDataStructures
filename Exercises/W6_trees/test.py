from binarytree import BinaryTree
from binarytree import Node
from bst import BinarySearchTree
from bintree import BinaryNode
from bintree import BinaryTree


class Tree2(BinaryTree):
    def preorder_traversal(self, node):
        ITnode = node
        print(ITnode)
        if node.left is not None:
            self.preorder_traversal(node.left)
        if node.right is not None:
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        ITnode = None
        if node.left is not None:
            self.postorder_traversal(node.left)
        if node.right is not None:
            self.postorder_traversal(node.right)
        ITnode = node
        print(ITnode)

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))


""" 
CREATION AND TESTING OF THE BINARY TREE
root = Node(1)
root_right = Node(2, parent=root)
root.right = root_right
root_left = Node(3, parent=root)
root.left = root_left
right2 = Node(4, parent=root_right)
root_right.right = right2
left2 = Node(5, parent=root_right)
root_right.left = left2
right3 = Node(6, parent=root_left)
root_left.right = right3
left3 = Node(7, parent=root_left)
root_left.left = left3
Tree = Tree2()
Tree._root = root
Tree.preorder_traversal(root)
Tree.postorder_traversal(root)
print(Tree.height(root))
"""


class BST2(BinarySearchTree):
    def search(self, node: BinaryNode, elem: object):
        """Return a node with the element specified in elem. The search starts
        in the node specified "node" """
        if node == None:
            raise ValueError("The element is not in the Tree")
        if elem < node.elem:
            self.search(node.left, elem)
        if elem > node.elem:
            self.search(node.right, elem)
        if elem == node.elem:
            print(node)
            return node

    def insert2(self, node: BinaryNode, elem: object):
        """Insert a node with the element "elem". Start at node "node" in order to search
        for the insertion point. """
        # Do a search for the element.
        if elem < node.elem:
            if node.left is None:
                node.left = BinaryNode(elem)
            else:
                self.insert2(node.left, elem)
        if elem > node.elem:
            if node.right is None:
                node.right = BinaryNode(elem)
            else:
                self.insert2(node.right, elem)
        if elem == node.elem:
            raise ValueError("Element is already in the Tree")

    def remove2(self, node: BinaryNode, elem: object):
        """
        Remove the element specified from the bst
        1. The node is a leaf

        Then just remove the node

        2. The node is an internal node with one child
            Then just remove the node and link the node´s child with the node´s parent.

        3. The node is an internal node with two childs.
            1. Search for the successor: The node in the right subtree with the smallest elem.
            2. The node element is changed  to be the same one as the successor elem
            3. Remove the successor
        """

        # Recursive cases





# CREATE A BINARY SEARCH TREE
root = BinaryNode(10)
bst = BST2()
bst._root = root
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(8)
bst.insert(20)
bst.insert(15)
bst.insert(30)
bst.search(root.left, 6)
bst.insert2(root, 9)
bst.search(root, 8)
bst.insert2(root, 7.5)
bst.search(root, 8)
bst.search(root,6)
print(root)
bst.remove2(root,6)
bst.search(root,6)
print(root)
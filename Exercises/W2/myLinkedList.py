"""
Linked list need to manage a series of nodes. Each node has a reference to the last node and an element.
1. Create two classes. One for the Singly linked list and another for the nodes:
    1.1 Singly list classes have a first node (HEAD) and a size as properties.No parameters need to be given
    1.2 Nodes have as properties the element they represent and a reference to the next node. Both the next node
     reference and the element are given as parameters. (the reference is set to None if nothing is given
    (there is nothing next))
2. Implement the basic singly linked list functions:
    2.1: AddFirst(e) -> adds an element as the first one of the list
    2.2: AddLast(e) -> Adds an element as he last one of the list
    2.3 RemoveFirst() -> Removes the first element and returns it´s value
    2.4 RemoveLast() -> Removes the last element and returns it´s value
    2.5 getAt(self,index) -> Returns the value of the element at that particular index (Not personally implemented)
"""
"""
Exercises: 
Implement the following methods: − contains(L,e):returns the first position of the
element e at the list. If e does not exist, then it returns -1.
− insertAt(L,index,e): inserts the element e at the position index of the list L.
− removeAt(L,index): removes the element at the
    position index from the list L.

Stacks and Queues implementations with single linked list: 
Implement a stack with a singly linked list. 
Implement a queue with a singly linked list.
"""

#Node class
class Node:
    def __init__(self, element, next = None):
        self.element = element
        self.next = next
#list class
class List:
    def __init__(self):
        self.head = None
        self.size = 0

    #AddFirst(e) implementation
    def AddFirst(self,element):
        """Create a new node: The node must have "element" as its value for self.element.The next node is going
        to be the Head node."""
        # Directly assign the head as the next node from the new node adding
        newNode = Node(element, self.head)
        # The new node created turns into the head of the list
        self.head = newNode
        self.size += 1

    #AddLast(e) implementation
    def AddLast(self,element):
        """Create a new node in the last place of the list -> Create a new node and give the penult element of
        the list (final list) the reference for that node created.
        1. Find the last element of the list (without the added element)
            This can be done by looking the nodes until one of them has no reference. This node has to be the last one.
        2. Assign the newNode as the reference for the last element of the original ist -> This turns into the
            penult element

        Especial cases:
        We need to have in mind that the list might be EMPTY then instead of adding last. We are adding firs
        """
        newNode = Node(element)
        # Check if the list is Empty ( is there a Head node)
        if self.head is not None:
            lastNode = self.head
        else:
            self.AddFirst(element)
        #While the node we are looking for has a next node (it is not the last) we keep iterating
        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = newNode
        #Increase the size
        self.size += 1

    #RemoveFirst(e) implementation
    def RemoveFirst(self):
        """This function should change the head element of the list. The new head element should be the referenced
        node by the anterior Head element."""
        # The variable that we´ll return
        result = None
        if self.isEmpty():
            # This error is not the right one
            raise ValueError("Cant Remove from an empty list")
        else:
            # Need to return THE ELEMENT of the list
            result = self.head.elem
            self.head = self.head.next
            self.size -= 1
            return result

    #RemoveLast(e) implementation:
    def RemoveLast(self):
        """In order to remove the last one:
            1. Is th elist empty? -> Cant remove from an empty list
            2. If the list is not empty -> Find the first element with a reference
                to None (that`s the last element). Get it´s value and return it
            3. Find the element penult of the list -> Need to turn the reference of this
                element to None"""
        if self.isEmpty():
            raise ValueError("Cant remove from an empty list")
        else:
            #The value we´ll return
            result = None
            if self.head.next is None:
                result = self.head.element
                self.head = None
            else:
                lastNode = self.head.next
                penultNode = self.head
                while lastNode.next is not None:
                    lastNode = lastNode.next
                    penultNode = penultNode.next
                penultNode.next = None
                result = lastNode.elem
                self.size -= 1
        return result

    #getAt(self,index) implementation: -> Theory implementation
    def getAt(self,index):
        if index < 0 or index >= self.size:
            print(index, 'error: index out of range')
        return None
        i = 0
        node = self.head
        while i < index: node = node.next
        i += 1
        return node.elem

    #isEmpty() implementation
    def isEmpty(self):
        # This is a boolean statement (==)
        return self.size == 0


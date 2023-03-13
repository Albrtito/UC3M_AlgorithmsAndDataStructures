import slistH


class dlist2(slistH):
    def leftrightShift(self, left, n):
        if left:
            node = self._head
            start = node  # Stores the first node to connect it to the last of our sequence
            for e in range(n - 1):  # Iterates until the last node that is not in the sequence
                node = node.next
            lastnode = node.next  # Not needed just saves one iteration of the while
            while lastnode.next is not None:  # It iterates for all the elements in the sequence
                lastnode = lastnode.next
            lastnode.next = start  # It takes the last element in the sequence and connects it to the rest of the list
            self._head = node.next  # It assigns the first element of the sequence to the head of the list.
            node.next = None  # Makes the last element of the list .next atribute be None
            return self
        else:
            node = self._head
            for e in range(1, self._size - n):  # Iterates the elements of the sequence
                node = node.next
            lastnode = node.next  # Not needed it saves one iteration
            while lastnode.next is not None:  # Finds the last node of the list
                lastnode = lastnode.next
            lastnode.next = self._head  # Assignst to the .next of the last element the head of the sequence
            self._head = node.next  # Assigns the new head of the list
            node.next = None  # Makes the last element's .next atribute None

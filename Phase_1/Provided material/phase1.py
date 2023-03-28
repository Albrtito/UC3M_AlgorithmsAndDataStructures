from slistH import SList
from slistH import SNode

import sys


class SList2(SList):

    # EXERCISE 1:
    def delLargestSeq(self):
        # implement here your solution
        if self._head.next is None:
            self._head = None
            return self
        seq1 = 0  # Variable to check the length of the sequences
        seq2 = 1  # Variable to store the length of the sequences
        node = self._head  # First node
        index = 0  # Tracks the index the iteration is on
        seqstart = 0  # Stores the index of the start of the sequence to remove
        afterseq = None  # Stores the object of the element after the sequence. It defaults to None if the sequence
        # is at the end
        posibleindex = -1  # It will store the index of the possible sequence
        while node.next is not None:  # Iterates all the list
            if node.elem == node.next.elem:  # Checks if we are in a sequence of same values
                seq1 += 1
            else:  # Changes the index of the start of the possible sequence since it is not in the current iteration
                posibleindex = index
            if seq2 <= seq1 and node.elem != node.next.elem:  # Checks if we are exiting a sequence and stores the
                # values in case
                # it´s the one
                afterseq = node.next
                seqstart = posibleindex
            if node.next.next is not None:  # Helps exclude the case the sequence ends due to the end of the list
                if node.elem != node.next.elem and node.next.elem == node.next.next.elem:  # Checks that the start of
                    # the
                    # sequence moves if there are two sequences together
                    posibleindex = index
            if node.elem != node.next.elem:  # Checks if we are not in a sequence and resets the seq parameters
                if seq1 > 0:
                    seq2 = seq1
                seq1 = 0
            node = node.next
            index += 1
        if seq2 <= seq1:
            afterseq = node.next
            seqstart = posibleindex
        if seqstart == -1 and seq2 > 1:
            seqstart = posibleindex
        node = self._head
        if seqstart == -1:
            self._head = afterseq
        else:
            for e in range(seqstart):
                node = node.next
            node.next = afterseq

        return

    # EXERCISE 2:
    def fix_loop(self):
        # implement here your solution
        # implementation using Floyd´s Cycle finding algorithm. Complexity O(n)
        """
        Source: GeeksforGeeks web.

        Finding a loop:
        This algorithm is based on a fast and slow iteration nodes. If there
        is no loop then the fast node will reach the end of the list (NONE)
        and there will be no loop. If the fast loop reaches te loop and starts
        cycling it then the slow node will reach the loop after that and at
        some point the slow node and fast node will be at the same node in the
        loop. We can then say that there´s a loop.


        Deleting the loop:
        1. Count the number of nodes that there are in the loop that was found
        2. Apply mathematical form of Floyd´s algorithm: Find the beginning of the cycle
            When firstly computing if there is a loop each iteration node does the following
            nº of iterations until they both equal.
            m -> Nodes before the beginning of the loop
            n -> Nodes in the loop
            k -> Nodes between the beginning of the loop and the node where the iteration equals
            x,y -> Times the iteration lopes the cycle
            ITslow -> (m +n*x +k)
            ITfast -> 2* (m + n*y + k) two times the slow

            Because they end up in the same node then:
            (m +n*x +k) = 2*(m +n*x +k)
            Then:
            m + k = (x-2y)*n : m+k is a multiple of n.
            m = i*n -k: There are the same number of steps in m than in i cycles - k.
            Then we can start an iteration node from the head IT_slow and another from k IT_fast.
            Then by the time the first node reaches m the second one has also reached m.
            IMPORTANT: If both nodes move at the same speed we evade having to loop twice as many times
            the cycle with IT_fast
            The node m is reached
        3. Find the end of the cycle -> Add the lenght of the cycle to the head
        4. Remove the cycle by setting the reference of the last node to none


        """

        ITfast = self._head
        ITslow = self._head

        # Check that we have not reached an end to the list. If we reach
        # an end then either of the following nodes is none then it´s an end
        while ITslow and ITfast and ITfast.next:
            ITslow = ITslow.next
            ITfast = ITfast.next.next

            # If both Iteration nodes meet then there is a loop
            if ITslow == ITfast:
                # remove the loop
                # 1. Count the number of nodes in the loop. Move one of the iteration nodes until it
                #    finds the other node again and keep count of how many nodes were in between.
                ITslow = ITslow.next
                lenght = 1
                while ITslow != ITfast:
                    ITslow = ITslow.next
                    lenght += 1

                # 2. Reach the starting node of the loop -> Explained above
                ITslow = self._head
                while ITslow != ITfast:
                    ITslow = ITslow.next
                    ITfast = ITfast.next

                # 3. Reach the end of the cycle
                for i in range(lenght - 1):
                    ITslow = ITslow.next

                # 4. Break the loop
                ITslow.next = None

                # Return true -> There´s a loop
                return True
        # There is no loop -> Return false
        return False

    def create_loop(self, position):
        # this method is used to force a loop in a singly linked list
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")

        current = self._head
        i = 0

        # We reach position to save the reference
        while current and i < position:
            current = current.next
            i += 1

        # We reach to tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next
        current.next = start_node

    # EXERCISE 3:
    def leftrightShift(self, left, n):
        # implement here your solution
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
            node.next = None  # Makes the last element of the list .next attribute be None
            return self
        else:
            node = self._head
            for e in range(1, self._size - n):  # Iterates the elements of the sequence
                node = node.next
            lastnode = node.next  # Not needed it saves one iteration
            while lastnode.next is not None:  # Finds the last node of the list
                lastnode = lastnode.next
            lastnode.next = self._head  # Assign to the .next of the last element the head of the sequence
            self._head = node.next  # Assigns the new head of the list
            node.next = None  # Makes the last element's .next attribute None


if __name__ == '__main__':

    l = SList2()
    print("list:", str(l))
    print("len:", len(l))

    for i in range(7):
        l.addLast(i + 1)

    print(l)
    print()

    l = SList2()
    print("list:", str(l))
    print("len:", len(l))

    for i in range(7):
        l.addLast(i + 1)

    print(l)
    print()

    # No loop yet, no changes applied
    l.fix_loop()
    print("No loop yet, no changes applied")
    print(l)
    print()

    # We force a loop
    l.create_loop(position=6)
    l.fix_loop()
    print("Loop fixed, changes applied")
    print(l)
    print()
    print()

    l = SList2()
    for i in [1, 2, 3, 4, 5]:
        l.addLast(i)
    print(l.delLargestSeq())

    l = SList2()
    for i in range(7):
        l.addLast(i + 1)

    print(l)
    l.leftrightShift(False, 2)
    print(l)

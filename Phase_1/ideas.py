from slistH import SList
from slistH import SNode
import unittest
import random
import time


class Dlist2(SList):

    # implementation using Floyd´s Cycle finding algorithm.
    """
    Source:

    Finding a loop:
    This algorithm is based on a fast and slow iteration nodes. If there
    is no loop then the fast node will reach the end of the list (NONE)
    and there will be no loop. If the fast loop reaches te loop and starts
    cycling it then the slow node will reach the loop after that and at
    some point the slow node and fast node will be at the same node in the
    loop. We can then say that there´s a loop.


    Deleting the loop:
    1. Count the number of nodes that there are in the loop that was found
    2. Apply mathematical form of Floyd´s algorithm:



    """

    def detect(self):
        ITfast = self._head
        ITslow = self._head

        # Check that we have not reached an end to the list. If we reach
        # an end then either of the following nodes is none then it´s an end
        while (ITslow and ITfast and ITfast.next):
            ITslow = ITslow.next
            ITfast = ITfast.next.next

            # If both Iteration nodes meet then there is a loop
            if ITslow == ITfast:
                print(ITslow)

                # Return true
                print("loop")
                return True
        # There is no loop -> Return false
        print("no loop")
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



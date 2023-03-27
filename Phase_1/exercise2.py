from slistH import SList
from slistH import SNode
import unittest
import random
import time


class Dlist2(SList):

    def fix_loop(self):
        """The purpose of this method is to detect loops in the list and
        break them.
        * We can only have one loop on each list: Cause each node is only referencing
        another one. (can´t reference more than one)
        * We can´t just go to the end of the list and set it´s reference to None because if there is a loop there´ll be
        no end
        IDEA:
        1. Use 1 while to go through each node until we reach None(if there was a None)
        2. For each of the nodes use another while to compare the reference of the node to each of the previous nodes
        3. If the reference matches with any of the previous nodes -> We have a loop
        4. When finding a loop. Set the reference of the starting loop node to None and return True
        5. If we don´t find any loops then we´ll reach None and return False. Without making changes"""

        if self.isEmpty():  # list empty
            return False
        # Loop the list until we find the last node. It will reference NONE or another node we have already
        # passed

        ITnode = self._head
        while ITnode is not None:  # Check for the end of the list. If we get to an element that is
            # None we know there is an end
            ITcheck = self._head  # We start by Iterating a check variable.
            while ITcheck is not ITnode:  # Check that the ITnode does not reference
                # to a previous node. Check all previous elements to ITnode.
                #ITcheck = ITcheck.next  # Keep iterating the check until we reach the ITnode

                if ITcheck == ITnode.next: # If the check node is the same as the reference of the ITnode we know the
                    # ITnode is creating a loop. We return True and break the loop (by setting it´s reference to None)
                    ITnode.next = None
                    return True
                
                ITcheck = ITcheck.next
                
            ITnode = ITnode.next # Iteration of the first while

        return False

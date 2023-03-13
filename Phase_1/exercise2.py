from slistH import SList
from slistH import SNode
import unittest
import random
import time


class Dlist2(SList):

    def fix_loop(self):
        """The purpose of this method is to detect loops in the list and
        break them.
        * We can only have one loop on each list: Cause each node is only referencint
        another one. (can´t reference more than one)"""

        if self.isEmpty():  # list empty
            return False
        # Loop the list until we find the last node. It will reference NONE or another node we have already
        # passed

        ITnode = self._head
        while ITnode is not None:  # Check for the end of the list. If we get to an element that is
            # None we know there
            # is an end
            ITcheck = self._head  # We start by Iterating a check variable.
            while ITcheck is not ITnode:  # Check that the ITnode does not reference
                # to a previous node. Check all previous elements to ITnode.
                ITcheck = ITcheck.next  # Keep iterating the check until we reach the ITnode
            # If the while stops we enter this if. If the while stopped
            if ITcheck == ITnode.next:
                return True
            ITnode = ITnode.next

        return False

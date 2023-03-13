import slistH


class dlist2(slistH):

    def fix_loop(self):
        """The purpose of this method is to detect loops in the list and
        break them.
        * We can only have one loop on each list: Cause each node is only referencint
        another one. (can´t reference more than one)"""

        if self.isEmpty():  # list empty
            return False
        # Loop the list until we find the last node. It will reference NONE or another node we have already
        # passed

        itnode = self.head
        # This is not valid because i´m using list.
        referenced_nodes = []

        if itnode is None:  # Last node references None
            return False
        else:  # Loop: Reference to a node we have already passed:
            itcheck = self.head
            while itcheck is not itnode.next:# Check that the itnode does not reference to a previous node
                itcheck = itcheck.next
                #We change the check variable and check if that reference is the same as the itnode.next
                if itcheck == itnode.next:
                    return True

                else:  # If there is loop
                    return True

from slistH import SList
from slistH import SNode
import unittest
import random
import time


class Dlist2(SList):

    #implementation with a complexity of O(n^2)
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
                if ITcheck == ITnode.next: # If the check node is the same as the reference of the ITnode we know the
                    # ITnode is creating a loop. We return True and break the loop (by setting it´s reference to None)
                    ITnode.next = None
                    return True

                ITcheck = ITcheck.next  # Keep iterating the check until we reach the ITnode

            ITnode = ITnode.next # Iteration of the first while


        return False

    #implementation using Floyd´s Cycle finding algorithm. Complexity O(n)
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
    def detect_and_remove(self):
        ITfast = self._head
        ITslow = self._head

        #Check that we have not reached an end to the list. If we reach
        #an end then either of the following nodes is none then it´s an end
        while ITslow and ITfast and ITfast.next:
            ITslow = ITslow.next
            ITfast = ITfast.next.next

            #If both Iteration nodes meet then there is a loop
            if ITslow == ITfast:
                #remove the loop
                #1. Count the number of nodes in the loop. Move one of the iteration nodes until it
                #    finds the other node again and keep count of how many nodes were in between.
                ITslow = ITslow.next
                lenght = 1
                while ITslow != ITfast:
                    ITslow = ITslow.next
                    lenght += 1

                #2. Reach the starting node of the loop -> Explained above
                ITslow = self._head
                while ITslow != ITfast:
                    ITslow = ITslow.next
                    ITfast = ITfast.next

                #3. Reach the end of the cycle
                for i in range(lenght-1):
                    ITslow = ITslow.next

                # 4. Break the loop
                ITslow.next = None



                #Return true
                return True
        #There is no loop -> Return false
        return False
import random
import unittest
from exercise2 import Dlist2


class Test(unittest.TestCase):
    # setup function
    def setUp(self):
        # SetUp for the test1 : List without loops
        self.test1 = Dlist2()
        for i in range(5):
            self.test1.addFirst(random.randint(0, 5))

        # SetUp for the test2 : List with a loop from tail to head
        self.test2 = Dlist2()
        for i in range(5):
            self.test2.addFirst(random.randint(0, 5))

        self.test2.create_loop(len(self.test2) - 1)

        """
        THIS CREATES A TIMEOUT ERROR
        # Get the last element to create a loop:
        last_elem_2 = self.test2._head
        for i in range(len(self.test2) - 1):
            last_elem_2 = last_elem_2.next
        # Link the last elem to the head elem.
        last_elem_2.next = self.test2._head
        """

        # SetUp for the test3: List with a loop from tail to a middle element:
        self.test3 = Dlist2()
        for i in range(5):
            self.test3.addFirst(random.randint(0, 5))
        """
        THIS CREATES A TIMEOUT ERROR
        # Create a loop on element 3: Using create_loop provided function:
        self.test3.create_loop(3)
        """
        # Get the element index in which to create a loop.
        loop_index = 3
        loop_elem = self.test3._head
        for i in range(loop_index + 1):  # Because the stop is omitted we need to add 1
            loop_elem = loop_elem.next
        
        # Get the last elem to create a loop:
        last_elem_3 = self.test3._head
        for i in range(len(self.test3) - 1):
            last_elem_3 = last_elem_3.next

        # Link the last elem to the loop elem.
        last_elem_3.next = loop_elem

    # TESTING

    # first test
    def test1(self):
        """No loops"""
        expected = [False, None]
        # Bool value returned by fix_loop
        bool_out = self.test1.fix_loop()

        # Get the last elem of the list and check it´s reference
        last_elem = self.test1._head
        for i in range(len(self.test1) - 1):
            last_elem = last_elem.next

        # The output generated by the fix_loop function: The bool value and the reference of the last element. That
        # should be none
        out = [bool_out, last_elem.next]

        self.assertEqual(str(expected), str(out))

    # second test
    def test2(self):
        """Loop tail-head"""
        # ** NO IMPLEMENTATION OF GETTING RID OF THE LOOP
        expected = [True, None]
        bool_out = self.test2.fix_loop()

        # Get the last elem of the list and check it´s reference
        last_elem = self.test2._head
        for i in range(len(self.test2) - 1):
            last_elem = last_elem.next

        # The output generated by the fix_loop function: The bool value and the reference of the last element. That
        # should be none
        out = [bool_out, last_elem.next]

        self.assertEqual(str(expected), str(out))

    # third test
    def test3(self):
        """Loop tail-middle point"""
        expected = [True, None]
        bool_out = self.test3.fix_loop()

        # Get the last elem of the list and check it´s reference
        last_elem = self.test3._head
        for i in range(len(self.test3) - 1):
            last_elem = last_elem.next

        # The output generated by the fix_loop function: The bool value and the reference of the last element. That
        # should be none
        out = [bool_out, last_elem.next]

        self.assertEqual(str(expected), str(out))

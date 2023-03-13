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
        # Get the last element to create a loop:
        last_elem_2 = self.test2._head
        for i in range(len(self.test2) - 1):
            last_elem_2 = last_elem_2.next
        # Link the last elem to the head elem.
        last_elem_2.next = self.test2._head

        # SetUp for the test3: List with a loop from tail to a middle element:
        self.test3 = Dlist2()
        for i in range(5):
            self.test3.addFirst(random.randint(0, 5))

        # Get the element index in which to create a loop.
        loop_index = 3
        loop_elem = self.test3._head
        for i in range(loop_index + 1):  # Because the stop is omitted we need to add 1
            loop_elem = loop_elem.next

        # Get the last elem to create a loop:
        last_elem_3 = self.test3._head
        for i in range(len(self.test2) - 1):
            last_elem_3 = last_elem_3.next

        # Link the last elem to the loop elem.
        last_elem_3.next = loop_elem

    # TESTING

    # first test
    def test1(self):
        """In a list with no loops we expect a False value in the fix_loop function
        and the same list as the one created. No changes should be made to the list."""
        print("test1")
        expected1 = [False, self.test1]
        bool_out = self.test1.fix_loop()
        out = [bool_out, self.test1]
        self.assertEqual(str(expected1), str(out))

    # second test
    def test2(self):
        print("test2")
        """In an slist with a loop from tail to head we expect a True bool value for 
        the fix_loop function and a list with no loop."""
        # ** NO IMPLEMENTATION OF GETTING RID OF THE LOOP
        expected2 = True
        bool_out = self.test2.fix_loop()
        out = bool_out
        self.assertEqual(str(expected2), str(out))

    # third test
    def test3(self):
        print("test3")

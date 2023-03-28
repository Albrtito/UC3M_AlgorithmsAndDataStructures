import unittest
import random
from phase1 import SList2


class Test(unittest.TestCase):

    # setUp is a method which is run before a test method is executed.
    # This is useful if you need some data (for example) to be present before running a test.

    def setUp(self):
        self.list = SList2()
        self.reference = SList2()

    # TESTING

    # TEST FOR EXERCISE 1
    def test1_1(self):
        """E1: Empty list"""
        # If the list is empty then ...
        ...

    def test1_2(self):
        """E1: One element"""
        # If the list has only one element then ...
        ...

    def test1_3(self):
        """E1: Left"""
        # If the list has...

    def test1_4(self):
        """E1: Right"""
        # If the list has...
        ...

    # TEST OF EXERCISE 2
    def test2_1(self):
        """E2: No loops"""
        # Create the list:
        for i in range(5):
            self.list.addFirst(random.randint(0, 5))

        expected = [False, None]
        # Bool value returned by fix_loop
        bool_out = self.list.fix_loop()

        # Get the last elem of the list and check it´s reference
        last_elem = self.list._head
        for i in range(len(self.list) - 1):
            last_elem = last_elem.next

        # The output generated by the fix_loop function: The bool value and the reference of the last element. That
        # should be none
        out = [bool_out, last_elem.next]

        self.assertEqual(str(expected), str(out))

    # second test
    def test2_2(self):
        """E2: Loop tail-head"""
        # Create the list
        self.list = SList2()
        for i in range(5):
            self.list.addFirst(random.randint(0, 5))

        # Create the loop
        self.list.create_loop(3)

        # Checking values
        expected = [True, None]

        bool_out = self.list.fix_loop()

        # Get the last elem of the list and check it´s reference
        last_elem = self.list._head
        for i in range(len(self.list) - 1):
            last_elem = last_elem.next

        # The output generated by the fix_loop function: The bool value and the reference of the last element. That
        # should be none
        out = [bool_out, last_elem.next]

        self.assertEqual(str(expected), str(out))

    # third test

    def test2_3(self):
        """E2: Loop tail-middle point"""
        # Create the list:
        self.list = SList2()
        for i in range(5):
            self.list.addFirst(random.randint(0, 5))

        # Create a loop on element 3: Using create_loop provided function:
        self.list.create_loop(position=3)

        # Check the values
        expected = [True, None]
        bool_out = self.list.fix_loop()

        # Get the last elem of the list and check it´s reference
        last_elem = self.list._head
        for i in range(len(self.list) - 1):
            last_elem = last_elem.next

        # The output generated by the fix_loop function: The bool value and the reference of the last element. That
        # should be none
        out = [bool_out, last_elem.next]

        self.assertEqual(str(expected), str(out))

    # implement here your test cases

    def test2_4(self):
        """E2: Empty"""
        expected = [False, None]
        bool_out = self.list.fix_loop()
        out = [bool_out, self.list._head]

        ...

    # TEST OF EXERCISE 3

    def test3_1(self):
        """E3: Some case"""
        # If the list ...
        ...

    def test3_1(self):
        """E3: Some case"""
        # If the list  ...
        ...

    def test3_1(self):
        """E3: Some case"""
        # If the list  ...
        ...

    def test3_1(self):
        """E3: Some case """
        # If the list  ...
        ...


if __name__ == "__main__":
    unittest.main()

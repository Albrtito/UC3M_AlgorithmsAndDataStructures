"""
Problem 1: Write a recursive method for finding the minimum element in a list of integers
"""
import unittest


# This implementation uses the min function for list. If we wanted to create a min function
# for this specific case we could create it outside and name it Mymin
def min_elem(int_list: list):
    if len(int_list) == 1:
        return int_list[0]
    else:
        return min(int_list[0], min_elem(int_list[1:]))


class Test(unittest.TestCase):
    def setUp(self):
        self.testlist = []
        # For list 1
        self.list1 = [6]
        self.expected1 = 6
        self.min_list1 = []

        # Decide what to run
        self.testlist = self.list1

    def test_1(self):
        # min elem of list 1
        self.min_list1 = min_elem(self.testlist)
        self.assertEqual(str(self.expected1), str(self.min_list1))

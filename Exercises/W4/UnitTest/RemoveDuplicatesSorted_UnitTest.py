import unittest
from removeDuplicates import DList2


class Test(unittest.TestCase):

    def setUp(self):
        # For sorted list

        # The list is emtpy
        self.input_empty = DList2()
        self.expected_empty = self.input_empty

        #The list has no duplicates
        self.input_nodup = DList2()
        for e in [1,2,3,4,5,6,7,8]:
            self.input_nodup.addLast(e)
        self.expected_nodup = self.input_nodup

        #The list has all duplicates
        self.input_alldup = DList2()
        for e in [1,1,1,1,1,1,1,1]:
            self.input_alldup.addLast(e)
        self.expected_alldup = [1]

        #The list is the "normal case"
        self.input_normal = DList2()
        for e in [1,1,1,2,3,4,5,6,11,22,33,44,55,567,567,789,789,789]:
            self.input_normal.addLast(e)
        self.expected_normal = [1,2,3,4,5,6,11,22,33,44,55,567,789]
        # Test sorted list

    def test_empty(self):
        self.input_empty.removeDuplicatesSorted()
        self.assertEqual(str(self.input_empty),str(self.expected_empty))

    def test_nodup(self):
        self.input_nodup.removeDuplicatesSorted()
        self.assertEqual(str(self.input_nodup), str(self.expected_nodup))

    def test_alldup_unsorted(self):
        self.input_alldup.removeDuplicatesSorted()
        self.assertEqual(str(self.input_alldup),str(self.expected_alldup))

    def test_normal_unsorted(self):
        self.input_normal.removeDuplicatesSorted()
        self.assertEqual(str(self.input_normal),str(self.expected_normal))


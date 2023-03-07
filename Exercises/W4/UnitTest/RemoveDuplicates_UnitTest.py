import unittest
from removeDuplicates import DList2


class Test(unittest.TestCase):

    def setUp(self):
        # For unsorted list
        self.uinput_empty = DList2()
        self.uexpected_empty = self.uinput_empty

        # The list has no duplicates
        self.uinput_nodup = DList2()
        for e in [2, 4, 5, 3, 7, 8, 9]:
            self.uinput_nodup.addLast(e)
        self.uexpected_nodup = self.uinput_nodup

        # The list has all duplicates
        self.uinput_alldup = DList2()
        for e in [5, 5, 5, 5, 5, 5, 5]:
            self.uinput_alldup.addLast(e)
        self.uexpected_alldup = [5]

        # The list is the "normal case"
        self.uinput_normal = DList2()
        for e in [2,3,3,4,2,3,4,5,1,1,5,1,3,2,4,6,7,8,1,2,3,4,6,9,3,4,5]:
            self.uinput_normal.addLast(e)
        self.uexpected_normal = [2,3,4,5,1,6,7,8,9]

        # Test unsorted list
    def test_empty_unsorted(self):
        self.uinput_empty.removeDuplicates()
        self.assertEqual(str(self.uinput_empty), str(self.uexpected_empty))

    def test_nodup_unsorted(self):
        self.uinput_nodup.removeDuplicates()
        self.assertEqual(str(self.uinput_nodup), str(self.uexpected_nodup))

    def test_alldup_unsorted(self):
        self.uinput_alldup.removeDuplicates()
        self.assertEqual(str(self.uinput_alldup), str(self.uexpected_alldup))

    def test_normal_unsorted(self):
        self.uinput_normal.removeDuplicates()
        self.assertEqual(str(self.uexpected_normal),str(self.uinput_normal))
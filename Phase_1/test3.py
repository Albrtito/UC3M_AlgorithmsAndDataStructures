import unittest
import random
from exercise3 import Slist2


class Test3(unittest.TestCase):

    # SET UP THE INITIAL CONDITIONS
    def setUp(self):
        self.list = Slist2()
        self.reference = Slist2()

    # TEST THE DIFFERENT CASES
    def testempty(self):
        list = Slist2(self.list)
        check = self.reference
        self.assertEqual(len(list), len(check), "Fail: len in a length of length==0")

    def test_one_element(self):
        self.list.addFirst(1)
        list = Slist2(self.list)
        list.delLargestSeq()
        check = self.reference
        check.addFirst(1)
        self.assertEqual(len(list), len(check), "Fail: len in a length of length==1")

    def test_left(self):
        list = self.list
        list.addLast(1)
        list.addLast(1)
        list.addLast(1)
        list.addLast(1)
        list.addLast(2)
        list.addLast(3)
        list = Slist2(list)
        list.leftrightShift(True, 3)
        check = self.reference
        check.addLast(1)
        check.addLast(2)
        check.addLast(3)
        check.addLast(1)
        check.addLast(1)
        check.addLast(1)
        self.assertEqual(len(list), len(check), "Fail: DeleteSequence didn't work")

    def test_right(self):
        list = self.list
        list.addLast(1)
        list.addLast(1)
        list.addLast(1)
        list.addLast(1)
        list.addLast(2)
        list.addLast(3)
        list = Slist2(list)
        list.leftrightShift(False, 3)
        check = self.reference
        check.addLast(1)
        check.addLast(2)
        check.addLast(3)
        check.addLast(1)
        check.addLast(1)
        check.addLast(1)
        self.assertEqual(len(list), len(check), "Fail: DeleteSequence didn't work")

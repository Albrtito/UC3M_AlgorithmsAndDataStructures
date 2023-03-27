import unittest
from phase1 import SList2
from slistH import SList
from slistH import SNode

class Test(unittest.TestCase):

    def setUp(self):
	     self.list = SList()
         self.reference = SList()

    def testempty(self):
	      list = SList2(self.list)
          check = self.reference
          self.assertEqual(len(list), len(check), "Fail: len in a length of length==0")
     
    def test_one_element(self):
          list = SList2(self.list)
          list.delLargestSeq()
          check = self.reference
          self.assertEqual(len(list),len(check), "Fail: len in a length of length==1")

    def test_one_sequence(self):
          list = self.list
          list.addLast(1)
          list.addLast(1)
          list.addLast(1)
          list.addLast(1)
          list.addLast(2)
          list.addLast(3)
          list = SList2(list)
          list.delLargestSeq()
          check = self.reference
          check.addLast(2)
          check.addLast(3)
          self.assertEqual(len(list),len(check), "Fail: DeleteSequence didn't work")
    def test_two_sequence(self):
          list = self.list
          list.addLast(1)
          list.addLast(1)
          list.addLast(3)
          list.addLast(3)
          list = SList2(list)
          list.delLargestSeq()
          check = self.reference
          check.addLast(1)
          check.addLast(1)
          self.assertEqual(len(list),len(check), "Fail: DeleteSequence didn't work")
    def test_first_sequence_bigger(self):
          list = self.list
          list.addLast(1)
          list.addLast(1)
          list.addLast(1)
          list.addLast(3)
          list.addLast(3)
          list = SList2(list)
          list.delLargestSeq()
          check = self.reference
          check.addLast(3)
          check.addLast(3)
          self.assertEqual(len(list),len(check), "Fail: DeleteSequence didn't work")
    def test_second_sequence_bigger(self):
          list = self.list
          list.addLast(1)
          list.addLast(1)
          list.addLast(3)
          list.addLast(3)
          list.addLast(3)
          list = SList2(list)
          list.delLargestSeq()
          check = self.reference
          check.addLast(1)
          check.addLast(1)
          self.assertEqual(len(list),len(check), "Fail: DeleteSequence didn't work")
    def test_no_sequence(self):
          list = self.list
          list.addLast(1)
          list.addLast(2)
          list.addLast(3)
          list = SList2(list)
          list.delLargestSeq()
          check = self.reference
          check.addLast(1)
          check.addLast(2)
    
    
    
    
    

















        
if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
from dlist import DList
from dlist import DNode

class DList2(DList):
      
       
    def removeDuplicatesSorted(self):
        
            
        if len(self)>1:
            
            prevIt=self.head
            nodeIt=prevIt.next
            
            count = 0
          
            while nodeIt is not None:
                
                
                if prevIt.elem==nodeIt.elem:
                  
                   while nodeIt and  nodeIt.elem == prevIt.elem:
                       nodeIt = nodeIt.next
                       count += 1
                      
                   self.size -= count
                   
                   prevIt.next = nodeIt
                   if nodeIt is None:
                      self.tail = prevIt 
                   else:
                      nodeIt.prev = prevIt
                     
                      
                          
                prevIt = nodeIt
                if nodeIt:
                    nodeIt = nodeIt.next

    def removeDuplicates(self):

        if len(self) > 1:

            prevIt = self.head
            nodeIt = prevIt.next

            while prevIt:
                while nodeIt:
                    if nodeIt.elem == prevIt.elem:
                        nodeIt.prev.next = nodeIt.next
                        if nodeIt.next:
                            nodeIt.next.prev = nodeIt.prev

                    nodeIt = nodeIt.next

                if prevIt.next is None:
                    self.tail = prevIt
                    break
                elif prevIt.next.next is None:
                    self.tail = prevIt.next
                    break

                prevIt = prevIt.next
                nodeIt = prevIt.next







if "start" == "start":
    print("true")
else:
    print("false")
                        
                    
         
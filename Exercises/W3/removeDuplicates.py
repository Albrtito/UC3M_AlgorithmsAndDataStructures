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








l4=DList2()
for i in range(8):
      l4.addLast(i)  
print(l4)              
l4.insertAt(1,1)
l4.insertAt(1,1)
l4.insertAt(6,3)
l4.insertAt(8,5)
l4.insertAt(9,5)
l4.addLast(7)
l4.addLast(7)
l4.addFirst(0)
l4.addFirst(0)

print("before remove duplicates (sorted):",l4)
l4.removeDuplicatesSorted()
print("after remove duplicates (sorted):", l4)
print()                
                  
l4=DList2()
for i in range(8):
      l4.addLast(i)     
l4.addFirst(0)
l4.addFirst(0)

print("before remove duplicates (sorted):",l4)
l4.removeDuplicatesSorted()
print("after remove duplicates (sorted):", l4)
print()  
        
l4=DList2()
for i in range(8):
      l4.addLast(i)     
l4.addLast(7)
print("before remove duplicates (sorted):",l4)
l4.removeDuplicatesSorted()
print("after remove duplicates (sorted):", l4)
print()       
                 
                  
                        
                    
         
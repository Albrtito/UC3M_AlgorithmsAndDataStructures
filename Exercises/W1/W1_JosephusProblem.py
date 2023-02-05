"""
Given n soldiers, and k being the number of soldiers skipped before killing the next one. Meaning if n=6 and k=3,
the first one to kill must skip 2 soldiers and kill the third one, then the fourth soldier skips 2, killing the first
one, then the second soldier must kill the 4th and so on.
Implement a method to find out what position Josephus should sit in order to not be
killed. The solution should generalize for any number of jewish soldiers and any step.
The solution should use a queue of integers (each soldier is represented with a number
from 1 to n).
"""
"""
IDEA: 
+ Order the people in a Queue (numbers) 
+ Dequeue the number k of people and enqueue them back (move them from the top to the bottom)
+ Dequeue -> KILL
repeat the last two steps until the size is 1.
"""


class Queue:
    """FIFO Queue implementation using a Python list as storage.
    We add new elements at the tail of the list (enqueue)
    and remove elements from the head of the list (dequeue)."""

    def __init__(self):
        """Create an empty queue"""
        self.items = []

    def __len__(self):
        """Return the number of elements in the queue"""
        return len(self.items)

    def isEmpty(self):
        """Return True if the queue is empty"""
        # return len(self.items)==0
        return len(self) == 0
        # return self.items==[]

    def __str__(self):
        return str(self.items)

    def enqueue(self, e):
        """Add the element e to the tail of the queue"""
        self.items.append(e)

    def dequeue(self):
        """Remove and return the first element in the queue"""
        if self.isEmpty():
            print('Error: Queue is empty')
            return None
        # remove first item from the list
        return self.items.pop(0)

    def front(self):
        """Return the first element in the queue"""
        if self.isEmpty():
            print('Error: Queue is empty')
            return None

        # returns first element in the list
        return self.items[0]


# create the queue
number_of_soldiers = int(input("Enter a number from 1 to n: "))
q = Queue()
for i in range(1, number_of_soldiers + 1):
    q.enqueue(i)
# Ask for number of Steps to kill
steps_to_kill = int(input("STEP: Enter a number from 1 to n: "))

while q.__len__() > 1:
    # Take out the ones who live and the one who kills
    for i in range(steps_to_kill):
        q.enqueue(q.dequeue())
    # Kill and take out the one who dies
    q.dequeue()

print(q)

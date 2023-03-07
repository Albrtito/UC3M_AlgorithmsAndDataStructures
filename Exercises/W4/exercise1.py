"""
1. Write a function randomList(n,a,b) that returns a list of n random integers between a and
b. The function can consider that the default values for a and b are 0 and 25, respectively.
This functions will be used later.
"""
import random
def randomList(n,a = 0,b = 25):
    randomlist = []
    for i in range (n): #we are repeating this n times.
        randomlist.append(random.randint(a,b))
    return randomlist
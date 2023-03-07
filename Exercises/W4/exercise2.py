"""
2. Write a function, called sumList(l), which takes a list of integers as parameter and returns
the sum of all its elements. You must empirically study the time complexity of this function.
To do this, you should include instructions to measure the running time. Then, you should run
it for different size of lists (such as 10,100,1000,10000,10000,etc). Finally, plot its time
complexity on list of different sizes. What does the running time depend on?
Notes:
● You should use the randomList function to generate lists of different sizes.
● When you plot the results, you should choose the logarithmic scale for the axes.

"""
import unittest #unitest let us do analysis of functions.
def sumList(l):
    "l is a list of parameters. The function sums all the parameters in the list l"
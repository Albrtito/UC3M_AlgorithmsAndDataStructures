"""
Problem 5: Write a recursive method that takes two integers x and y and returns
x times y by using the russian method. This russian method consists of :

1) Make two columns. Write the largest number in the first column,
and the smallest in the second.
2) In the first column, divide the number by 2 repeatedly until to get to 1.
In the second column, multiply the number by 2 until you have the same rows
as in the first column.
3) Cross out the rows whose value in the first column is an even number
(x % 2==0)
4) Add the values in the second columns. The result is the answer.
For example, 17*100=1700
"""

def russian_method(number1: int, number2:int):
    ...
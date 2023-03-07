"""
Problem 3: Write a recursive method that takes an integer and returns the sum of its digits (for
example, for n=2356, the method should return 2+3+5+6=16).
Hint: 2356/10=235, 235/10=23,
23/10=2.
"""


def sum_digits(number: int):
    if number < 10:
        return number
    return number % 10 + sum_digits(number // 10)


test = 534
print(sum_digits(test))
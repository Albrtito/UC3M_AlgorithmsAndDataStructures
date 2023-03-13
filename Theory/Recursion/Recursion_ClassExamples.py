# -*- coding: utf-8 -*-
"""unit4-7feb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J5rIxWXJ_IObNytNE1ssVwMKrBDjMAbS

# Factorial
"""


def factorialIt(n):
    "Iterative solution"

    if type(n) != int or n < 0:
        print('n must be a positive number')
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


for i in range(10):
    print('factorial({})={}'.format(i, factorialIt(i)))


def factorial(n):
    """Returns the factorial of n. n
  should be a positive integer"""

    if type(n) != int or n < 0:
        print('n must be a positive number')
        return None

    if n == 0:  # BASE CASE
        return 1

    else:  # RECURSIVE OR GENERAL CASE
        return n * factorial(n - 1)


for i in range(5):
    print('factorial({})={}'.format(i, factorial(i)))

"""# Multiplication by Addition"""


def multiply(a, b):
    # assume that a,b are positive integers
    i = 1
    result = 0
    while i <= b:
        result += a
        i += 1

    return result


for i in range(11):
    print("multiply({},{})={}".format(i, 5, multiply(i, 5)))


def multiplyRec(a, b):
    # assume that a,b are positive integers
    if b == 0:
        return a
    else:
        return a + multiplyRec(a, b - 1)


for i in range(11):
    print("multiplyRec({},{})={}".format(i, 5, multiplyRec(i, 5)))

"""# Power"""


def power(a, b):
    # assume that a,b are positive integers
    i = 1
    result = 1
    while i <= b:
        result *= a
        i += 1

    return result


for i in range(11):
    print("power({},{})={}".format(2, i, power(2, i)))


def powerRec(a, b):
    # assume that a,b are positive integers
    if b == 0:
        return 1
    else:
        return a * powerRec(a, b - 1)


for i in range(11):
    print("power({},{})={}".format(2, i, power(2, i)))

"""# Sum the odd numbers from 1 to n"""


def sumOdd(n):
    # assume that n is a positive integer
    i = 1
    result = 0
    while i <= n:
        if i % 2 != 0:
            result += i
        i += 1
    return result


for i in range(1, 11):
    print("sumOdd({})={}".format(i, sumOdd(i)))

print(sumOdd(2))


def sumOdd(n):
    # assume that n is a positive integer
    i = 1
    result = 0
    while i <= n:
        if i % 2 != 0:
            result += i
        i += 2

    return result


for i in range(1, 11):
    print("sumOdd({})={}".format(i, sumOdd(i)))


def sumOddRec(n):
    # assume that n is a positive integer
    if n == 1:
        return 1
    elif n % 2 == 0:
        return sumOddRec(n - 1)
    else:
        return n + sumOddRec(n - 2)


"""# Sum the elements of a list"""

data = [0, 10, 15, 20, -15, 20, 30]

print("data=", data)
print("data[-1]=", data[-1])

print("data[1:]=", data[1:])
print("data[:-1]=", data[:-1])
print("data[1:-1]=", data[1:-1])

print("data[5:]=", data[5:])
print("data[0:5]=", data[0:5])


def sumList(data):
    result = 0
    for x in data:
        result += x
    return result


data = [0, 5, 3, 2, 1]
print(sumList(data))


def sumListRec(data):
    if len(data) == 0:
        return 0
    else:
        return data[0] + sumListRec(data[1:])


print(sumListRec(data))

"""# Binary search

The list must be sorted.
"""

data = [8, -1, 5, 2, 0, 3]
data.sort()
print(data)


def binary_search(data, x):
    start = 0
    end = len(data) - 1
    while start <= end:
        m = (start + end) // 2

        if data[m] == x:
            return True
        elif data[m] > x:
            end = m - 1
        else:
            # data[m]<x
            start = m + 1

    return False


print("binary_search({},{})={}".format(data, -2, binary_search(data, -2)))
print("binary_search({},{})={}".format(data, 8, binary_search(data, 8)))
print("binary_search({},{})={}".format(data, 5, binary_search(data, 5)))
print("binary_search({},{})={}".format(data, 3, binary_search(data, 3)))


def binary_searchRec(data, x):
    if len(data) == 0:
        return False
    else:
        m = len(data) // 2
        if data[m] == x:
            return True
        elif x > data[m]:
            return binary_searchRec(data[m + 1:], x)
        else:
            return binary_searchRec(data[0:m], x)


print("binary_searchRec({},{})={}".format(data, -2, binary_searchRec(data, -2)))
print("binary_searchRec({},{})={}".format(data, 8, binary_searchRec(data, 8)))
print("binary_searchRec({},{})={}".format(data, 5, binary_searchRec(data, 5)))
print("binary_searchRec({},{})={}".format(data, 3, binary_searchRec(data, 3)))

"""# Reversing a python list

## Removing the first element
"""


def reverse(data):
    if len(data) == 0:
        pass
    else:
        x = data.pop(0)
        reverse(data[1:])
        data.append(x)


data = [8, -1, 5, 2, 0, 3]

print("original=", data)
reverse(data)
print("reverse=", data)

"""## Swapping the first and last elements"""


def reverse(data):
    if len(data) == 0:
        pass
    else:
        n = len(data) - 1
        temp = data[0]
        data[0] = data[n]
        data[n] = temp
        reverse(data[1:n])


data = [8, -1, 5, 2, 0, 3]

print("original=", data)
reverse(data)
print("reverse=", data)

"""# Binary Recursion"""


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


for i in range(30):
    # for i in range(30,40):
    print('fibo({})={}'.format(i, fibo(i)))


def fibo2(n):
    """returns the pair (a,b) where a=fibo(n) and b=fib(n-1)"""
    if n == 1:
        return (1, 0)
    else:
        (a, b) = fibo2(n - 1)
        return (a + b, a)


for i in range(10, 30):
    # for i in range(30,40):
    print('fibo2({})={}'.format(i, fibo2(i)))

"""# Binary sum List"""


def binarySumList(data):
    if len(data) == 0:
        return 0
    else:
        m = len(data) // 2
        return data[m] + binarySumList(data[0:m]) + binarySumList(data[m + 1:])


data = [8, -1, 5, 2, 0, 3]
print(binarySumList(data))
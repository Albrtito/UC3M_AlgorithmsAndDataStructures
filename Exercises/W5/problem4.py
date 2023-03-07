"""
Problem 4: Write a recursive method that takes a list of integers and checks if
the list is sorted(ascending order).
 For example if a=[3,4,5,2], checkSort(a)=False, a=[3,4,5,7],
 checkSort(a)=True
"""


def is_sorted_asc(n: list):
    if len(n) == 1:
        return True
    if len(n) == 2:
        return n[0] < n[1]
    return (n[0] < n[1]) and is_sorted_asc(n[1:])


n = [34,56,78,90]
print(is_sorted_asc(n))

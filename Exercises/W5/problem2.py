"""
Problem 2: Write a recursive method that determines if a string s is a palindrome, that is, it is
equal to its reverse. For example, racecar and gohangasalamiimalasagnahog are palindromes.
"""
import unittest


def is_palindrome(word: str):
    if len(word) <= 2:
        if word[0] == word[len(word) - 1]:
            return True
        else:
            return False
    elif len(word) == 1:
        return True

    return word[0] == word[len(word) - 1] and \
        is_palindrome(word[1:len(word) - 1])


class Test(unittest.TestCase):
    def setUp(self):
        # For list 1
        self.word1 = "gohangasalamiimalasagnaho"
        self.expected = True

        # Decide what to run
        self.testword = self.word1

    def test_1(self):
        # min elem of list 1
        result = is_palindrome(self.testword)
        self.assertEqual(str(self.expected), str(result))

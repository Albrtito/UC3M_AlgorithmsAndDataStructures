"""
Problem 1 – Balanced arithmetic expression.
Implement a Python class to guess if the delimiters (,),{,},[,] in an arithmetic expression
(e.j. [(5+x)-(y+z)]) are balanced.
● Correct expression example: ()(()){([()])}
● Incorrect expression example: ({[])}
Use a stack to implement your solution. Consider the following hints:
● If an opening symbol is found [,(,{ it must be pushed.
● If a closing symbol is found ],},) the element at the top of the stack must be
queried. If both symbols belong to the same type, the element must be removed.
● The arithmetic expression is balanced if at the end of the process the stack is
empty.
"""
"""
Basic idea: 
When evaluating the expression, 
+ if symbol that opens  -> Push it
+ if we find a symbol that closes the type of symbol that is last -> we pop it. 
    else: ERROR
    if the stack is empty -> ERROR
"""


# implement a stack with a class

class Stack:
    """LIFO Stack implementation using a Python list as storage.
    The top of the stack stored at the end of the list."""

    def __init__(self):
        """Create an empty stack"""
        self.items = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self.items)

    def isEmpty(self):
        """Return True if the stack is empty"""
        return len(self) == 0

    def __str__(self):
        # print the elements of the list
        return str(self.items)

    def push(self, e):
        """Add the element e to the top of the stack"""
        self.items.append(e)

    def pop(self):
        """Remove and return the element from the top of the stack"""
        if self.isEmpty():
            print('Error: Stack is empty')
            return None

        return self.items.pop()  # remove last item from the list

    def top(self):
        """Return the element from the top of the stack"""
        if self.isEmpty():
            print('Error: Stack is empty')
            return None

        # returns last element in the list
        return self.items[-1]


"""
The possible optimization in this function is mainly on the methods for checking if the symbol is opening, closing, type
etc. 
"""


def evaluate_expression(expression: str):
    s = Stack()

    def is_symbol(symbol: str):
        if symbol == "(" or symbol == "[" or symbol == "{" or symbol == ")" or symbol == "]" or symbol == "}":
            return True
        else:
            return False

    def symbol_state(symbol: str):
        if symbol == "(" or symbol == "[" or symbol == "{":
            return True
        elif symbol == ")" or symbol == "]" or symbol == "}":
            return False

    def symbol_type(symbol: str):
        if symbol == "(" or symbol == ")":
            return 1
        elif symbol == "[" or symbol == "]":
            return 2
        elif symbol == "{" or symbol == "}":
            return 3

    for i in expression:
        if is_symbol(i):
            print(s)
            # symbol state returns True if the symbol opens and False if it closes
            if symbol_state(i):
                s.push(i)
            if not symbol_state(i):
                if s.isEmpty():
                    raise ValueError("The expression is not valanced")
                # Symbol type returns the type of symbol: 1 for parenthesis 2 for squared brackets and 3 for brackets
                elif symbol_type(i) == symbol_type(s.top()):
                    s.pop()
                else:
                    raise ValueError("There is a closing symbol without its necessary opening symbol. No balance")
    if s.isEmpty():
        return True
    else:
        return False


expression = input("Enter expression: ")
if evaluate_expression(expression):
    print("The list is balanced")
else:
    print("The list is not balanced")

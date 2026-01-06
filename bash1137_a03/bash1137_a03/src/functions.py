"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from enum import Enum
from Stack_array import Stack


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = []
    target2 = []

    i = 1
    while not source.is_empty():
        if i % 2 != 0:
            target1.append(source.pop())
        else:
            target2.append(source.pop())
        i += 1
    return target1, target2


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    contents = []
    for element in source:
        contents.append(source.pop())

    for element in contents:
        source.push(element)

    return None


# Constants
OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()

    elements = string.split()

    for element in elements:
        if element in OPERATORS:
            right_operand = stack.pop()
            left_operand = stack.pop()

            if element == "+":
                stack.push(left_operand + right_operand)
            elif element == "-":
                stack.push(left_operand - right_operand)
            elif element == "*":
                stack.push(left_operand * right_operand)
            elif element == "/":
                stack.push(left_operand / right_operand)
        else:
            stack.push(float(element))

    answer = stack.pop()

    return answer


def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    stack = []
    values_out = []
    value_index = 0
    vaild = True

    for operation in opstring:
        if operation == "S":
            if value_index < len(values_in):
                stack.append(values_in[value_index])
                value_index += 1
            else:
                vaild = False
                break
        elif operation == "X":
            if stack:
                values_out.append(stack.pop())
            else:
                vaild = False
                break
        else:
            vaild = False
            break
    if not vaild:
        values_out = None

    return values_out

# Imports


# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"

    result = MIRRORED.IS_MIRRORED  # Default to IS_MIRRORED for now

    for char in string:
        if char != m and char not in valid_chars:
            result = MIRRORED.INVALID_CHAR
            break

    if result == MIRRORED.IS_MIRRORED:
        parts = string.split(m)

        if len(parts) != 2:
            result = MIRRORED.NOT_MIRRORED
        else:
            L, R = parts

            if len(L) > len(R):
                result = MIRRORED.TOO_MANY_LEFT
            elif len(R) > len(L):
                result = MIRRORED.TOO_MANY_RIGHT
            elif L != R[::-1]:
                result = MIRRORED.MISMATCHED

    return result

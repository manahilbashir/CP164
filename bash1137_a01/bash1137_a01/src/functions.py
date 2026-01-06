"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-10"
-------------------------------------------------------
"""


def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    new_list = []

    for each in minuend:

        if each not in subtrahend:
            new_list.append(each)

    minuend.clear()
    minuend.extend(new_list)

    return


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged:
    Do not strip() the lines.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    upp = 0
    low = 0
    dig = 0
    whi = 0
    rem = 0

    for line in fv:
        for char in line:
            if char.isupper():
                upp += 1
            elif char.islower():
                low += 1
            elif char.isdigit():
                dig += 1
            elif char.isspace():
                whi += 1
            else:
                rem += 1

    return upp, low, dig, whi, rem


def is_palindrome(string):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())

    return cleaned_string == cleaned_string[::-1]


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    rows = len(a)
    cols = len(a[0]) if a else 0

    transposed_matrix = [[a[j][i] for j in range(rows)] for i in range(cols)]

    return transposed_matrix


def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a. A 'flattened' list is a
    2D list that is converted into a 1D list.
    a must be unchanged.
    Use: b = matrix_flatten(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """
    flattened_list = []

    for sublist in a:
        for element in sublist:
            flattened_list.append(element)

    return flattened_list


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    if len(a[0]) != len(b):
        raise ValueError(
            "Matrices dimensions are incompatible for multiplication")
    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            c[i][j] = sum(a[i][k] * b[k][j] for k in range(len(b)))

    return c


def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    transposed_matrix = [[a[j][i]
                          for j in range(len(a))] for i in range(len(a[0]))]

    rotated_matrix = [row[::-1] for row in transposed_matrix]

    return rotated_matrix


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    pl = ""

    upper = False

    if word[0].isupper():
        upper = True
    if word[0] in vowels:
        pl += word + "way"
    else:
        vowels_AND_Y = ["a", "e", "i", "o", "u",
                        "A", "E", "I", "O", "U", "y", "Y"]
        c = []
        if word[0] == "y" or word[0] == "Y":
            word = word[1:] + word[0].lower()
        w = 0
        while word[w] not in vowels_AND_Y:
            c.append(word[w].lower())
            w += 1

        pl = word[len(c):]

        for i in c:
            pl += i

        pl += "ay"

    if upper:
        pl = pl[0].upper()+pl[1:]

    return pl


def substitute(string, ciphertext):
    """
    -------------------------------------------------------
    Encipher a string using the letter positions in ciphertext.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = substitute(string, ciphertext):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        ciphertext - ciphertext alphabet (str)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    substitution_dict = {chr(65 + i): ciphertext[i] for i in range(26)}

    estring = ""
    for char in string:
        if char.isalpha():
            uppercase_char = char.upper()
            if uppercase_char in substitution_dict:
                estring += substitution_dict[uppercase_char]
        else:
            estring += char

    return estring

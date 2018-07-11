#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW09 - Recursion
"""

__author__ = """ Jared Williams """
__collab__ = """ I worked on this assignment with Fidel Flores, using only this semester's course materials. """

"""
Function name: is_palindrome
Parameters: aStr (string)
Returns: True/False (bool)
Description: Write a function that takes in a String and return whether or not
it is a valid palindrome.

Hint: A palindrome is a word that is the same backwards as forwards.
"""
##############################
def is_palindrome(astring):
    if len(astring) == 1 or len(astring) == 0:
        return True
    a = astring[0]
    b = astring[-1]
    if a == b:
       return is_palindrome(astring[1:-1])
    else:
        return False
    
##############################

"""
Function name: matching_brackets
Parameters: aStr (string)
Returns: True/False (bool)
Description: Write a function called matching_brackets that takes in a String
and return whether or not it has matching brackets. (Hint: To have matching
brackets, every “(“, “{“ and “[“ must be matched with their corresponding “)”,
“}”, “]”)
"""
##############################
def matching_brackets(astring):
    if len(astring) == 0:
        return True
    a = astring[0]
    b = astring[-1]
    par = ["(",")"]
    bra = ["[","]"]
    curl = ["{","}"]
    if a in par and b in par:
        astring = astring[1:-1]
        return matching_brackets(astring)
    elif a in bra and b in bra:
        astring = astring[1:-1]
        return matching_brackets(astring)
    elif a in curl and b in curl:
        astring = astring[1:-1]
        return matching_brackets(astring)
    else:
        return False
    
##############################


"""
Function name: find_p_string
Parameters: aStr (string)
Returns: aStr (string)
Description: Given a string that contains a single pair of parenthesis, compute recursively
a new string made of only of the parenthesis and their contents. Return this
string.
"""
##############################
def find_p_string(astring):
    if astring[0] == "(" and astring[-1] == ")":
        return astring
    elif astring[0] == "(":
        return find_p_string(astring[:-1])
    elif astring[-1] == ")":
        return find_p_string(astring[1:])

    else:
        return find_p_string(astring[1:-1])
    
    ##############################

"""
Function name: fibonacci_dictionary
Parameters: aNum (int)
Returns: aDict (dict)
Description: Write a function that takes in an integer. Return a dictionary
whose keys are the entries in the fibonacci sequenece starting at 1 and up to
and including the number passed in and whose values are the fibonacci number
corresponding to the keys.
"""
##############################
def fibonacci_dictionary(num):
    adict = {}
    if num == 1:
        adict[1] = 1
        return adict
    if num == 2:
        adict[1] = 1
        adict[2] = 1
        return adict
       
    adict = fibonacci_dictionary(num-1)
    adict[num] = adict[num-1] + adict[num-2]
    return adict
##############################

"""
Function name: count_patterns
Parameters: aStr (string)
Returns: count (int)
Description: Write a function that takes in a String. The string will contain 0
or more patterns in the format "xAx" with a character surrounded by two
identical characters. Go through the String and determine how many patterns of
this format are found within.
"""
##############################
def count_patterns(astring):
    if len(astring) == 2:
        return 0
    if astring[0] == astring[2] and astring[0] != astring[1]:
        return 1 + count_patterns(astring[1:])
    else:
        return count_patterns(astring[1:])
    
##############################

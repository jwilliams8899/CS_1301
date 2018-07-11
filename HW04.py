#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW04 - Strings & Lists
"""
__author__ = """ Jared Williams """
__collab__ = """ I worked on this homework assignment alone, using this semester's course materials and referencing stackoverflow.com. """

"""
Function name: digits_space
Parameters: string
Returns: string
Description: Write a function that takes in a string. Create a new string that
contains single spaces instead of digits. Return the new string.

Note: You may not use python's built in replace function.
"""
##############################
def digits_space(string):
    new_str = ""
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    for letter in string:
        if letter in digits:
            new_str += " "
        else:
            new_str += letter
    return new_str
##def digits_space(string):
##    new_str = ""
##    digits = ["0","1",'2','3','4','5','6','7','8','9']
##    for letter in string:
##        if letter in digits:
##            new_str += " "
##        else:
##            new_str += letter
##    return new_str
##############################

"""
Function name: count_chars
Parameters: aStr (string), characters (string)
Returns: string
Description: Write a function that takes in two string parameters. Count the
total times the characters in the second string appear in the first string. The
format of the return statement must be: "The character(s) in  '(second
argument)' occur (# of times) times in '(value from first argument passed into
digits_space).'"

Note: The second parameter will only contain unique characters (it will not
contain duplicates).
"""
##############################
def count_chars(aStr,characters):
    count = 0
    for char in aStr:
        if char in characters:
            count += 1
    
    return "The character(s) in '{}' occur {} times in '{}'.".format(characters,count,aStr)
##############################

"""
Function name: multiple_index
Parameters: aStr (string), divisor (int), upper (int)
Returns: string
Description: Write a function that takes in three parameters: a string, a
divisor (an int), and an upper bound (an int). Determine what indeces of the
string are multiples of the divisor passed in and are less than or equal to the
upper bound. Construct a string using these indexes according to the format:
"(index1)(character1)(index2)(character2)...".

Note:
    (a) The upper bound is inclusive.
    (b) All parameters passed in for the divisor and upper bound will be
    positive integers.
"""
##############################
def multiple_index(aStr,divisor,upper):
    new_string = ""
    for index in range(len(aStr)):
        if index % divisor == 0 and index <= upper:
            new_string += str(index) + aStr[index]
    return new_string
##############################

"""
Function name: string_in_list
Parameters: string, list
Returns: boolean
Description: Write a function that takes in a string and a list of strings.
Return True if the string is in every element of the list and False otherwise.
"""
##############################
def string_in_list(string,list1):
    bools = []
    for element in list1:
        if string in element:
            bools += [True]
        else:
            return False
    if all(bools):
        return True
##############################

"""
Function name: common_list
Parameters: list, list
Returns: list
Description: Write a function that takes in two lists and returns a list that
contains elements that both lists share. The list that is returned should
contain the shared elements in the same order as they appear in the first list.
The returned list should contain no duplicates.
"""
##############################
def common_list(list1,list2):
    list_final = []
    for i in range(len(list1)):
        if list1[i] in list_final:
            pass
        elif list1[i] in list2:
            list_final += [list1[i]]
            
    return list(list_final)

##############################

"""
Function name: championship_teams
Parameters: list, int
Returns: list
Description: Write a function that takes in two parameters: a list and an int
that provides a lower bound. The list will be a nested list in which each
nested list will have the fomat: [team name (string), chance of winning (int),
sport (string)]. Your function must return a nested list that has the
"Football" and "Basketball" teams that have at least the minimum (second
parameter) chance of winning. However, the football teams must come before the
basketball teams, and each sport section must be alphabetically sorted.
"""
##############################

def championship_teams(list1,int1):
    list_football = [] 
    list_basketball = []
    return_list = []
    return_football = []
    return_basketball = []
    for element in list1:    
        if "Football" in element:
            list_football += [element]
    for element in list1:
        if "Basketball" in element:
            list_basketball += [element] 
    for element in list_football:
        for index in range(len(element)):
            if type(element[index]) == int:
                if element[index] >= int1:
                    return_football += [element[0]]
    return_football = sorted(return_football)
    for element in list_basketball:
        for index in range(len(element)):
            if type(element[index]) == int:
                if element[index] >= int1:
                    return_basketball += [element[0]]
    return_basketball = sorted(return_basketball)
    return_list = return_football + return_basketball
    return return_list
##############################

"""
Function name: string_split
Parameters: list
Returns: list
Description: Write a function that takes in a list and replace any entry that
is a string with a list that contains each character of the corresponding
string.

Note: You must return a modified list, not a new list (make changes to the list
passed in rather than creating a new one).
"""
##############################
def string_split(list1):
    for index in range(len(list1)):
        if type(list1[index]) == str:
            list1[index] = list(list1[index])
    return list1
##############################

"""
Function name: sort_types
Parameters: list
Returns: list
Description: Write a function that takes in a list containing values of several
different types (int, string, Boolean, float).  Create a new list that consists
of a set of sublists for each data type. Add each element in the original list
to its correct sublist based on type. In creating your list, keep in mind that
the order of sublists matters. The ints list should come first, strings list
should come second, floats list should come third, and Booleans list should
come fourth. Do not include empty sublists in your final list. Return the new
list.
"""
##############################
def sort_types(list1):
    list_int = []
    list_str = []
    list_float = []
    list_bool = []
    return_list = []
    for index in range(len(list1)):
        if type(list1[index]) == int:
            list_int += [list1[index]]
        elif type(list1[index]) == str:
            list_str += [list1[index]]
        elif type(list1[index]) == float:
            list_float += [list1[index]]
        elif type(list1[index]) == bool:
            list_bool += [list1[index]]
    if list_int != []:
        return_list.append(list_int)
    if list_str != []:
        return_list.append(list_str)
    if list_float != []:
        return_list.append(list_float)
    if list_bool != []:
        return_list.append(list_bool)
    
    return return_list
##############################

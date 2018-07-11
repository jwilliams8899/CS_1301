#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW05 - Tuples & Modules
"""

__author__ = " Jared Williams "
__collaboration__ = """ I worked on this homework assignment alone, using only this semester's resources. """


"""
Function name: cubeVolume
Parameters: tuple
Returns: tuple
Description: Write a function that accepts a tuple of dimensions  (length,
width, and height) for an object and returns a tuple with the volume and shape
of the object. Assume that the tuple will always contain three values (each of
which can be integers or floats). Given that the three values in the tuple each
represent the width, length, and height of a rectangular prism or cube, make a
new tuple that contains the volume. The volume should ALWAYS be a float (round
the volume to two decimal places if needed). If the object is a cube (the
width, length, and height are all equal), then add the word  "Cube" to the end
of the tuple. Otherwise, add the word "Rectangular Prism" to the end of the
tuple. Zero will never be given as a value in the tuple. Return the tuple that
you have created.
"""
##############################
def cubeVolume(tuple1):
    volume = 1
    for dimension in tuple1:
        volume *= dimension
    copy_tuple = tuple1[:]
    volume = float(round(volume,2))
    if all(index == tuple1[0] for index in tuple1): # also could have done: if len(set(tuple1))==1
        return (volume, 'Cube')
    else:
        return (volume, 'Rectangular Prism')
##############################

"""
Function name: beMyValentine
Parameters: list of tuples of booleans
Returns: tuple of booleans
Description: It's almost Valentine's day (even though it's over now) and
someone is looking for a date! Each tuple in the list passed in represents
someone who might potentially be free to go out on Valentine's day. Each tuple
contains Boolean values and if a tuple has two or more True values, then the
person represented by that tuple will be your valentine!

Return a tuple of Booleans that corresponds to whether or not each person
represented in the list will be your valentine.
"""
##############################
def beMyValentine(list1):
    true_count = 0
    dates = []
    for tuples in list1:
        for bools in tuples:
            if bools == True:
                true_count += 1
        if true_count == 2:
            dates.append(True)
        else:
            dates.append(False)
        true_count = 0
    return tuple(dates)
            
##############################

"""
Function name: passingMembers
Parameters: aList (list of lists of a tuple and a teamScore(int)), testScore
(int)
Returns: list of tuples of strings 
Description: It's an Olympic year and in order to celebrate, Georgia Tech is
holding a competition to find who the best test takers at the university are.
The list passed in is a nested list. Each nested list represents a team. Each
nested list contains a tuple that holds the names of the competitors on the
team as strings and the team's overall score (as an int). The first name in the
tuple is the team captain. The testScore (int) passed in represents the minimum
passing grade for the test.

Return a list of tuples that hold the name of the team captain and all of the
passing members on the team.

Members are only considered to be passing if their team's score is greater than
or equal to the minimum passing grade and the first letter of their name is the
same as the first letter of the ir team captain's name. Always include the team
captain's name if the team score is above the threshold. If a team doesn't meet
the requirements to pass, don't include any of the members of the team.
"""
##############################
def passingMembers(aList,testScore):
    passed_list = []
    passed_tuple = []
    final_list = []
    for lists in aList:
        #for tuples in range(len(lists[0])):
        if lists[1] >= testScore:
            passed_list.append(lists[0][0])
            for tuples in range(1,len(lists[0])):
                if (lists[0][tuples][0]) == (lists[0][0][0]): # if age matches
                    passed_list.append(lists[0][tuples])
        passed_tuple = tuple(passed_list)
        final_list.append(passed_tuple)
        passed_list = []
    for tups in final_list:
        if len(tups) == 0:
            final_list.remove(tups)
    return final_list
      
            
                
##############################

"""
Function name: removeVeggies
Parameters: recipeList (list of tuples of strings), veggieList (list of strings)
Returns: list of tuples of strings
Description: You're hired to create a menu for a birthday party, but at the
last minute you realize that it's for a 5-year-old baby who hates vegetables.
You are given recipeList which is a list of tuples. Each tuple represents a
dish and contains strings representing the ingredients of the dish. The second
parameter, veggieList, is a list of vegetables that the baby does not like. For
this function, go through the ingredients for each dish (tuple) and remove the
vegetables. Return a new list of tuples representing the modified dishes
without vegetables.
"""
##############################
def removeVeggies(recipeList, veggieList):
    new_recipe = []
    new_recipeList = []
    for tuples in recipeList:
        for tuple_index in range(len(tuples)):
            if tuples[tuple_index] not in veggieList:
                new_recipe.append(tuples[tuple_index])
        new_recipe_tups = tuple(new_recipe)
        new_recipeList.append(new_recipe_tups)
        new_recipe = []
    return new_recipeList
            
            
##############################

"""
Function name: hireTAs
Parameters: listOfTAs (list of tuples), newTAList(list of tuples)
Returns: listOfTAs (modified)
Description: We are hiring new TAs and we want to keep track of all TAs by
their age. The first parameter, listOfTAs, represents all the existing TAs and
is a list of tuples. The tuples are in the format of age (as an integer)
followed by the TAs that are that age (as strings). The second parameter,
newTAList, is of all the newly hired TAs, but the format is different. It is a
list of tuples, but each tuple contains only the age and the name of one TA
that is that age. There can be multiple tuples in this list that have the same
age. In this function, go through the list of newly hired TAs and add the names
to the end of the tuples in listOfTAs that have the same age. Do not make and
return a new list. Modify and return the existing listOfTAs.

Note: There will not be an age in newTAList that is not in listOfTAs so you do
not have to worry about that edge case.
"""
##############################
def hireTAs(listTAs,newTAs):
    add_list = []
    new_tup = ()
    for tuples in range(len(listTAs)):
        for tups in newTAs:
            if listTAs[tuples][0] == tups[0]:
                add_list.append(tups[1])
        listTAs[tuples] += tuple(add_list)
        add_list = []        
    return listTAs
        
                
            
                             
            
##############################

"""
Function name: simpleCalculator
Parameters: a (int), b (int), operation (string)
Returns: int
Description: Provided is a Python file (calculator.py) containing functions for
simple calculations. This function will take in an operation (as a string) that
will either be '+', '-', '*', or '/'. Depnding on the operation that is passed
in, call the appropriate function from the provided Python file and pass in the
a and b arguments as parameters to the function. Return the result of your
calculation. If you do not use the functions in calculator.py to solve this
function then you will not recieve credit for this function.
"""
##############################
import calculator
def simpleCalculator(a,b,op): # op = operation
    if op == '+':
        result = calculator.add(a,b)
    elif op == '-':
        result = calculator.subtract(a,b)
    elif op == '*':
        result = calculator.multiply(a,b)
    elif op == '/':
        result = calculator.divide(a,b)
    result = int(result)
    return result
    
    
##############################
















    

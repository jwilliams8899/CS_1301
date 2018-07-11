#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW03 - Conditionals & Iteration
"""
__author__ = """ Jared Williams """
__collab__ = """ I worked on this homework assignment alone, using only this semester's course materials. """

"""
Function name: outdoor_excursion
Parameters: temperature (int)
Returns: string
Description: Write a function that takes in a temperature as an int. If the
temperature value is less than 50, return the string "It's too cold to go
out!". If the temperature value is greater than 70, return the string
"Adventure time!". If the temperature value is between 50 and 70 (inclusive),
return the string "It's a beautiful day to go on an outdoor excursion!".
"""
##############################
def outdoor_excursion(temp):
    if temp < 50:
        return "It's too cold to go out!"
    elif temp >= 50 and temp <= 70:
        return "It's a beautiful day to go on an outdoor excursion!"
    else:
        return "Adventure time!"
##############################

"""
Function name: is_affordable
Parameters: animal type (str), price (int), quantity (int)
Returns: string
Description: Write a function that takes in an animal type as a string, an
animal price as as int, and an animal quantity as an int. Given these
parameters, determine whether or not you are willing to buy the quantity of the
animal type passed into the function based on the following criteria:
    (a) You will spend at least $5000 and no more than $15000.
    (b) If the price of the total number of animals you want to buy is below
    $5000,
    then return the string: "I need more animals!".
    (c) If price of the total number of animals you want to buy is above $15000,
    then return the string: "I won't buy (quantity) of the (animal type)(s).".
    (d) If the price of the total number of animals you want to buy
    is within your budget range (between $5000 and $15000 inclusive), return
    the string: "I will buy (quantity) of the (animal type)(s).".
"""
##############################
def is_affordable(animal, price, quantity):
    total = price * quantity
    if total < 5000:
        return "I need more animals!"
    elif total > 15000:
        return "I won't buy {} of the {}(s).".format(quantity,animal)
    else:
        return "I will buy {} of the {}(s).".format(quantity,animal)
##############################

"""
Function name: find_hotel
Parameters: distance1 (int), price1 (int), distance2 (int), price2 (int)
Returns: int (0, 1, or 2)
Description: Tiffany wants to travel to Amsterdam, but she is having trouble
finding a hotel. She ideally wants a hotel that is close to the city and is
cheap, but she is willing to stay farther the cheaper the hotel is and pay more
the closer the hotel is. Write a function that takes in four integer
parameters: the distance of hotel one from Amsterdam, the price of hotel one,
the distance of hotel two from Amsterdam, and the price of hotel two. Uset
these parameters to help Tiffany make her travel decisions. Tiffany has decided
the following:
    (a) if the hotel is at least 500 feet away, she will pay at most 20 dollars
    for the it
    (b) if the hotel is closer than 500 feet, she will pay at most 100 dollars
    (c) if there are no hotels that meet the above criteria, she is going to
    stay in an AirBnB

Your function should return:
(a) 1 if her best option is to stay in hotel one
(b) 2 if her best option is to stay in hotel two
(c) 0 if here best option is to stay in an AirBnB

If hotel one and hotel two are both valid options, return the hotel that is cheaper. You can assume that no two hotels will have the same price.
"""
##############################
def find_hotel(dist1, price1, dist2, price2):
    if dist1 >= 500 and price1 <= 20:
        hotel1 = price1
    elif dist1 < 500 and price1 <=100:
        hotel1 = price1
    else:
        hotel1 = False

    if dist2 >= 500 and price2 <= 20:
        hotel2 = price2
    elif dist2 < 500 and price2 <= 100:
        hotel2 = price2
    else:
        hotel2 = False

    if hotel1 == False and hotel2 == False:
        return 0

    if hotel1 == False and hotel2 != False:
        return 2
    elif hotel1 != False and hotel2 == False:
        return 1
    elif hotel1 != False and hotel2 != False:
        if hotel1 < hotel2:
            return 1
        elif hotel1 > hotel2:
            return 2
    
   
##############################

"""
Function name: multiples
Parameters: lower (int), upper (int)
Returns: the number of integers between the bounds that are a multiple of 3 and
not a multiple of 5 (int)
Description: Write a function that takes in a lower bound and an upper bound as
a parameter. Return the number of integers between the lower bound and the
upper bound (inclusive) that are a multiple of 3, but not a multiple of 5. You
can assume that the upper bound will always be greater than or equal to the
lower bound. You will not receive full credit unless you use a loop.
"""
##############################
def multiples(lower, upper):
    multiples = 0
    for number in range(lower,upper+1):
        if number % 3 == 0 and number % 5 != 0:
            multiples += 1
    return multiples
           
##############################

"""
Function name: strengthen_password
Parameters: password (str)
Returns: new password (str)
Description: This function takes in a password as a parameter. Write a function
that returns a new password with certain characters replaced. The characters
you will need to replace are in the table below along with the characters you
will replace them with (in the column labeled New Characters). You must replace
the characters on the left with the appropriate character from the right. You
may not use the replace() function. You will not receive full credit unless you
use a loop.
Characters: 1       ->  !
            a or A  ->  @
            e or E  ->  3
            o or O  ->  0
            s or S  ->  $
"""
##############################
def strengthen_password(password):
    password = list(password) # must convert string to a list because strings are immutable
    index = 0
    for letter in password:  #range(len(password)+1):
        if letter == "1":
            password[index] = "!"
            index +=1
        elif letter == "a" or letter == "A":
            password[index] = "@"
            index +=1
        elif letter == "e" or letter == "E":
            password[index] = "3"
            index +=1
        elif letter == "o" or letter == "O":
            password[index] = "0"
            index +=1
        elif letter == "s" or letter == "S":
            password[index] = "$"
            index +=1
        else:
            index += 1
    new_password = "".join(password)
    return new_password # return password with updated indices

##############################

"""
Function name: fibonacci_table
Parameters: length (int), width (int)
Returns: None
Description: Write a function that prints out the fibonacci sequence of
numbers in a table with dimensions based off of the length and width (passed in
as the parameters).  The table should have length rows and width columns. Use
the newline character (\n) to separate lines and the horizontal tab character
(\t) to separate the numbers. For the purposes of this assignment, we will
assume the fibonacci sequence starts at 1.
"""
##############################
def fibonacci_table(length, width):
    n = length * width
    count = 2
    prev = 1
    current = 1
    if width == 1 and length == 1:
        print(1,end="\t\n")
    elif width == 2 and length == 1:
        print(1,end="\t")
        print(1,end="\t\n")
    elif width == 1 and length == 2:
        print(1,end="\t\n")
        print(1,end="\t\n")
    elif width == 0 and length == 0: # fails on (0,0)
        #endchar = "\t\n"
        #print("")#end=endchar)
        print("",end="")
    elif width == 2:
            print(1,end="\t")
            print(1,end="\t\n")
    else:
            print(1,end="\t")
            print(1,end="\t")
    while count < n:
        count += 1
        aSum = prev + current
        if count % width == 0:
            #print(aSum,end="\t\n")
            endchar = "\t\n"
        else:
            endchar= "\t"
        #else:
            #print(aSum,end="\t")
        print(aSum, end=endchar)   
        prev = current
        current = aSum
        
    
##############################

"""
Function name: draw_snake
Parameters: length (int), width (int), distance (int)
Returns: None
Description: Write a function that takes in a length, width, and distance
between coils and prints a snake based off of those specifications. Make sure
the snake prints in the exact format as the examples below. There is one rule: a
snake cannot do its bend on either its head or tail end. Do not hardcode this
function. Use a for-loop.
"""
##############################
# How to account for tiny lengths

def draw_snake(length, width, distance):
    
    for i in range(length):
        printed_i = i % 10
        if i == 0:
            print("^")
        elif i == length-1:
            if distance == 1: # debuggin short snek
                print("v")
            elif i == distance:
                print("v")
            elif (i // distance) % 2 == 0: #checks if we're on the left side
                print("v")
            elif (i // distance) % 2 != 0: # checks if we're on the right
                print(" "*(width - 1) +"v")
            
        elif i % distance == 0:
            print(str(printed_i)*width)
            
        elif (i // distance) % 2 == 0: #checks if we're on the left side
                print(printed_i)
        elif (i // distance) % 2 != 0: # checks if we're onnt the right
                print(" "*(width - 1) + str(printed_i))
##        elif i == length - 1:
##                if (i // distance) % 2 == 0: #checks if we're on the left side
##                    print("v")
##                elif (i // distance) % 2 != 0:
##                    print(" "*width +"v")
##            


        
        
            
        
    













##############################

#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW02 - Parameters and Fruitful Functions
"""
__author__ = """ Jared Williams """
__collab__ = """ I worked on the homework assignment alone, and referred to stackoverflow.com for string formatting. """

"""
Function name: split_pizza
Parameters: number of pizzas (int), number of people (int)
Returns: None (NoneType)
Description: Write a function that takes in the number of pizzas ordered for a
party (int) and the number of people who will attend the party. Each pizza will
have exactly 8 slices and each person who attends the party must eat exactly
the same number slices (each person will eat the maximum amount of slices that
they can eat). Given this information, determine how many pieces of pizza each
person will eat at the party and how many pieces will be remaining at the end
of the party. Print out this information in the following format: "Each person
will eat (slices) slices with (remaining slices) slice(s) left over."
"""
##############################
def split_pizza(pizzas, people):
    total_slices = pizzas * 8
    slices_each = total_slices // people
    left_over = total_slices % people
    print("Each person will eat {} slices with {} slice(s) left over.".format(slices_each, left_over))
##############################

"""
Function name: how_many_pets
Parameters: dollars (int)
Returns: statement on pets user can buy (string)
Description: Write a function that takes in the amount of dollars available to
the user (as an integer). Next, calculate the amount of pets the user can buy,
given this amount of dollars. It costs $5 to buy a dog, $2 to buy a cat, and $1
to buy a bird. The user will buy as many dogs as possible, followed by as many
cats as possible, and will spend any left over money on buying birds. Return a
string informing the user about the amount of pets the user can buy in the
following format: "$(dollars) will buy you (dogs) dog(s), (cats) cat(s), and
(birds)  bird(s)."
"""
##############################
def how_many_pets(dollars):
    num_dogs = dollars // 5
    dollars_after_dogs = dollars % 5
    num_cats = dollars_after_dogs // 2
    dollars_after_cats = dollars_after_dogs % 2
    num_birds = dollars_after_cats
    return "${} will buy you {} dog(s), {} cat(s), and {} bird(s).".format(dollars, num_dogs, num_cats, num_birds)
##############################

"""
Function name: create_username
Parameters: name (str), animal (str), year (str)
Returns: username (str)
Description: Write a function that takes in a name as a string, an animal type
as a string, and a year as a string. Your job is to use these parameters to
create a username. The animal type will be the first element of the username,
the year will be the second element of the username, and the name will be the
third element of the username. Every element of the username should be
separated from the other elements by a dash ("-"). At the end of your function,
return the username (string) that you have created.
"""
##############################
def create_username(name, animal, year):
    username = animal + "-" + year + "-" + name
    return username
##############################

"""
Function name: help_user
Parameters: no parameters
Returns: username (str)
Description: Write a function that asks for the user's name, favorite animal,
and year of birth. Given this information, create a username for this user by
calling the function create_username that you have already written. Return this
username to the user.
"""
##############################
def help_user():
    name = input("What is your name? ")
    fav_animal = input("What is your favorite animal? ")
    year = input("What year were you born? ")
    assisted_username = create_username(name, fav_animal, year)
    return assisted_username
##############################

"""
Function name: sphere
Parameters: radius (float)
Returns: volume (float)
Description: Write a function that takes in the radius of a sphere as a float.
Return the volume of the sphere as a float rounded to 2 decimal places.
                        Volume of Sphere=  (4πr^3)/3
Note: Make sure you import the math module in order to get the value of pi
(like you did in HW01).
"""
##############################
import math
pi = math.pi
def sphere(radius):
    volume = round((4*pi*radius**3)/3, 2)
    return volume
##############################

"""
Function name: cube
Parameters: side length (float)
Returns: volume (float)
Description: Write a function that takes in one side of a cube as a float. Return the volume of the cube as a float rounded to 2 decimal places.
                        Volume of Cube= r^3
"""
##############################
def cube(length):
    volume = round(length**3, 2)
    return volume
##############################

"""
Function name: volume_difference
Parameters: radius (float), side length (float)
Returns: difference (float)
Description: Write a function that takes in the radius of a sphere as a float
and the side length of a cube as a float. Call the function sphere that you
have already written to find the volume of a sphere with a radius equal to the
one that was passed in. Call the function cube to find the volume of a cube with
side lengths equal to the one that was passed in. Then compute the difference
between these two volumes (volume of the sphere minus volume of the cube). At
the end of your function, return this difference rounded to 2 decimal places.
"""
##############################
def volume_difference(radius, length):
    vol_sphere = sphere(radius)
    vol_cube = cube(length)
    difference = vol_sphere - vol_cube
    return round(difference, 2)
##############################

"""
Function name: museum_tours
Parameters: no parameters
Returns: closing time (str)
Description: A museum has hired you to make a function that calculates the time
the museum will close for the day. The closing time for the museum is depednent
upon the number of tours that will take place that day and how long the average
tour is. Ask the user how many tours will take place in a day and how long the
average tour is (in minutes). Given this information, return a string
representation of the tours end time (which will be the museum's closing time)
in the following format: "__:___".  You may assume that tours start at 1:00 pm
and will not go later than 11:59 pm. You may also assume that the user will
only enter in integer values for number of tours and tour duration.

Note: Acceptable formatted return times include: "4:55", "9:00", "3:02".
Unacceptable formatted return times include: "04:55", "9: ", and "3:2". String
formatting will be helpful in making sure that your return time is formatted
correctly!
"""
##############################
def museum_tours():
    tours = int(input("How many tours will take place today? "))
    mins = int(input("How many minutes is the average tour? "))
    total_mins = tours * mins
    hour_of_closing = 1 + total_mins // 60   # total hours museum will be open
                                   # added to the tour start time of 1:00 pm
    mins_closing = total_mins % 60
    mins_closing = format(mins_closing, '02d') # formats single digits to have
                                           # a leading zero
    closing_time = "{}:{}".format(hour_of_closing, mins_closing)    
    return closing_time
##############################  Question: '02' vs '02d' formatting

#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Statements
"""
__author__ = """ Jared Williams """
__collab__ = """ I worked on this homework assignment alone, using only this semester's course materials. """
"""
Function name: income_tax
Parameters: no parameters
Return value: None
Description: Write a function that prompts a user to enter his / her gross
income. Then print out the user’s net income after tax in the format detailed
in the test cases below. For this function we will assume that tax is 22.5% for
everybody.
"""
##############################
def income_tax():
    gross = input("What is your gross income? ")
    gross_calc = float(gross)
    tax = .225
    net = round((gross_calc - (gross_calc * tax)), 2)
    print("With a gross income of ${}, your net income after tax is ${}.".format(gross, net))
##############################

"""
Function name: volume_of_sphere
Parameters: no parameters
Return value: None
Description: Write a function that asks the user for the radius of a sphere.
Print the volume of this sphere in the following format: "A sphere with a
radius of ____ has a volume of ____." . Round the answer to 3 decimal places.
You may assume that the user will always enter a positive number.
"""
##############################
import math
pi = math.pi
def volume_of_sphere():
    rad = input("What is the length of the radius of the sphere? ")
    rad_calculation = float(rad)
    vol = ((4/3)*(pi)*(rad_calculation**3))
    vol = round(vol, 3)
    print("A sphere with a radius of {} has a volume of {}.".format(rad, vol))
    
##############################

"""
Function name: calculate_bmi
Parameters: no parameters
Return value: None
Description: Write a function that asks the user a weight (lbs) and height (m),
and calculates the BMI for a person of the given specifications. Print out the
person’s BMI in a statement of the following format: "A person who weighs ____
kg and is ____ meters tall, will have a BMI of ____.". Please round the weight,
height, and BMI to 3 decimal places when you print out the final string (DO NOT
round before BMI calculation). You may assume all inputs will be positive.
"""
##############################
def calculate_bmi():
    lbs = input("What is the person's weight (in lbs)? ")
    met = input("What is the person's height (in m)? ")
    lbs_calc = float(lbs)
    kg = lbs_calc*0.453592
    met_calc = float(met)
    bmi = round((kg/(met_calc**2)), 3)
    kg_round = round(kg, 3)
    met_round = round(met_calc, 3)
    print("A person who weighs {} kg and is {} meters tall, will have a BMI of {}.".format(kg_round, met_round, bmi))
##############################

"""
Function name: fitness_freak
Parameters: no parameters
Return value: None
Description: Write a function that asks the user for the number of meals the
user eats in a day, the number of miles the user runs in a day, and the number
of laps the user swims in a day. Given this information, print the net calorie
intake for that user in the following format: "A person who eats ____ meals,
runs ____ miles, and swims ____ laps has a calorie count of ____ calories.".
You may assume the user will always provide positive integers.
"""
##############################
def fitness_freak():
    meals = input("How many meals did you eat today? ")
    miles = input("How many miles did you run today? ")
    laps = input("How many laps did you swim today? ")
    meals_calc = int(meals)
    miles_calc = int(miles)
    laps_calc = int(laps)
    cal_count = (meals_calc*500) - (miles_calc*95) - (laps_calc*10)
    print("A person who eats {} meals, runs {} miles, and swims {} laps has a calorie count of {} calories.".format(meals, miles, laps, cal_count))
##############################

"""
Function name: make_cents
Parameters: no parameters
Return value: None
Description: Write a function that that asks the user for a dollar amount as a
float and converts this amount to the equivalent number of quarters, dimes,
nickels and pennies. Print the number of quarters, dimes, nickels, and pennies
in the following format: "____ is equivalent to ____ quarter(s), ____ dime(s),
____ nickel(s), and ____ pennies.". You may assume that the number of dollars
passed in will always be positive.
"""
##############################
def make_cents():
    dollars = input("What is the dollar amount? ")
    dollars_calc = float(dollars)
    cents = dollars_calc*100
    quarters = cents // 25
    after_quarters = cents % 25
    dimes = after_quarters // 10
    after_dimes = after_quarters % 10
    nickels = after_dimes // 5
    after_nickels = after_dimes % 5
    pennies = after_nickels
    print("${} is equivalent to {} quarter(s), {} dime(s), {} nickel(s), and {} pennies.".format(dollars, quarters, dimes, nickels, pennies))
##############################

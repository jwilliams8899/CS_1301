#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW07 - Dictionaries
"""
__author__ = """ Jared Williams """
__collaboration__ = """ I worked on this assignment alone, using only this semester's course materials. """

"""
Function name: total_in_stock
Parameters: list of tuples (format of tuples: ("name", quantity))
Returns: dictionary mapping items (as strings) to total quantity of those items
in stock (as ints)
Description: You own a coffee shop. Every morning you need to go to the grocery
store to buy items to make pastries and coffee drinks, and you must take
inventory of the items that you buy. Write a function called total_in_stock
that takes in a list of tuples. Each tuple will contain the name of an item (as
a string) and the quantity of those items purchased (as an int). Return a
dictionary whose keys are the names of the items and whose values are
the total amount of that item purchased. If an item appears more than once in
your list, then the value associated with that item will be the total sum of
all the items of that type purchased.
"""
##############################
def total_in_stock(tups):
    dictionary = {}
    for tup in tups:
        if tup[0] in dictionary.keys():
            dictionary[tup[0]] = dictionary[tup[0]] + int(tup[1])
        else:
            dictionary[tup[0]] = int(tup[1])
    return dictionary
##############################

"""
Function name: smoothies
Parameters: dictionary whose keys are names of fruits (as strings) and whose
values are lists of months (as strings)
Returns: month in which the most fruits are available (string)
Description: You have decided to start selling smoothies at your coffee shop
and want to know which month is best for buying freshly harvested fruit. Write
a function called smoothies that takes in a dictionary whose keys are fruits'
names and whose values are lists of the months in which the respective fruits
are harvested. Return the month which has the most fruits available for harvest.

Note: If there is a tie, return the month that occurs earliest in the year
(e.g. January is the month that occurs earliest in the year, followed by
February, etc.)."""
##############################
def smoothies(dict1):
    dictionary = {}
    return_list = []
    return_months = []
    return_key = []
    month_dict = {'January':12, 'February':11, 'March':10, 'April':9, 'May':8, 'June':7, 'July':6, 'August':5, 'September':4, 'October':3, 'November':2, 'December':1}
    for key in dict1.keys():
        list1 = dict1[key]
        for month in set(list1):
            if month in dictionary.keys():
                dictionary[month] = dictionary[month] + 1
            else:
                dictionary[month] = 1
    productivity = []
    months = ()
    for key in dictionary.keys():
        months += (key,)
        productivity.append(dictionary[key])
    max_prod = max(productivity)
    for key in dictionary.keys():
        if dictionary[key] == max_prod:
            return_months.append(key)
            return_key.append(month_dict[key])
    earliest_month = max(return_key)
    month_index = return_key.index(earliest_month)
    return months[month_index]
    
    
    
    
        
##############################

"""
Function name: worker_average
Parameters: dictionary whose keys are the names of the workers at your coffee
shop (as strings) and whose values are dictionaries with key value pairs
representing the worker's age, hours worked per week, and wage
Returns: dictionary containing the average age, average hours worked per week,
and average wage of the workers whose names start with consonants
Description: For an upcoming monthly report about your employees, you need to
find the average ages, average hours worked per week, and average wages of your
employees. Write a function called worker_average that takes in a dictionary
whose keys are the names of the workers at your coffee and whose values are
dictionaries containing a worker's age, hours worked per week, and wage. Return
a dictionary containing the average age (as an int), average hours per week (as
an int), and average wage (as a float) of the workers whose names start with
consonants. The keys in this dictionary must be 'age', 'hours per week', and
'wage'. Round the average wage to two decimal places. If none of the workers
have names that start with consonants, return an empty dictionary.
"""
##############################
def  worker_average(workers):
    return_dict = {}
    vowels = ['A','a','E','e','I','i','O','o','U','u']
    count = 0
    ages = 0
    hours = 0
    wage = 0
    vowel_scum = 0
    num_names = len(workers.keys())
    for name in workers.keys():
        if name[0] not in vowels:
            count += 1
            data_dict = workers[name]
            ages = ages + data_dict['age']
            avg_age = round(ages/count,2)
            hours = hours + data_dict['hours per week']
            avg_hours = round(hours/count,2)
            wage = wage + data_dict['wage']
            avg_wage = round(wage/count,2)
            return_dict['age'] = avg_age
            return_dict['hours per week'] = avg_hours
            return_dict['wage'] = avg_wage
        else:
            vowel_scum += 1
    if vowel_scum == num_names:
        return {}
    else:
        return return_dict
            
##############################

"""
Function name: cashier
Parameters:  dictionary whose keys are customer names (as strings) and whose
values are lists of food items (as strings), dictionary whose keys are food
items (as strings) and whose values are prices (as floats), whether or not the
teams are paying together (as a Boolean - True if yes, False if no)
Returns: dictionary whose keys are strings of the customers' names (or whose
key is "Total" if the teams are paying together) and whose values are their
payments (or the total payment if the teams are paying together)
Description: Your coffee shop needs a way to calculate prices. Write a function
that takes in a dictionary whose keys are customer names and whose values are
lists of items ordered, a dictionary whose keys are the names of food items and
whose values are the costs of the food items, and a boolean that is True when
the customers are paying together and False when they are paying separately.
The function should return a dictionary with a key for each customer and with
values that are the customer's total order cost as the value if they are paying
separately, or a dictionary whose only key is "Total" with a value that is the
sum of everything that the customers ordered.

Note: You can assume that food items will be spelled the same way and in the
same case (upper / lower) in both dictionaries.
"""
##############################
def cashier(dict1,dict2, booly):
    return_dict = {}
    if booly == False:
        for key1 in dict1.keys():
            order = dict1[key1]
            price = 0
            for item in order:
                price += dict2[item]
            return_dict[key1] = price
        return return_dict
    else:
        price = 0
        for key1 in dict1.keys():
            order = dict1[key1]
            for item in order:
                price += dict2[item]
        return_dict["Total"] = price
        return return_dict
        
##############################



"""
Function name: allergy
Parameters: file name (string), allergies list (list of strings), and
order_string (string containing the food item that was ordered and its
ingredients)
Returns: string containing the correct ingredients (see format below)
Description: Sometimes customers would like to order items specially made
without ingredients that they're allergic to. Write a function that takes in a
file name (as a string), a list of strings representing allergies, and a string
of a describing a food's ingredients. Read the file and turn each line into a
key-value pair in a dictionary. Then make ingredient replacements in the string
based off of this dictionary. Return a string that has all of the ingredients
the customer is allergic to replaced with the substitutions given in the file
(see "substitutions.txt").

Note: You can assume each allergy item will only have one substitution. These
will always be separated by a comma followed by one space. You may use
.replace() in this function.
"""
##############################
def allergy(filename,allergies,string):
    f = open(filename,'r')
    f_list = f.readlines()
    f.close()
    replacements = {}
    for strings in f_list:
        string_list = strings.split(',')
        allergen = string_list[0]
        substitute = string_list[1].strip()
        replacements[allergen] = substitute
    if len(allergies) == 0:
        return string
    for allergens in allergies:
        if allergens in string:
            new_string = string.replace(allergens,replacements[allergens])
            string = new_string
    return string    
##############################

"""
Function name: drink_locations
Parameters: dictionary whose keys are restaurants (as strings) and whose values
are lists of the drinks that the restaurants serve (lists of strings)
Returns: a dictionary whose keys are drinks (as strings) and whose values are
lists of restaurants that serve that drink (lists of strings)
Description: You are trying to find the locations that serve your favorite
drinks, but you only have the restaurant names and respective menus. Write a
function called drink_locations that takes in a dictionary whose keys are
restaurant names and whose values are lists of the drinks that they serve.
Return a dictionary whose keys are drinks and whose values are lists of
restaurants that serve that drink. The restaurants should be in alphabetical
order, and restaurant names should occur at most once in each list.
"""
##############################
##def drink_locations(dict1):
##    return_dict = {}
##    places = []
##    for key in dict1.keys():
##        for drink in dict1[key]:
##            places.append(key)
##            return_dict[drink] = sorted(set(places))
##    for keys in return_dict.keys():
##        for place in return_dict[keys]:
##            for key in dict1.keys():
##                if keys not in dict1[key]:
##                    index = place.index(place)
##                    del return_dict[keys][index]
##    return return_dict






def drink_locations(dict1):
    return_dict = {}
    places = list(dict1.keys())
    place_list = []
    for key,value in dict1.items():
        for drink in value:
            return_dict[drink] = sorted(set(places))
            
    for keys in return_dict.keys():
        for places in dict1.keys():
            if keys not in dict1[places]:
                index = return_dict[keys].index(places)
                del return_dict[keys][index]
    return return_dict

##def drink_locations(dict1):
##    return_dict = {}
##    values = []
##    keys = []
##    for key in dict1.keys():
##        values.append(key)
##        values.sort()
##        for drinks in dict1[key]:
##            keys.append(drinks)
##    keys = set(keys)
##    new_values = []
##    keys = list(keys) # list of drinks
##    for new_key in keys:
##        #print(new_key)
##        for key in dict1.keys():
##            #print(key)
##            #print(dict1[key])
##            if new_key in dict1[key]:
##                new_values.append(key)
##        return_dict[new_key] = new_values
##    return return_dict
##    










    
    
##############################

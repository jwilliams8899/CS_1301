#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW06 - File I/O
"""

__author__ = "Jared Williams"
__collaboration__ = """ I worked on this assignment alone, using only this semester's course materials. """

"""
Function name: get_roster
Parameters: file_name (str)
Return value:  roster (list)
Description: Read in a file (that has the same format shown above). Generate a list with every student's name. Make sure the names do not contain newline characters (\n) and are in the order they appear in the file. Assume the passed in filename is a valid file.
"""
##############################
def get_roster(file_name):
    file = open(file_name,'r')
    roster = []
    for f in file:
        if "Test" not in f and f != "\n":
            roster.append(f.strip('\n'))
    file.close()
    return roster

##def get_roster(file_name):
##    file = open(file_name,'r')
##    roster = []
##    file_list = file.readlines()
##    for lines in file_list:
##        if "Test" not in lines and lines != '\n':
##            roster.append(lines.strip('\n'))
##    return roster
##    file.close()  
##############################

"""
Function name: tests_missed
Parameters: file_name (str)
Return value: tests_missed (list)
Description: Read in a file that has the format specified at the beginning of this section. For each DNT score, add the test number of that score to a list. Return the list at the end. The order of tests should be the same order as the DNT scores that are encountered. If multiple people did not take the same test (tests with the same number), the test number should be included in the list multiple times. Assume the passed in filename is a valid file.
"""
##############################
def tests_missed(file_name):
    file = open(file_name,'r')
    tests_missed = []
    file_list = file.readlines()
    for line in file_list:
        line = list(line.split()) # why is split doing this way
        if "DNT" in line:
            tests_missed.append(int(line[1].strip(':')))
    file.close()
    return tests_missed
    
    
##############################

"""
Function name: choose_group
Parameters: aList(str), num (int), filename (str)
Return value:  Boolean (True or False)
Description: Write a function that takes in a list of student names. You will form a group of size num from the group of names. You will choose the last num students in the list. You will write out the names of the students who will form the group to the file sepcified by the filename passed in. This will be the format:

Team: [Name1], [Name2], [NameNum]
If there are not enough students for a group, write 'Not enough people for a group.' to the file. If there are zero people on a team then leave the file empty. Finally, return True if there are enough people to form a group and False otherwise.
Note: In regards to formatting, the file will only be one line no matter how many names there are so it should contain no newline characters ('\n'). Additionally, write the names in reverse order to the list passed in (see test cases for clarification).
"""
##############################
def choose_group(aList, num, filename):
    file = open(filename,'w')
    group_members = []
    if len(aList) < num:
        file.write("Not enough people for a group.")
        file.close()
        return False
    elif num == 0:
        file.close()
        return False
    else:
        for i in reversed(aList[len(aList)-num:len(aList)]): # reversed() gives a reversed string of the list
            group_members.append(i)
        file.write("Team: " + ", ".join(group_members)) # joining a list turns it into a string
        file.close()
        return True
    
    
##############################

"""
Function name: max_volume
Parameters: stock (string)
Return value: date (string)

Description: Define a function that takes in the name of a stock as a string. Read from the provided file "all_stocks.csv" and determine the date on which the stock has the maximum volume. Return this date as a string in the format  "yyyy-mm-dd". If there is a tie for maximum volume, return the most recent date.
"""
##############################
def max_volume(stock):
    file = open('all_stocks.csv','r')
    file_list = file.readlines()
    volume = 0
    for info in file_list:
        info = info.split(',')
        if info[6].strip('\n') == stock:
            if float(info[5]) >= float(volume):
                volume = float(info[5])
                date = info[0]
    file.close()
    return date
##############################

"""

Function name: stock_average
Parameters: year (int), stocks (list of strings)
Return value: None (NoneType)
Description: Write a function that takes in a year as an int and a list of stock names as strings. For the given year, find the average open price for each stock (using the file "all_stocks.csv"). Then write the stocks and their respective average open prices for that year into a new file called "opening_price.txt" in ascending order (by price). The first stock in "opening_price.txt" should be the stock with the lowest average open price. The "opening_price.txt" file should be formatted as follows:

1. [Stock Name]
	[Average open price]
2. [Stock Name]
	[Average open price]
"""
##############################
def stock_average(year,stocks):
    file = open('all_stocks.csv')
    file_list = file.readlines()
    avg_list = []
    for names in stocks:
        count = 0
        open_price = 0
        for info in file_list:
            info = info.split(',')
            if info[6].strip('\n') == names:
                if int(info[0][0:4]) == year:
                    count += 1
                    open_price += float(info[1])
                    average = round((open_price)/count,3)
        avg_list.append((average,names)) # average is an int
    avg_list = sorted(avg_list)
    f = open('opening_prices.txt','w')
    for tups in range(len(avg_list)):
        f.write(str(tups+1) + '. ' + avg_list[tups][1] + '\n')
        f.write('\t' + str(avg_list[tups][0]) + '\n')
    f.close()
    return None
##############################

#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW10 - Recursion
"""

__author__ = """ Jared Williams """
__collab__ = """ I worked on this assignment alone, using only this semester's course materials. """


class Restaurant:

    """
    Write a constructor (__init__ method) for a Restaurant below.
    It should have the following attributes:
        name (string)
        priceRange (tuple)
        foodType (string)
        rating (float)

    The function header has been given to you below.
    """
    def __init__(self, name, priceRange, foodType, rating=0.0):
        self.name = name
        self.priceRange = priceRange
        self.foodType = foodType
        self.rating = rating

    """
    Function name: __str__
    Return a string representation of a Restaurant.
    """
    ##############################
    def __str__(self):
        if self.rating != 0.0:
            return "A Restaurant named {}, serving {}, with a price range of {}-{} has a rating of {}.".format(self.name,self.foodType,self.priceRange[0],self.priceRange[1],self.rating)
        elif self.rating == 0.0:
            return "A Restaurant named {}, serving {}, with a price range of {}-{}, currently has no rating.".format(self.name,self.foodType,self.priceRange[0],self.priceRange[1])
        
    ##############################

    """
    Function name: make_food
    Return the dish that the patron should order.
    """
    ##############################
    def make_food(self, dishes, patron):
        if len(patron.name) > len(dishes):
            index = len(patron.name) % len(dishes)
        else:
            index = len(patron.name)
        return dishes[index]
    ##############################

    """
    Function name: sponsor
    Return the name of the best sponsor (based on criteria outlined in PDF) for
    the Restaurant.
    """
    ##############################
    def sponsor(self, patronList):
        exp = []
        food_types = []
        fav_food = self.foodType
        for patron in patronList:
            exp.append(patron.experienceLevel)
            food_types.append(patron.favoriteTypeOfFood)
        highest_exp = patronList[exp.index(max(exp))]
        # highest experience level^
        
        if fav_food not in food_types:
            return highest_exp.name
        else:
            preferred = []
            count = 0
            for food in food_types:
                if food == fav_food:
                    preferred.append(patronList[count])
                count += 1 #### should fix
            exp_preferred = []
            for yelper in preferred:
                exp_preferred.append(yelper.experienceLevel)
            ratings = []
            for yelper in preferred:
                ratings.append(yelper.numberOfRatings)
            
            most_ratings = preferred[ratings.index(max(ratings))]
            
            most_exp = preferred[exp_preferred.index(max(exp_preferred))]
            if exp_preferred.count(max(exp_preferred)) > 1:
                return most_ratings.name
            else:
                return most_exp.name
            

    ##############################


class YelpElite:

    """
    Write a constructor (__init__ method) for a YelpElite below.
    It should have the following attributes:
        name (string)
        experienceLevel (int)
        numberOfRatings (int)
        favoriteTypeOfFood (string)

    The function header has been given to you below.
    """
    def __init__(self, name, experienceLevel, numberOfRatings, favoriteTypeOfFood=None):
        self.name = name
        self.experienceLevel = experienceLevel
        self.numberOfRatings = numberOfRatings
        self.favoriteTypeOfFood = favoriteTypeOfFood

    """
    Function name: __str__
    Return a string representation of a YelpElite.
    """
    ##############################
    def __str__(self):
        if self.favoriteTypeOfFood != None:
            return "A YelpElite named {} loves {} food, has written {} reviews, and has an experience level of {}.".format(self.name,self.favoriteTypeOfFood,self.numberOfRatings,self.experienceLevel)
        else:
            return "A YelpElite named {} has written {} reviews, and has an experience level of {}.".format(self.name,self.numberOfRatings,self.experienceLevel)
    ##############################

    """
    Function name: review
    Update the restaurants rating and the YelpElites numberOfRatings
    attributes given a review by the YelpElite (passed in as a string) about the
    Restaurant  (passed in as a Restaurant).
    """
    ##############################
    def review(self, restaurant, review):
        if "Okay" in review:
            new_rating = 3
        elif "Good" in review:
            new_rating = 4
        elif "Great" in review:
            new_rating = 4.5
        elif "Fantastic" in review:
            new_rating = 5
            
        exp = self.experienceLevel
        numRatings = self.numberOfRatings
        cur_rating = restaurant.rating

        offset = abs(cur_rating - new_rating) * (exp/10) * (numRatings/1000)

        if new_rating < cur_rating:
            cur_rating -= offset
            restaurant.rating = round(cur_rating,2)
            if restaurant.rating > 5.0:
                restaurant.rating = 5.0
        elif new_rating > cur_rating:
            cur_rating += offset
            restaurant.rating = round(cur_rating,2)
            if restaurant.rating > 5.0:
                restaurant.rating = 5.0
                
        self.numberOfRatings += 1
        
    ##############################

    """
    Function name: recommend
    Return the name of the restaurant from the list of Restaurants passed in
    that the YelpElite recommends (based on criteria specified in the PDF).
    """
    ##############################
    def recommend(self, restaurants, person):
        ratings = []
        food_types = []
        fav_food = person.favoriteTypeOfFood
        for restaurant in restaurants:
            ratings.append(restaurant.rating)
            food_types.append(restaurant.foodType)
        highest_rated = restaurants[ratings.index(max(ratings))]
        # highest rated restaurant^
        
        if fav_food not in food_types:
            return highest_rated.name
        else:
            preferred = []
            count = 0
            for food in food_types:
                if food == fav_food:
                    preferred.append(restaurants[count])
                count += 1
            ratings_preferred = []
            for place in preferred:
                ratings_preferred.append(place.rating)
            best_place = preferred[ratings_preferred.index(max(ratings_preferred))]
            return best_place.name
            
            
        
    ##############################

class AverageJoe:

    """
    Write a constructor (__init__ method) for an AverageJoe below.
    It should have the following attributes:
        name (string)
        bankAccount (int)
        favoriteTypeOfFood (string)

    The function header has been given to you below.
    """
    def __init__(self, name, bankAccount, favoriteTypeOfFood=None):
        self.name = name
        self.bankAccount = bankAccount
        self.favoriteTypeOfFood = favoriteTypeOfFood

    """
    Function name: __str__
    Return a string representation of an AverageJoe.
    """
    ##############################
    def __str__(self):
        if self.favoriteTypeOfFood != None:
           return "An AverageJoe named {} loves {} food, and has {} dollars in the bank.".format(self.name,self.favoriteTypeOfFood,self.bankAccount)
        else:
            return "An AverageJoe named {} has {} dollars in the bank.".format(self.name,self.bankAccount)
    ##############################

    """
    Function name: eat_out
    Return a list of boolean values representing whether or not the AverageJoe 
    can eat at the Restaurant corresponding to the index of a given 
    boolean in the list of Restaurants passed in.
    """
    ##############################
    def eat_out(self, restaurants):
        return_list = []
        half = self.bankAccount/2  # half of the bank account
        quarter = self.bankAccount/4  # 1/4 of the bank account
        fav_food = self.favoriteTypeOfFood
        for restaurant in restaurants:
            if restaurant.priceRange[1] < half and restaurant.priceRange[1] > quarter and restaurant.foodType == fav_food:
                return_list.append(True)
            elif restaurant.priceRange[1] <= quarter or restaurant.priceRange[1] == self.bankAccount:
                return_list.append(True)
            else:
                return_list.append(False)
        return return_list
    ##############################

    """
    Function name: review
    Update the passed in restaurant's ratings given the rating passed in.
    """
    ##############################
    def review(self, restaurant, rating):
        fav_food = self.favoriteTypeOfFood
        if restaurant.foodType == fav_food:
            factor = .005
        else:
            factor = .002
        change = rating * factor
        if rating < restaurant.rating:
            restaurant.rating -= change
            restaurant.rating = round(restaurant.rating,2)
            if restaurant.rating > 5.0:
                restaurant.rating = 5.0
        elif rating > restaurant.rating:
            restaurant.rating += change
            restaurant.rating = round(restaurant.rating,2)
            if restaurant.rating > 5.0:
                restaurant.rating = 5.0





    ##############################


















#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW08 - API and Requests Module
"""

import requests
import random

__author__ = """ Jared Williams """
__collab__ = """ I worked on this assigment alone, using only this semester's course materials """

base_url = "https://pokeapi.co/api/v2/"

"""
Function name: moves
Parameters: pokémon (returned dict by GET api/v2/pokemon/{id or name})
Returns: move_list (list of dictionaries that represent each move)
Description: Every pokémon has a certain move set that it can use in battle.
Write a function that takes in a pokémon. This function should return a list
that contains a dictionary of information for EACH of the first 5 moves listed
as the pokemon’s moves. The keys in each dictionary should be "id", "name",
"type", and "power". The values at each key must match the values at each key
in the dictionary returned when using a get request on a move’s url. Note that
this information should pertain to the MOVE, not the Pokémon.

Hints: Look at the dictionary representation of a pokémon in the APIs
documentation. Look also at the dictionary representation of a move in the APIs
documentation.
"""
##############################
def moves(pokemon):
    moves_list = []
    for move in range(5):
        url = pokemon['moves'][move]['move']['url']
        result = requests.get(url)
        move_dict = result.json()
        myid = move_dict['id']
        myname = move_dict['name']
        mytype = move_dict['type']
        mypower = move_dict['power']
        new_dict = {}
        new_dict['id'] = myid
        new_dict['name'] = myname
        new_dict['type'] = mytype
        new_dict['power'] = mypower
        moves_list.append(new_dict)
    return moves_list

##from pprint import pprint
##result = requests.get("https://pokeapi.co/api/v2/pokemon/1")
##bulbasaur = result.json()
##pprint(moves(bulbasaur))
##############################

"""
Function name: team_builder
Parameters: trainer’s name (str), pokémon ids (list of ints)
Returns: dictionary representation of a team
Description: Every aspiring pokémon trainer must start with a good team! Write
a function that takes in the trainer’s name as a string and a list of pokémon
ids as a list of ints. The function should return a dictionary with three
key-value pairs. The first key should be the string "trainer" with the
trainer’s name as the value. The second key should be the string "pokemon" with
a value that is a list of dictionaries as shown in the graphic below.  Note
that the only pokémon that should be added to this list are the ones whose
name’s first letter matches the trainer’s name’s first letter. The list should
contain one dictionary of information PER pokémon that matches this criteria.
The third key is the string "active_pokemon", whose value is the int zero by
default. The value at the key "active_pokemon" represents the index (into the
list at the key "pokemon") of the pokémon that is currently battling. It starts
at 0 because a battle always begins with the pokémon that is first it the
trainer’s list of pokémons.
"""
##############################
def team_builder(trainer,ids):
    team = {}
    team["trainer"] = trainer
    pokemon_list = []
    for ints in ids:
        url = base_url + 'pokemon/' + str(ints)
        result = requests.get(url)
        poke_dict = result.json()
        if poke_dict['name'][0].lower() == trainer[0].lower():
            myname = poke_dict['name']
            myid = poke_dict['id']
            stat_dict = {}
            for stat in poke_dict['stats']:
                mybasestat = stat['base_stat']
                mystatname = stat['stat']['name']
                stat_dict[mystatname] = mybasestat
            types_list = []
            for type_ in poke_dict['types']:
                mytype = type_['type']['name']
                types_list.append(mytype)
            info_dict = {}
            info_dict['name'] = myname
            info_dict['id'] = myid
            info_dict['stats'] = stat_dict
            info_dict['types'] = types_list
            info_dict['moves'] = moves(poke_dict)
            pokemon_list.append(info_dict)
    team["pokemon"] = pokemon_list
    team["active_pokemon"] = 0
    return team

##from pprint import pprint
##pprint(team_builder("Jack", [255,135,385]))

##############################

"""
Function name: modifier
Parameters: attacker (dict), defender (dict), move (dict)  (NOTE: attacker and
defender follow the same format as the pokémon from team_builder(), and move
follows the same format as one of the dictionaries in the list that moves()
returns)
Returns: (STAB, type_bonus) (tuple with elements of the following types:
(float, float))
Description: Not all attacks do the same damage! Write a function that takes in
a dictionary of the attacker’s pokémon, a dictionary of the defender’s pokémon,
and a dictionary of the information for the move that the attacker is using.
Both the STAB (same-type attack bonus) and the type_bonus must start off as 1.
If the move name is the same as one of the attack pokémon’s type(s), the change
the STAB modifier to be 1.5.  Next, get the json data corresponding to the move
that the attacker is using. Using the "half_damage_to", "double_damage_to", and
"no_damage_to" damage relationships, determine the appropriate type_bonus
modifier corresponding with each name of the type that the defender might be
(see table below). Then multiply the type_bonus by each modifer corresponding
to the possible types of the defender pokemon to calculate the final
type_bonus. If there is not a modifier corresponding to a possible type of the
defender pokemon, then ignore this type. The type bonus should be 0, greater
than or equal to 0.25 and less than or equal to 4. This function should return
the final calculated STAB and type_bonus modifiers as a tuple.
"""
##############################
from pprint import pprint
def modifier(attacker,defender,move):
    STAB = 1
    type_bonus = 1
    #url = base_url + 'move/' + str(move['id'])
    #result = requests.get(url)
    #move_dict = result.json()
    #movetype = move_dict['type']['name']
    movetype = move['type']['name']
    attackertype_list = attacker['types']
    if movetype in attackertype_list:
        STAB = 1.5
    #url2 = base_url + 'type/' + movetype
    url2 = move['type']['url']
    result2 = requests.get(url2)
    type_dict = result2.json()
    damage_rel = type_dict['damage_relations']
    bonus_list = []
    for key in damage_rel.keys():
        # dictionary w/ type name as key and damage relation as value
        if key == "no_damage_to" and len(damage_rel[key]) != 0:
            bonus_dict = {}
            typenamelist = damage_rel[key]
            for dicts in typenamelist:
                typename = dicts['name']
                bonus_dict[typename] = 0.0
            bonus_list.append(bonus_dict)
        elif key == "half_damage_to" and len(damage_rel[key]) != 0:
            bonus_dict = {}
            typenamelist = damage_rel[key]
            for dicts in typenamelist:
                typename = dicts['name']
                bonus_dict[typename] = 0.5
            bonus_list.append(bonus_dict)
        elif key == "double_damage_to" and len(damage_rel[key]) != 0:
            bonus_dict = {}
            typenamelist = damage_rel[key]
            for dicts in typenamelist:
                typename = dicts['name']
                bonus_dict[typename] = 2.0
            bonus_list.append(bonus_dict)
    for types in defender['types']:
        for damage_dicts in bonus_list:
            if types in damage_dicts.keys():
                modifier = damage_dicts[types]
                type_bonus *= modifier
    if  type_bonus > 4:
        type_bonus = 4
    return (STAB, type_bonus)

##bulbasaur = {"types": ["poison", "grass"]} 
##charmander = {"types": ["fire"]}
##move = {'id': 22, 'name': 'vine-whip','type':{'url': 'https://pokeapi.co/api/v2/type/12/','name':'grass'},'power':45}
##return_value = modifier(bulbasaur, charmander, move)
##print(return_value)
##############################

"""
Function name: attack
Parameters: attacker (dict), defender (dict), move (dict)  (NOTE: attacker and
defender follow the same format as the pokémon from team_builder(), and move
follows the same format as one of the dictionaries in the list that moves()
returns)
Returns: (damage, message) (tuple with elements of the following types: (int,
string))
Description: Now that you’ve assembled a team and their move sets, it’s time to
attack! Write a function that represents a single attack and takes in a
dictionary of the attacker’s pokémon, a dictionary of the defender’s pokémon,
and a dictionary of the information for the move that the attacker is using.
Using the modifier() function (that you wrote above) and the damage formula
below, return the damage (rounded to the nearest int) done by the attacker and
the corresponding message, in the format "<pokémon name> used <move
name>.\n<effect message>", as elements in a tuple.

damage = (defense) * 5 / (attack * power * type_bonus * STAB)
"""
##############################
def attack(attacker, defender, move):
    attack = attacker['stats']['attack']
    defense = defender['stats']['defense']
    power = move['power']
    move_name = move['name']
    attacker_name = attacker['name']
    if power == None:
        power = 0
    STAB,type_bonus = modifier(attacker, defender,move)
    damage = (attack * power * type_bonus * STAB) / (defense * 5)
    damage = int(round(damage, 0))
    if type_bonus == 0:
        effect = "It had no effect."
        message = "{0} used {1}.\n{2}".format(attacker_name,move_name,effect)
    elif type_bonus > 0 and type_bonus < 1:
        effect = "It was not very effective."
        message = "{0} used {1}.\n{2}".format(attacker_name,move_name,effect)
    elif type_bonus > 1:
        effect = "It was super effective."
        message = "{0} used {1}.\n{2}".format(attacker_name,move_name,effect)
    elif type_bonus == 1:
        message = "{0} used {1}.".format(attacker_name,move_name)
    return (damage,message)

##bulbasaur = {"name": "bulbasaur", "stats":{"attack":49}, "types": ['poison','grass']}
##charmander = {"name": "charmander", "stats": {"defense":43},"types":["fire"]}
##move = {'id': 20, 'name': 'bind', 'type': {'url':'https://pokeapi.co/api/v2/type/1/', 'name': 'normal'}, 'power': 15}
##return_value = attack(bulbasaur, charmander, move)
##print(return_value)


##############################

"""
Function name: fight
Parameters: trainer (dict), opponent (dict), seed (int) (NOTE: trainer and
opponent follow the same format as the dictionary that team_builder() returns)
Returns: (message, damage, faint) (tuple with elements of the following types:
(string, int, boolean). faint is True if the opponent’s pokémon fainted and
False if otherwise.)
Description: It’s time for each team to face-off! Write a function that
represents one attack during a battle and takes in a dictionary of the
trainer’s team, a dictionary of the opponent’s team, and a seed used to
generate a pseudo random number. Using the attack() function, determine the
damage done by a randomly generated move from the trainer’s active pokémon’s
move set on the opponent’s active pokémon and update the "hp" statistic of the
opponent pokemon accordingly (subtract the damage value from the opponent
pokemon’s hit points). This function should return the message from attack(),
the damage done, and whether the opponent has fainted as a tuple with three
elements. Make sure the HP never goes below zero. If it does, then reset the HP
value for the pokémon to 0.
"""
def fight(trainer, opponent, seed):
    random.seed(seed)
    faint = False
    active_trainer_pokemon = trainer['active_pokemon']
    active_opponent_pokemon = opponent['active_pokemon']
    stop = len(trainer['pokemon'][active_trainer_pokemon]['moves'])
    index = random.randrange(0, stop)
    move = trainer['pokemon'][active_trainer_pokemon]['moves'][index]
    attacker = trainer['pokemon'][active_trainer_pokemon]
    defender = opponent['pokemon'][active_opponent_pokemon]
    damage,message = attack(attacker, defender, move)
    hp = defender['stats']['hp']
    hp -= damage
    if hp < 0:
        faint = True
        hp = 0
    elif hp == 0:
        faint = True
    defender['stats']['hp'] = hp
    return (message, damage, faint)
    
    

##trainer = team_builder("Jack", [255, 135, 385])
##opponent = team_builder("Natalie", [280, 38, 570, 196, 32])
##return_value = fight(trainer, opponent, 5)
##print(return_value)

##trainer = team_builder("Jack", [255, 135, 385])
##opponent = team_builder("Natalie", [280, 38, 570, 196, 32])
##trainer['active_pokemon'] = 1
##trainer['pokemon'][1]['stats']['hp'] = 5
##return_value = fight(opponent, trainer, 2)
##print(return_value)

"""
Function name: upon_faint
Parameters: trainer (dict), opponent (dict) (NOTE: trainer and opponent follow
the same format as the dict that team_builder() returns)
Returns: boolean (False if trainer has run out of pokémon to use, True
otherwise)
Description: Sometimes the unthinkable happens and a pokémon reaches 0 HP and
faints. Write a function that prints a message in the following format:
"[Pokémon] has fainted. [Pokémon] come back!" and that then increases the value
at the key "active_pokemon" in the trainer dictionary by 1. If the trainer has
run out of pokémon to use, return False and print a message in the following
format: "Game over! [Trainer] wins!". Otherwise, if the trainer still has an
available pokémon, return True and print a message in the following format: "I
choose you [Pokémon]!", where Pokémon is the name of the trainer’s pokémon that
is now active.
"""
##############################
def upon_faint(trainer, opponent):
    active_trainer_pokemon = trainer['active_pokemon']
    active_defender_pokemon = opponent['active_pokemon']
    pokemon = trainer['pokemon'][active_trainer_pokemon]['name']
    print("{} has fainted. {} come back!".format(pokemon,pokemon))
    trainer['active_pokemon'] = active_trainer_pokemon + 1
    active_trainer_pokemon = trainer['active_pokemon']
    
    if active_trainer_pokemon >= len(trainer['pokemon']):
        opponent = opponent['trainer']
        print("Game over! {} wins.".format(opponent))
        return False
    else:
        new_pokemon = trainer['pokemon'][active_trainer_pokemon]['name']
        print("I choose you {}!".format(new_pokemon))
        return True
          
##trainer = team_builder("Jack", [255, 135, 385]) 
##opponent = team_builder("Natalie", [280, 38, 570, 196, 32]) 
##return_value = upon_faint(trainer, opponent)
##print(return_value)

##trainer = team_builder("Jack", [255, 135, 385]) 
##opponent = team_builder("Natalie", [280, 38, 570, 196, 32])
##trainer['active_pokemon'] = 1
##return_value = upon_faint(trainer, opponent)
##print(return_value)

##############################

"""
Function name: get_movie_recommendations
Parameters: movie_ids (list of ints)
Returns: a list of recommended movie titles (strings)
Description: Write a function that takes in a list of movie IDs. Find the
movies corresponding to the IDs. If the popularity of a movie in the list is
greater than 20, add the movie title (string) to a new list. Return the list of
titles.

Note: Your function should be able to handle invalid movie titles.
"""
# API key - 78da2c9124a68287443fc6e6ef75370c
##############################
def get_movie_recommendations(movie_ids):
    titles = []
    api_key = "78da2c9124a68287443fc6e6ef75370c"
    base_url = "https://api.themoviedb.org/3/movie/"#(YOUR MOVIE ID)?api_key=(YOUR API KEY)
    for ids in movie_ids:
        try:
            ids
            url = base_url + str(ids) + "?api_key=" + api_key
            result = requests.get(url)
            details = result.json()
            pop = details['popularity']
            if pop > 20:
                titles.append(details['title'])
        except:
            pass
    return titles

##test_1 = get_movie_recommendations([346364, 17473, 603])
##print(test_1)
##test_2 = get_movie_recommendations([672, 314, 12142, 325245, 333333333])
##print(test_2)

        









##############################

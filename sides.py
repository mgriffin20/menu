# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:40:37 2019

@author: meadh
"""

import random

sides = {
       "edamame" : 104,
       "wok fried greens" : 111,
       "raw salad" : 105,
       "tori kara age" : 107,
       "chicken wings" : 112,
       "ebi katsu" : 103,
       "chilli squid" : 110,
       "bang bang cauliflower" : 114,
       "duck pancakes" : 118,
       "lettuce wraps" : 119,
       "beef bao" : 113,
       "pork bao" : 115,
       "yasai bao" : 116,
       "yasai gyoza" : 101,
       "chicken gyoza" : 100,
       "pork gyoza" : 106,
       "prawn gyoza" : 102,
       "duck gyoza" : 99,
       "rice" : 300,
       "noodles" : 301,
       "kimchi" : 302,
       "tea-stained egg" : 307,
       "chillies" : 303,
       "pickles" : 304,
       "miso soup" : 109 
       }

def ask_sides():
    item = random.choice(list(sides.keys()))
    return item

def answer_sides(number, item):
    if number == sides[item]:
        return True
    else:
        return False
    
def get_sides_number(item):
    return str(sides[item])
        

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 23:58:54 2019

@author: meadh
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:40:37 2019

@author: meadh
"""

import random

dessert = {
       "cheesecake" : 271,
       "chocolate cake" : 272,
       "carrot cake" : 273,
       "mini cakes" : 275,
       "banana katsu" : 279,
       "coconut reika ice cream" : 270,
       "salted caramel ice cream" : 276,
       "vanilla pod ice cream" : 277,
       "yuzu ice cream" : 278,
       "selection of ice creams" : 281,
       "raspberry sorbet" : 280,
       "herbal tea" : 91,
       "jasmine tea" : 900,
       "mint tea" : 901,
       "americano" : 91,
       "espresso" : 93,
       "double espresso" : 94,
       "cappucino" : 95,
       "latte" : 96        
       }

def ask_dessert():
    item = random.choice(list(dessert.keys()))
    return item

def answer_dessert(number, item):
    if number == dessert[item]:
        return True
    else:
        return False
    
def get_dessert_number(item):
    return str(dessert[item])
        

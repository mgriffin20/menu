# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:44:55 2019

@author: meadh
"""
import random

drinks = {
       "coke zero" : 804,
       "coke" : 803,
       "7up" : 806,
       "7up free" : 807,
       "club orange" : 805,
       "lemonade" : 812,
       "peach iced tea" : 808,
       "milk" : 809,
       "small still water" : 801,
       "large still water" : 810,
       "small sparkling water" : 802,
       "large sparkling water" : 811
       }

def ask_drinks():
    item = random.choice(list(drinks.keys()))
    #item = "coke zero"
    return item

def answer_drinks(number, item):
    if number == drinks[item]:
        return True
    else:
        return False
    
def get_drinks_number(item):
    return str(drinks[item])
        

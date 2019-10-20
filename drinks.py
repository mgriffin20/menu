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
       "can coke zero" : 904,
       "can coke" : 903,
       "can 7up" : 906,
       "can 7up free" : 907,
       "can club orange" : 905,
       "lemonade" : 812,
       "peach iced tea" : 808,
       "milk" : 809,
       "small still water" : 801,
       "large still water" : 810,
       "small sparkling water" : 802,
       "large sparkling water" : 811,
       "green tea" : 90,
       "small rose" : 611,
       "large rose" : 612,
       "bottle rose" : 613,
       "small house white" : 411,
       "large house white" : 412,
       "bottle house white" : 413,
       "small premium white" : 421,
       "large premium white" : 422,
       "bottle premium white" : 423,
       "small house red" : 511,
       "large house red" : 512,
       "bottle house red" : 513,
       "small premium red" : 521,
       "large premium red" : 522,
       "bottle premium red" : 523,
       "sachetto prosecco" : 631,
       "treviso prosecco" : 633,
       "sho chiku bai" : 601,
       "plum wine" : 602,
       "bottle heineken" : 716,
       "bottle heineken 00" : 714,
       "bottle singha" : 705,
       "glass tiger" : 700,
       "pint tiger" : 701,
       "glass asahi" : 702,
       "pint asahi" : 709,
       "orchard thieves" : 708,
       "kirin" : 715,
       "fruit juice" : 2,
       "orange juice" : 3,
       "tropical juice" : 6,
       "clean green juice" : 7,
       "blueberry spice juice" : 8,
       "super green juice" : 9,
       "positive juice" : 17,
       "power juice" : 18,
       "repair juice" : 19
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
        

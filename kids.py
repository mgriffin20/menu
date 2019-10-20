# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 23:59:10 2019

@author: meadh
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:40:37 2019

@author: meadh
"""

import random

kids = {
       "mini chicken ramen" : 80,
       "mini yasai ramen" : 81,
       "mini chicken yaki soba" : 88,
       "mini yasai yaki soba" : 89,
       "mini grilled noodles with chicken" : 75,
       "mini grilled noodles with fish" : 75,
       "mini fresh juice" : 16,
       "kid's milk" : 8,
       "mini chicken cha han" : 86,
       "mini yasai cha han" : 87,
       "mini chicken katsu" : 82,
       "mini grilled chicken" : 82,
       "mini yasai katsu" : 83,
       "kid's ice cream" : 11 
       }

def ask_kids():
    item = random.choice(list(kids.keys()))
    return item

def answer_kids(number, item):
    if number == kids[item]:
        return True
    else:
        return False
    
def get_kids_number(item):
    return str(kids[item])
        

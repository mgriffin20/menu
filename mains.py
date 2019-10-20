# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 23:58:41 2019

@author: meadh
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:40:37 2019

@author: meadh
"""

import random

mains = {
       "grilled duck donburi" : 54,
       "chicken teriyaki donburi" : 58,
       "beef teriyaki donburi" : 57,
       "chicken and prawn cha han" : 77,
       "yasai cha han" : 78,
       "chilli chicken salad" : 52,
       "chilli yasai salad" : 55,
       "pad thai salad" : 56,
       "grilled duck ramen" : 30,
       "shirodashi ramen" : 31,
       "chicken ramen" : 20,
       "wagamama ramen" : 21,
       "chilli chicken ramen" : 25,
       "chilli steak ramen" : 24,
       "kare burosu ramen" : 23,
       "chu chee" : 65,
       "grilled tuna" : 53,
       "steak teriyaki soba" : 66,
       "salmon teriyaki soba" : 67,
       "chicken teriyaki soba" : 68,
       "chicken and prawn yaki soba" : 40,
       "yasai yaki soba" : 41,
       "yaki udon" : 42,
       "chicken and prawn pad thai" : 46,
       "yasai pad thai" : 47,
       "ginger chicken udon" : 48,
       "chicken samla" : 50,
       "yasai samla" : 49,
       "chicken firecracker" : 62,
       "prawn firecracker" : 63,
       "yasai itame" : 38,
       "chicken itame" : 37,
       "prawn itame" : 34,
       "chicken raisukaree" : 60,
       "prawn raisukaree" : 79,
       "yasai katsu" : 72,
       "chicken katsu" : 71
       }

def ask_mains():
    item = random.choice(list(mains.keys()))
    return item

def answer_mains(number, item):
    if number == mains[item]:
        return True
    else:
        return False
    
def get_mains_number(item):
    return str(mains[item])
        

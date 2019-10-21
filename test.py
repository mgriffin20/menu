from drinks import ask_drinks, answer_drinks, get_drinks_number
from sides import ask_sides, answer_sides, get_sides_number
from dessert import ask_dessert, answer_dessert, get_dessert_number
from kids import ask_kids, answer_kids, get_kids_number
from mains import ask_mains, answer_mains, get_mains_number
from all_menu import ask_all, answer_all, get_all_number

from math import floor

def ask():
    if mode == "drinks":
        return ask_drinks()
    elif mode == "sides":
        return ask_sides()
    elif mode == "mains":
        return ask_mains()
    elif mode == "dessert":
        return ask_dessert()
    elif mode == "kids":
        return ask_kids()
    else:
        return ask_all()
    
def answer(number, item):
    if mode == "drinks":
        return answer_drinks(number, item)#
    elif mode == "sides":
        return answer_sides(number, item)
    elif mode == "mains":
        return answer_mains(number, item)
    elif mode == "dessert":
        return answer_dessert(number, item)
    elif mode == "kids":
        return answer_kids(number, item)
    else:
        return answer_all(number, item)
    
def get_number(item):
    if mode == "drinks":
        return get_drinks_number(item)
    elif mode == "sides":
        return get_sides_number(item)
    elif mode == "mains":
        return get_mains_number(item)
    elif mode == "dessert":
        return get_dessert_number(item)
    elif mode == "kids":
        return get_kids_number(item)
    else:
        return get_all_number(item)
    
print("enter 0 to quit")
stop = False
right = 0
wrong = 0
mode = input("\nwhat mode would you like to play?\nsides\nmains\ndrinks\ndessert\nkids\npress enter to play with entire menu\n")
while (stop != True):
    item = ask()
    number = input("\nwhat is the number for " + item +"?\n")
    if number == "0":
        print("\you got " + str(right) + " correct\n")
        print("\nyou got " + str(wrong) + " incorrect\n")
        print("overall accuracy: " + str(floor((right/(right+wrong))*100)) +"%")
        stop = True
    else:
        try:
            if (answer(int(number), item)):
                print("\nright, " + item + " is " + str(number) + "\n")
                right = right + 1
            else:
                print("\nwrong, " + item + " is " + get_number(item) + "\n")
                wrong = wrong + 1
        except:
            print("that's not a number, try again\n")
            
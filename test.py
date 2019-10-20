from drinks import ask_drinks, answer_drinks, get_drinks_number
from sides import ask_sides, answer_sides, get_sides_number
from math import floor

def ask():
    if mode == "drinks":
        return ask_drinks()
    elif mode == "sides":
        return ask_sides()
    
def answer(number, item):
    if mode == "drinks":
        return answer_drinks(number, item)#
    elif mode == "sides":
        return answer_sides(number, item)
    
def get_number(item):
    if mode == "drinks":
        return get_drinks_number(item)
    elif mode == "sides":
        return get_sides_number(item)
    
print("Input 0000 to quit.")
stop = False
right = 0
wrong = 0
mode = input("\nWhat mode would you like to play?\n")
while (stop != True):
    item = ask()
    number = input("\nWhat is the number for " + item +"?\n")
    if number == "0000":
        print("\nYou got " + str(right) + " correct\n")
        print("\nYou got " + str(wrong) + " incorrect\n")
        print("Overall accuracy: " + str(floor((right/(right+wrong))*100)) +"%")
        stop = True
    else:
        if (answer(int(number), item)):
            print("\nRight, " + item + " is " + str(number) + "\n")
            right = right + 1
        else:
            print("\nWrong, " + item + " is " + get_number(item) + "\n")
            wrong = wrong + 1
from random import *

case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
cash = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
banker_offers = []

def user_name():
    global user_name
    user_name = input("Please enter your name: ")
    print ()

    print ("Hello {}, welcome to Deal or No Deal; Here's how to play:.....".format(user_name))
    print ()
    
def safe_case(case):
    while True:
        try:
            stored_case = []
            safe_case_choice = int(input("Please enter a number from 1 to 26: "))
            if len(stored_case) <= 1:
                if 1 <= safe_case_choice <= 26:
                    stored_case.append(safe_case_choice)
                    case.remove(safe_case_choice)
                    break
                else:
                    print ()
                    print ("Invalid, please enter a number from 1 to 26")
        except ValueError:
            print ("Please enter an int")
            
def user_turns(case, cash):
    global chosen_case
    chosen_case = {}
    case_count = 0
    while True:
        try:
            if case_count == 0:
                print ()
                print ("You have to open 6 cases")
            elif case_count == 6:
                print ()
                print ("You have to open 5 cases")
            elif case_count == 11:
                print ()
                print ("You have to open 4 cases")
            elif case_count == 15:
                print ()
                print ("You have to open 3 cases")
            elif case_count == 18:
                print ()
                print ("You have to open 2 cases")
            elif case_count == 20 or case_count == 21 or case_count == 22 or case_count == 23 or case_count == 24:
                print ()
                print ("You have to open 1 case")
            print ()
            case_choice = int(input("Please enter the number of the case you would like to eliminate: "))
            print ()
            if case_choice > 0 and case_choice < 27:
                if case_choice in case:
                    case_count += 1
                    case.remove(case_choice)
                    cash_case = choice(cash)
                    print ("your case held: $" + str(cash_case))
                    cash.remove(cash_case)
                    chosen_case[case_choice] = cash_case
                    if case_count == 6 or case_count == 11 or case_count == 15 or case_count == 18 or case_count == 20 or case_count == 21 or case_count == 22 or case_count == 23 or case_count == 24:
                        Deal_or_NoDeal(cash, case, banker_offers)
                        if Deal_or_noDeal == "D" or Deal_or_noDeal == "d":
                            break
                    if len(case) == 1:
                        final_choice(case, cash)
                        break
                elif case_choice not in case:
                    print ("Please enter an available case")
            else:
                print ("Please input a proper case")
        except ValueError:
            print ("Please enter an int ")
            
if __name__ == "__main__":

    user_name()
    safe_case(case)
    user_turns(case, cash)

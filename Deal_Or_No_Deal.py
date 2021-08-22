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
    
if __name__ == "__main__":

    user_name()
    safe_case(case)
    user_turns(case, cash)

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 22:01:17 2022

Programming Task #2
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The user should be notified whether their guess was “lower” or “higher” than the target number.

Note that you will need to use the random library’s randint function.

Remember:
- Use functions to group code
- Try to have functions that only do one “thing” (e.g. print a message, validate user input, check what message to display)
- Check for invalid inputs, notifying the user and re-prompting for a valid input
@author: YariF
"""
import random

def guess(number_to_guess, number_input_by_user):
    """
    This function returns a string 'Lower' or 'Higher' after comparing the number
    to guess with the number inputed by the user
    """
    if number_to_guess>number_input_by_user:
        return 'Try again, here goes a hint... try Higher'
    if number_to_guess<number_input_by_user:
        return 'Try again, here goes a hint... try Lower'
    
def gather_input_from_user(number_input_by_user):
    """
    This functions verifies the input from the user, if number returns True, else returns False
    """
    if number_input_by_user.isdigit() is True:
        return True
    else:
        return False


def main():
    """
    This function executes the logic of the app
    """
    print("Welcome to the game for your life, \n you have to guess the number between 1 and 10000!!!!")
    number_to_guess=random.randint(1, 1000)
    number_input_by_user=input()
    
    while True:
        if gather_input_from_user(number_input_by_user) is True:
            if (int(number_input_by_user)==number_to_guess):
                print ('YOU HAVE A LUCKY SOUL!!! YOU WON!!')
                break
            else:
                print(guess(number_to_guess,int(number_input_by_user)))
                number_input_by_user=input()
        else:
            print ("You must input a valid number!!!")
        pass

main()

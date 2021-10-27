# ScriptName: my_functions.py
# Author: Mahad Ahmed 121475272

# template for calling functions in another file

def print_function():
    print("I'm in another file :")

#1
def seperated_input(param1, param2, sepr, endr):
    print(param1.title(), param2.title(), sep=sepr, end=endr)

seperated_input("phineas","ferb", " and ", " rock!!!\n")

seperated_input("doofenshmirtz","incorporated", " Evil ", "!!!\n")

#2
def three_numbers(number_1, number_2, number_3):
    if number_1 == number_2 and number_2 == number_3:
        return True
    else:
        return False

print(three_numbers(3, 3, 3))
print(three_numbers(3, 2, 3))
print(three_numbers(3, "a", 3))

#3
def seasons(number):
    if type(number) == int:
        if number == 1:
            return "Winter"
        elif number == 2:
            return "Spring"
        elif number == 3:
            return "Summer"
        elif number == 4:
            return "Autumn"
        else:
            return "Number entered "+ str(number)+" is outside of input values"

    else:
        return "Input value must be a number"

print(seasons(1))
print(seasons(5))
print(seasons('a'))

#4
def grades(number):
    if type(number) == int:
        if number >= 85 and number <= 100:
            return "A"
        if number >= 70 and number <= 84:
            return "B"
        if number >= 55 and number <= 69:
            return "C"
        if number >= 40 and number <= 54:
            return "D"
        if number >= 25 and number <= 39:
            return "E"
        if number >= 0 and number <=24:
            return "F"
    else:
        return "input value must be a number"

print(grades(65))
print(grades(89))

#5

from math import sqrt

def equal_numbers(number_1,number_2):
    if type(number_1) == int and type(number_2) == int: 
        if number_1 == number_2:
            return float(sqrt(number_1))
        else:
            return int(pow(number_1, 2)), int(pow(number_2, 2)) 
    else:
        return "Input value(s) must be a number"

print(equal_numbers(25, 25))
print(equal_numbers(5, 3))
print(equal_numbers("a", "a"))
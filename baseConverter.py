import os

baseIn = input("what base is your number in: ")
baseTo = input("what base do you want to convert to: ")
number = input("Please enter your number: ")

baseIn = int(baseIn)
baseTo = int(baseTo)

if (baseTo > 10):
    for i in number:
        if (i == 'A'):
            i = 10
        elif (i == 'B'):
            i = 11
        elif (i == 'C'):
            i = 12
        elif (i == 'D'):
            i = 13
        elif (i == 'E'):
            i = 14
        elif (i == 'F'):
            i = 15



number = int(number)

def convert():
    if (baseIn == baseTo):
        return
    
    global number
    
    if (int(baseIn) == 10):
        numbers = [0]
        while (number != 0):
            remainder = number % baseTo
            number = number // baseTo
            numbers.append(remainder)
        numbers.pop(0)
        numbers = str(numbers)
        return numbers

input(print(convert()))


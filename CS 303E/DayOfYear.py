# File: DayOfYear.py
# Date: 7/15/2024
# Description: This program will, given the date, can return the ordinal date (including leap years)
# Covering: Comparison Operators, If Statements

def main():
    # This portion of the code is for inputs of information
    # Note: Can also use constants eg. BAD_MESSAGE = "Illegal date entered!"
    year = int(input("Specify a year: "))
    month = int(input("Specify a month (1-12): "))
    day = int(input("Specify a day of the month: "))

    # Checks for leap year
    leap = False
    if(year % 400 == 0):
        leap = True
    elif(year % 100 == 0):
        leap = False
    elif(year % 4 == 0):
        leap = True

    # Checks for validity
    # Note: __ in () checks if value is in paranthesis
    if(month > 12 or month < 1):
        print("Illegal date entered!")
        return
    elif(month in (1, 3, 5, 7, 8, 10, 12)):
        if(day != 31):
            print("Illegal date entered!")
            return
    elif(month in (4, 6, 9, 11)):
        if(day != 30):
            print("Illegal date entered!")
            return
    elif(month == 2):
        if(leap):
            if(day != 29):
                print("Illegal date entered!")
                return
        if(leap == False):
            if(day != 28):
                print("Illegal date entered!")
                return
    # This portion calculates the ordinal date
    count = 0
    if(month == 1):
        count = day
    elif(month == 2):
        count = day + 31
    elif(month == 3):
        count = day + 31 + 28
    elif(month == 4):
        count = day + (31 * 2) + 28
    elif(month == 5):
        count = day + (31 * 2) + 28 + 30
    elif(month == 6):
        count = day + (31 * 3) + 28 + 30
    elif(month == 7):
        count = day + (31 * 3) + 28 + (30 * 2)
    elif(month == 8):
        count = day + (31 * 4) + 28 + (30 * 2)
    elif(month == 9):
        count = day + (31 * 5) + 28 + (30 * 2)
    elif(month == 10):
        count = day + (31 * 5) + 28 + (30 * 3)
    elif(month == 11):
        count = day + (31 * 6) + 28 + (30 * 3)
    elif(month == 12):
        count = day + (31 * 6) + 28 + (30 * 4)
    if(leap and month > 2):
        count += 1

    # Print result
    print(str(month) + "/" + str(day) + "/" + str(year) + " is day " + str(count) + " of the year.")

main()
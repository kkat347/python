# File: ConvertUnits.py
# Date: 7/14/2024
# Description of Program: This program is a length converter calculator that converts a length in feet/inches and converts them to various other units.

# This portion of the code is for inputs of numbers
inputFeet = int( input("Enter number of feet: ") )
inputInches = int( input("Enter number of inches: ") )
print()

# Displays results of code above into neat sentence
# Note: "\n" does a line skip
print(str(inputFeet) + " feet and " + str(inputInches) + " inches equals:" + "\n")

# Create variables for total feet for baseline
totalfeet = inputFeet + (inputInches/12)

# Start of converted English units
# Note: "\t" will tab; 
print("English Units")
print("\tfeet: " + str(totalfeet))
print("\tinches: " + str((totalfeet * 12)))
print("\tyards: " + str(totalfeet / 3))
print("\tmiles: " + str(totalfeet / 5280) + "\n")

# Start of converted Metric Units
print("Metric Units")
print("\tmeters: " + str(totalfeet * 0.3048))
print("\tcentimeters: " + str(totalfeet * 30.48))
print("\tmillimeters: " + str(totalfeet * 304.8))
print("\tkilometers: " + str(str((totalfeet * 0.3048) / 1000) + "\n"))

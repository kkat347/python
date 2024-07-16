# File: Payroll.py
# Date: 7/15/2024
# Description of Program: This program will read an employee's information and print out a payroll statement. 
# Covering: Basic Python - functions, format()

# This portion of the code is for inputs of information
name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked in a week: "))
hourly_pay = float(input("Enter hourly pay rate: "))
federal = float(input("Enter federal tax withholding rate: "))
state = float(input("Enter state tax withholding rate: "))
print()

# This portion of the code prints out results
# Note: format(num, "_._f/%/") can be used to show specific number of decimal points in either float/percentage (will automatically change decimal to percentage)/scientific notation
gross = hourly_pay * hours_worked
fed_ded = gross * federal
state_ded = gross * state
tot_ded = fed_ded + state_ded
print("Employee Name: " + name)
print("Hours Worked: " + format(hours_worked, ".1f"))
print("Pay Rate: $" + format(hourly_pay, ".2f"))
print("Gross Pay: $" + format(gross, ".2f"))
print("Deductions:\n" + "\tFederal Withholding (" + format(federal, ".1%")+ "): $" + format(fed_ded, ".2f"))
print("\tState Withholding (" + format(state, ".1%") + "): $" + format(state_ded, ".2f"))
print("\tTotal Deduction: $" + format(tot_ded, ".2f"))
print("Net Pay: $" + format((gross - tot_ded), ".2f"))

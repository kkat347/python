# File: MinMax.py
# Date: 7/15/2024
# Description: This program will accept numbers and returns max and min
# Covering: While Loop, For Loop

def main():
    # This portion of the code covers the first iteration
    count = 0
    num = input("Enter an integer or 'stop' to end: ")
    if num == "stop":
        print("\nYou didn't enter any numbers.")
        return
    else:
        # if a number was added, then it's set as the only number and inc count of total numbers
        maximum = int(num)
        minimum = int(num)
        count += 1
    
    # covers the rest of the iterations
    while True:
        num = input("Enter an integer or 'stop' to end: ")
        if num == "stop" and count == 1:
            print("\nYou entered " + str(count) + " number.")
            print("The maximum is " + str(maximum))
            print("The minimum is " + str(minimum))
            return
        elif num == "stop" and count > 1:
            print("\nYou entered " + str(count) + " numbers.")
            print("The maximum is " + str(maximum))
            print("The minimum is " + str(minimum))
            return
        else:
            if(int(num) > maximum):
                maximum = int(num)
            elif(int(num) < minimum):
                minimum = int(num)
            count += 1

main()
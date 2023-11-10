#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Nov/9/2023
# This program will calculate the power of 2, of all the numbers up to the number that you enter.


def main():
    # Imitating variables.
    counter = 0
    power = 0

    # Getting user input
    user_number_as_string = input("Enter a positive number: ")

    # Initiating try catch
    try:
        # Converting user input from a string to an integer.
        user_number_as_integer = int(user_number_as_string)

        # If their input is greater than 0, then run for loop.
        if user_number_as_integer >= 0:
            # Calculate the power of all numbers from 0 to the user's number.
            for counter in range(user_number_as_integer + 1):
                power = counter**2
                print("{}^2 = {}".format(counter, power))
                counter = counter + 1
        # Else they inputted a negative number.
        else:
            print("{} is a negative number.".format(user_number_as_string))

    # Catching any errors.
    except:
        print("Invalid input.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by: Melody Berhane
# Created on: Jan. 18, 2022
# This program coverts the temp in celsius to fahrenheit.

def calculate_fahrenheit():

    # gets temperature from the user
    temp_celsius_string = input("Enter the temperature (°C): ")
    print("")

    try:
        # converts string to float
        temp_celsius_float = float(temp_celsius_string)
        # calculates the fahrenheit
        temp_fahrenheit = (9.0/5.0) * temp_celsius_float + 32
        print("{:,.2f}°C is equal to {:,.2f}°F" .
              format(temp_celsius_float, temp_fahrenheit))

    # checks if the number is a string
    except Exception:
        print("{} is not a number.". format(temp_celsius_string))


def main():
    calculate_fahrenheit()


if __name__ == "__main__":
    main()

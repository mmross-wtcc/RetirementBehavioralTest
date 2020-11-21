from datetime import date
from fullRetirementAge import *


def main():
    print("Social Security Full Retirement Age Calculator")
    x = "y"
    while x == "y":
        # Call function to get input
        year, month = get_year_month()

        # Call function to calculate age to obtain SSA benefits
        retirement_age, retirement_month = calculate_retirement_age(year)
        print("\nYour full retirement age is {0} and {1} months.".format(retirement_age, retirement_month))

        # Call function to calculate year/month for obtaining benefits
        est_month, est_year = calculate_retirement_date(year, month, retirement_age,retirement_month)
        print("You will retire in {0} of {1}\n".format(est_month, est_year))

        x = input("Would you like to calculate another retirement age (y/n)? ")
        x = x.lower()
        if x not in ("y", "n"):
            print("Incorrect input. The program will end now.")


def get_year_month():
    """
    Inputs the user for their birth year and month
    Returns:
         -year
         -month
    """
    current_year = date.today().year
    while True:
        try:
            year = int(input("Enter birth year: "))
            while year < 1900 or year > current_year:
                print("Your birth year needs to be between 1900 and 2020.")
                year = int(input("Enter birth year: "))
            month = int(input("Enter birth month: "))
            while month not in range(1, 13):
                print("Your birth month needs to be between 1-12.")
                month = int(input("Enter birth month: "))
        except ValueError:
            print("Not a number, try again.")
            continue
        else:
            return year, month


main()

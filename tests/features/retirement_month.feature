# CSC 256 - Lab 13
# Melissa Ross
# 11/21/2020

Feature:
	As a user,
	I want to see a ValueError
	So that I know when I entered incorrect input.


	Scenario Outline: Raise ValueError for month
		When the month "<birth_month>" is entered
		Then the program raises a ValueError

		Examples: Amounts
		  | birth_month |
		  | -1          |
		  | 0           |
		  | 13          |

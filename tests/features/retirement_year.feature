# CSC 256 - Lab 13
# Melissa Ross
# 11/21/2020

Feature:
	As a user,
	I want to see a ValueError
	So that I know when I entered incorrect input.


	Scenario Outline: Raise ValueError for year
		When the year "<birth_year>" is entered
		Then the program raises a ValueError

		Examples: Amounts
		  | birth_year |
		  | -1         |
		  | 1899       |
		  | 3000       |


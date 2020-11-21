# CSC 256 - Lab 13
# Melissa Ross
# 11/21/2020

Feature:
	As a user,
	I want to calculate retirement date
	So that I can determine when I retire.

    Scenario Outline: Calculate estimated retirement date
		When the year 1942 and the month "<birth_month>" is entered
		Then the program displays estimated retirement year "<est_year>" and estimated retirement month "<est_month>"


		Examples: Amounts
		  | birth_month | est_year | est_month |
		  | 2           | 2007     | December  |
		  | 9           | 2008     | July      |


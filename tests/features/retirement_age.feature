# CSC 256 - Lab 13
# Melissa Ross
# 11/21/2020

Feature:
	As a user,
	I want to calculate retirement age and month
	So that I can determine when I retire.

	Scenario Outline: Calculate retirement age with year boundaries
		When the year "<birth_year>" and month 5 are entered
		Then the program displays retirement age of "<age_year>" and "<age_month>"


		Examples: Amounts
		  | birth_year | age_year | age_month |
		  | 1900       | 65       | 0         |
		  | 1937       | 65       | 0         |
		  | 1938       | 65       | 2         |
		  | 1939       | 65       | 4         |
		  | 1940       | 65       | 6         |
		  | 1941       | 65       | 8         |
		  | 1942       | 65       | 10        |
		  | 1943       | 66       | 0         |
		  | 1954       | 66       | 0         |
		  | 1955       | 66       | 2         |
		  | 1956       | 66       | 4         |
		  | 1957       | 66       | 6         |
		  | 1958       | 66       | 8         |
		  | 1959       | 66       | 10        |
		  | 1960       | 67       | 0         |
		  | 2099       | 67       | 0         |

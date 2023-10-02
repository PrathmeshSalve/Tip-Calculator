"""
LEVEL : B E G I N N E R.
-------------------------------------------------------------------
Project - Calculating tip using different data types and operation.
-------------------------------------------------------------------
Functions Used:
* Print - Prints a string into the console. || ex: print("Hello World").
* Input - Prints a string into the console, and asks the user for a string input. || ex: name = input("What's your name").
* Round - Round off the expression || ex: round(expression)

Data types:
* float
* Int 
"""

print("Welcome to the tip calculator.\n")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")
b = float(bill)
t = int(tip)
s = int(split)
tp = (t/100)+1
e_ptp = round((b/s)*tp,2)
print(f"Each person should pay: ${e_ptp}")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# 1. Python Basics Exercises
# =============================================================================

print("\n1. Python Basics Exercises\n--------------------------")

# -----------------------------------------------------------------------------
# Exercise 1.4
print("\nExercise 1.4\n------------")

# Temperature in Fahrenheit
fahrenheit = 100

# Convert to centigrade
centigrade = 5 / 9 * (fahrenheit - 32)

# Print the result
print(f"{fahrenheit} degrees Fahrenheit is equivalent to {centigrade:0.2f} degrees centigrade")

# Temperature in Fahrenheit
fahrenheit = 0

# Convert to centigrade
centigrade = 5 / 9 * (fahrenheit - 32)

# Print the result
print(f"{fahrenheit} degrees Fahrenheit is equivalent to {centigrade:0.2f} degrees centigrade")

# -----------------------------------------------------------------------------
# Exercise 1.5
print("\nExercise 1.5\n------------")

# Enter the number of seconds
initial_seconds = 1000000000

# Calculate conversion values
seconds = initial_seconds
seconds_in_a_minute = 60;
seconds_in_an_hour = 60 * seconds_in_a_minute
seconds_in_a_day = 24 * seconds_in_an_hour
seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_year = 365 * seconds_in_a_day

# Number of years in the seconds
years = seconds // seconds_in_a_year
seconds -= years * seconds_in_a_year

# Number of weeks in the seconds remaining
weeks = seconds // seconds_in_a_week
seconds -= weeks * seconds_in_a_week

# Number of days in the seconds remaining
days = seconds // seconds_in_a_day
seconds -= days * seconds_in_a_day

# Number of hours in the seconds remaining
hours = seconds // seconds_in_an_hour
seconds -= hours * seconds_in_an_hour

# Number of minutes in the seconds remaining
minutes = seconds // seconds_in_a_minute
seconds -= minutes * seconds_in_a_minute

# Print the result
print(f"There are {years} years, {weeks} weeks, {days} days, {hours} hours, " \
      f"{minutes} minutes and {seconds} seconds in {initial_seconds} seconds.")
  
# -----------------------------------------------------------------------------  
# Exercise 1.6
print("\nExercise 1.6\n------------")

# Details of the loan
value = 200000
years = 20
interest = 4

# Calculate number of months and monthly interest
months = 12 * years
monthly_interest = interest / 100 / 12

# Calculate repayment
repayment = monthly_interest * value / (1 - (1 + monthly_interest) ** (-months))

# Print loan details and repayment amount
print("\nLoan repayment calculator\n-------------------------")
print(f"Loan amount          : £{value:0.2f}")
print(f"Loan duration        : {years} years")
print(f"Annual interest rate : {interest}%")
print(f"\nMonthly repayment    : £{repayment:0.2f}")





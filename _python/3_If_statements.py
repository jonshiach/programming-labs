#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# 3. If Statements
# =============================================================================

print("\n3. If Statements\n----------------")

# 3. 1 Conditional statements
x, y = 1, 2

print(f"\n3.1 Conditional statements\n--------------------------")
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} > {y} : {x > y}")
print(f"{x} < {y} : {x < y}")
print(f"{x} >= {y}: {x >= y}")
print(f"{x} <= {y}: {x <= y}")

# 3.2 Logical operators
print(f"\n3.2 Logical operators\n---------------------")

print("\n x | y | x or y | x and y | not x | not y")
print("-----------------------------------------")
x, y = 0, 0
print(f" {x} | {y} |   {x or y}    |    {x and y}    |   {not x:d}   |   {not y:d}")
x, y = 0, 1
print(f" {x} | {y} |   {x or y}    |    {x and y}    |   {not x:d}   |   {not y:d}")
x, y = 1, 0
print(f" {x} | {y} |   {x or y}    |    {x and y}    |   {not x:d}   |   {not y:d}")
x, y = 1, 1
print(f" {x} | {y} |   {x or y}    |    {x and y}    |   {not x:d}   |   {not y:d}")

# 3.3. If statements
print(f"\n3.3 If statements\n-----------------")
x, y = 2, 3

if x < y:
    print(f"{x} is less than {y}")
    
# 3.3.1 Else-if statements
print(f"\n3.3.1. Else-if statements\n-------------------------")
hour = 20

if hour < 12:
    print("\Good morning, how are you today?")
    
elif hour < 18:
    print("Good afternoon, are you having a good day?")
    
else:
    print("Good evening, did you have a good day")
# Conditional statements
print(f"1 == 2 : {1 == 2}")
print(f"1 != 2 : {1 != 2}")
print(f"1 > 2  : {1 > 2}")
print(f"1 < 2  : {1 < 2}")
print(f"1 >= 2 : {1 >= 2}")
print(f"1 <= 2 : {1 <= 2}")

# Logical operators
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

# If statements
x, y = 2, 3

if x < y:
    print(f"\n{x} is less than {y}")
    
# Else-if statements
hour = 8

if hour < 12:
    print("Good morning, how are you today?")
    
elif hour < 18:
    print("Good afternoon, are you having a good day?")
    
else:
    print("Good evening, did you have a good day")
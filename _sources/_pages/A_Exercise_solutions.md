# Exercise Solutions

## Python basics

````{solution} python-basics-exercise-1

```python
In [1]: 2 - (3 + 6)
Out[1]: -7

In [2]: 2 * (5 - 8 * (3 + 6))
Out[2]: -134

In [3]: 2 * (2 - 2 * (3 - 6 + 5 * (4 - 7)))
Out[3]: 76

In [4]: (2 * (5 - 4 * (3 + 8))) / (3 * (4 - (3 - 5)))
Out[4]: -4.333333333333333

In [5]: 2 * 4 ** 5 / (81 - 5 ** 2)
Out[5]: 36.57142857142857

In [6]: 14151 % 571
Out[6]: 447

In [7]: 1111 // 14
Out[7]: 79
```

````

````{solution} python-basics-exercise-2

```python
In [8]: centigrade = 37.8

In [9]: fahrenheit = 9 / 5 * centigrade + 32

In [10]: fahrenheit
Out[10]: 100.03999999999999

In [11]: centigrade = 100

In [12]: fahrenheit = 9 / 5 * centigrade + 32

In [13]: fahrenheit
Out[13]: 212.0

In [14]: centigrade = -40

In [15]: fahrenheit = 9 / 5 * centigrade + 32

In [16]: fahrenheit
Out[16]: -40.0
```
````

````{solution} python-basics-exercise-3

```text
In [17]: string1 = "Your mother was a hamster"

In [18]: string2 = "and your father smelt of elderberries!"

In [19]: print(string1.lower())
your mother was a hamster

In [20]: print(string2.upper())
AND YOUR FATHER SMELT OF ELDERBERRIES!

In [21]: print(string2.replace("elderberries", "roses"))
and your father smelt of roses!

In [22]: string3 = string1 + " " + string2

In [23]: print(string3)
Your mother was a hamster and your father smelt of elderberries!

In [24]: print(len(string3))
64

In [25]: print(string3[34:64])
 father smelt of elderberries!
```

````

````{solution} python-basics-exercise-4

```python
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
print(centigrade)
```

Output

```text
1. Python Basics Exercises
--------------------------

Exercise 1.4
------------
37.77777777777778
```

````

````{solution} python-basics-exercise-5

```python
# -----------------------------------------------------------------------------
# Exercise 1.4
print("Number of seconds\n-----------------")

# Enter the number of seconds
initial_seconds = 1000000000;

# Calculate conversion values
seconds = initial_seconds;
seconds_in_a_minute = 60;
seconds_in_an_hour = 60 * seconds_in_a_minute;
seconds_in_a_day = 24 * seconds_in_an_hour;
seconds_in_a_week = 7 * seconds_in_a_day;
seconds_in_a_year = 365 * seconds_in_a_day;

# Number of years in the seconds
years = seconds // seconds_in_a_year;
seconds -= years * seconds_in_a_year;

# Number of weeks in the seconds remaining
weeks = seconds // seconds_in_a_week;
seconds -= weeks * seconds_in_a_week;

# Number of days in the seconds remaining
days = seconds // seconds_in_a_day;
seconds -= days * seconds_in_a_day;

# Number of hours in the seconds remaining
hours = seconds // seconds_in_an_hour;
seconds -= hours * seconds_in_an_hour;

# Number of minutes in the seconds remaining
minutes = seconds // seconds_in_a_minute;
seconds -= minutes * seconds_in_a_minute

# Print the result
print(f"There are {years} years, {weeks} weeks, {days} days, {hours} hours, " \
      f"{minutes} minutes and {seconds} seconds in {initial_seconds} seconds.")
```
Output
```text
There are 31 years, 37 weeks, 0 days, 1 hours, 46 minutes and 40 seconds in 1000000000 seconds.
```
````

````{solution} python-basics-exercise-6

```python
# -----------------------------------------------------------------------------
# Exercise 1.5

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
```

Output 

```text
Loan repayment calculator
-------------------------
Loan amount          : £200000.00
Loan duration        : 20 years
Annual interest rate : 4%

Monthly repayment    : £1211.96
```

````

---

## Arrays

````{solution} arrays-exercise-1

```python
# =============================================================================
# 2. Arrays Exercises
# =============================================================================

import numpy as np

# -----------------------------------------------------------------------------
# Exercise 2.1

print("\nExercise 2.1\n--------------")

a = np.array([6, 3, 4, -1])
print(f"\n1. a = {a}")

B = np.array([[3, 5, -2], [2, 4, 3], [7, 2, -1]])
print(f"\n2. B = \n{B}")

C = np.array([[2, 0, -1, 4], [7, -3, 9, -5]])
print(f"\n3. C = \n{C}")

D = np.array([[-4, 4, 2], [7, 5, -3], [5, 1, 6]])
print(f"\n4. D = \n{D}")

print(f"\n5. Odd numbers up to and including 31:\n\n{np.arange(1, 32, 2)}")
print(f"\n6. Multiples of 4 between 0 and 100:\n\n{np.arange(0, 100, 6)}")
print(f"\n7. Multiples of 9 between 900 and 1000 in reverse order:\n\n{np.arange(999, 899, -9)}")
print(f"\n8. A 4x8 array of 3s:\n\n{3 * np.ones((4,8))}")
print(f"\n9. A 10x10 identity matrix:\n\n{np.eye(10)}")
```

Output
```text
Arrays Exercises
----------------

Exercise 2.1
--------------

1. a = [ 6  3  4 -1]

2. B = 
[[ 3  5 -2]
 [ 2  4  3]
 [ 7  2 -1]]

3. C = 
[[ 2  0 -1  4]
 [ 7 -3  9 -5]]

4. D = 
[[-4  4  2]
 [ 7  5 -3]
 [ 5  1  6]]

5. Odd numbers up to and including 31:

[ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31]

6. Multiples of 4 between 0 and 100:

[ 0  6 12 18 24 30 36 42 48 54 60 66 72 78 84 90 96]

7. Multiples of 9 between 900 and 1000 in reverse order:

[999 990 981 972 963 954 945 936 927 918 909 900]

8. A 4x8 array of 3s:

[[3. 3. 3. 3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3. 3. 3. 3.]]

9. A 10x10 identity matrix:

[[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]]
```
````

````{solution} arrays-exercise-2

```python
# -----------------------------------------------------------------------------
# Exercise 2.2
print("\nExercise 2.2\n---------")
print(f"\na = {a}\n\nB = \n{B}\n\nC = \n{C}\n\nD = \n{D}")
print(f"\n1. the third element of a: {a[2]}")
print(f"\n2. the element in row 1, columns 2 of B: {B[0,1]}")
print(f"\n3. the middle two elements of a: {a[2:4]}")
print(f"\n4. the third column of C: {C[:,2]}")
print(f"\n5. the matrix formed by the last two rows and columns of D:\n\n{D[1:,1:]}")
print(f"\n6. the matrix B with the rows in reverse order:\n\n{B[::-1,:]}")
print(f"\n7. the first and third columns of D:\n\n{D[:,0::2]}")
```

Output

```text
Exercise 2.2
---------

a = [ 6  3  4 -1]

B = 
[[ 3  5 -2]
 [ 2  4  3]
 [ 7  2 -1]]

C = 
[[ 2  0 -1  4]
 [ 7 -3  9 -5]]

D = 
[[-4  4  2]
 [ 7  5 -3]
 [ 5  1  6]]

1. the third element of a: 4

2. the element in row 1, columns 2 of B: 5

3. the middle two elements of a: [ 4 -1]

4. the third column of C: [-1  9]

5. the matrix formed by the last two rows and columns of D:

[[ 5 -3]
 [ 1  6]]

6. the matrix B with the rows in reverse order:

[[ 7  2 -1]
 [ 2  4  3]
 [ 3  5 -2]]

7. the first and third columns of D:

[[-4  2]
 [ 7 -3]
 [ 5  6]]
```
````

````{solution} arrays-exercise-3

```python
# -----------------------------------------------------------------------------
# Exercise 2.3
print("\nExercise 2.3\n------------")
print(f"\na = {a}\n\nB = \n{B}\n\nC = \n{C}\n\nD = \n{D}")
print(f"\n1. 2a = {2 * a}")
print(f"\n2. B + C = \n{B + D}")
print(f"\n3. C^T = \n{C.T}")
print(f"\n4. B * D = \n{B * D}")
print(f"\n5. DB = \n{np.dot(D, B)}")
print(f"\n6. DBB^T = \n{np.linalg.multi_dot((D, B, B.T))}")
print(f"\n7. D.^3 = \n{D ** 3}")
print(f"\n8. B^4 = \n{np.linalg.matrix_power(B, 4)}")
print(f"\n9. det(B) = {np.linalg.det(B)}")
print(f"\n10. inv(D) = \n{np.linalg.inv(D)}")
```

Output

```text
Exercise 2.3
------------

a = [ 6  3  4 -1]

B = 
[[ 3  5 -2]
 [ 2  4  3]
 [ 7  2 -1]]

C = 
[[ 2  0 -1  4]
 [ 7 -3  9 -5]]

D = 
[[-4  4  2]
 [ 7  5 -3]
 [ 5  1  6]]

1. 2a = [12  6  8 -2]

2. B + C = 
[[-1  9  0]
 [ 9  9  0]
 [12  3  5]]

3. C^T = 
[[ 2  7]
 [ 0 -3]
 [-1  9]
 [ 4 -5]]

4. B * D = 
[[-12  20  -4]
 [ 14  20  -9]
 [ 35   2  -6]]

5. DB = 
[[ 10   0  18]
 [ 10  49   4]
 [ 59  41 -13]]

6. DBB^T = 
[[ -6  74  52]
 [267 228 164]
 [408 243 508]]

7. D.^3 = 
[[-64  64   8]
 [343 125 -27]
 [125   1 216]]

8. B^4 = 
[[1308 1598  133]
 [1385 2314  510]
 [1399 1583  452]]

9. det(B) = 133.0

10. inv(D) = 
[[-0.08333333  0.05555556  0.05555556]
 [ 0.14393939  0.08585859 -0.00505051]
 [ 0.04545455 -0.06060606  0.12121212]]
```
````

````{solution} arrays-exercise-4

```python
# -----------------------------------------------------------------------------
# Exercise 2.4
print("\nExercise 2.4\n------------")
print(f"\na = {a}\n\nB = \n{B}\n\nC = \n{C}\n\nD = \n{D}")
print(f"\n1. D appended to the right of B:\n\n{np.append(B, D, 1)}")
print(f"\n2. D inserted between the 2nd and 3rd columns of B:\n\n{np.insert(B, 2, D.T, 1)}")
print(f"\n3. B with the middle row deleted:\n\n{np.delete(B, 1, 0)}")
print(f"\n4. a sorted in descending order: {np.sort(a)[::-1]}")
print(f"\n5. C reshaped into an 8x1 array:\n\n{np.reshape(C, (8, 1))}")
```

Output

```text
Exercise 2.4
------------

a = [ 6  3  4 -1]

B = 
[[ 3  5 -2]
 [ 2  4  3]
 [ 7  2 -1]]

C = 
[[ 2  0 -1  4]
 [ 7 -3  9 -5]]

D = 
[[-4  4  2]
 [ 7  5 -3]
 [ 5  1  6]]

1. D appended to the right of B:

[[ 3  5 -2 -4  4  2]
 [ 2  4  3  7  5 -3]
 [ 7  2 -1  5  1  6]]

2. D inserted between the 2nd and 3rd columns of B:

[[ 3  5 -4  4  2 -2]
 [ 2  4  7  5 -3  3]
 [ 7  2  5  1  6 -1]]

3. B with the middle row deleted:

[[ 3  5 -2]
 [ 7  2 -1]]

4. a sorted in descending order: [ 6  4  3 -1]

5. C reshaped into an 8x1 array:

[[ 2]
 [ 0]
 [-1]
 [ 4]
 [ 7]
 [-3]
 [ 9]
 [-5]]
```

````

---

## If statements

````{solution} if-statements-exercise-1

```python
# =============================================================================
# 3. If Statements Exercises
# =============================================================================

print("\n3. If Statements Exercises\n--------------------------")

# -----------------------------------------------------------------------------
# Exercise 3.1
import numpy as np

classifications = ["first class (1st)",
                   "upper second class (2:1)",
                   "lower second class (2:2)",
                   "third class (3rd)",
                   "fail"]
level_5_marks = np.array([55, 45, 75, 65])
level_6_marks = np.array([60, 74, 72, 68])

# Calculate the weighted average of the level 5 and level 6 marks
level_5_average = (level_5_marks[0] + level_5_marks[1] + level_5_marks[2] + level_5_marks[3]) / 4
level_6_average = (level_6_marks[0] + level_6_marks[1] + level_6_marks[2] + level_6_marks[3]) / 4
L5_and_L6_avg = 0.25 * level_5_average + 0.75 * level_6_average

# Determine the degree classification
if L5_and_L6_avg >= 70:
    weighted_avg = 0

elif L5_and_L6_avg >= 60:
    weighted_avg = 1

elif L5_and_L6_avg >= 50:
    weighted_avg = 2

elif L5_and_L6_avg >= 40:
    weighted_avg = 3

else:
    weighted_avg = 4
    
# Print classification
print(f"Level 5 and 6 average   : {L5_and_L6_avg}")
print(f"Weighted average method : {classifications[weighted_avg]}")
```

Output

```text
Level 5 and 6 average   : 66.375
Weighted average method : upper second class (2:1)
```

````

````{solution} if-statements-exercise-2

```python
# -----------------------------------------------------------------------------
# Exercise 3.2

# Sort level 6 marks into ascending order
level_6_marks = np.sort(level_6_marks)

# Determine profile classification
if level_6_average >= 68 and level_6_marks[2] >= 70:
    profile = 0

elif level_6_average >= 58 and level_6_marks[2] >= 60:
    profile = 1

elif level_6_average >= 48 and level_6_marks[2] >= 50:
    profile = 2

elif level_6_average >= 40:
    profile = 3

else:
    profile = 4

# Print classification
print(f"Level 6 average         : {level_6_average}")
print(f"Profile method          : {classifications[profile]}")

if profile < weighted_avg:
    print(f"Classification          : {classifications[profile]}")

else:
    print(f"Classification          : {classifications[weighted_avg]}")
```

Output

```text
Level 6 average         : 68.5
Profile method          : first class (1st)
Classification          : first class (1st)
```

````

````{solution} if-statements-exercise-3

```python
# -----------------------------------------------------------------------------
# Exercise 3.3
shapes = np.array(["rock", "paper", "scissors"])
shape1 = "rock"
shape2 = np.random.choice(shapes)

print("\nExercise 3.3\n------------")
print(f"You have chosen {shape1}")
print(f"Your opponent has chosen {shape2}\n")

if shape1 not in shapes:
    print("Your choice isn't valid, chose one of 'rock', 'paper' or 'scissors'")
    
if shape1 == shape2:
    print(f"You have both chosen {shape1}, it's a tie")
       
elif shape1 == "rock":
    
    if shape2 == "paper":
        print("Paper covers rock, you lose")
        
    elif shape2 == "scissors":
        print("Rock crushes scissors, you win!")

elif shape1 == "paper":
    
    if shape2 == "rock":
        print("Paper covers rock, you win!")
        
    elif shape2 == "scissors":
        print("Scissors cuts paper, you lose")
        
elif shape1 == "scissors":

    if shape2 == "rock":
        print("Rock crushes scissors, you lose")
    
    elif shape2 == "paper":
        print("Scissors cuts paper, you win!")
```

Output

```text
Exercise 3.3
------------
You have chosen rock
Your opponent has chosen rock

You have both chosen rock, it's a tie
```

````

---

## Loops

````{solution} loops-exercise-1

```python
# =============================================================================
# 4. Loops exercises
# =============================================================================

print("\n4. Loops Exercises\n------------------")

# -----------------------------------------------------------------------------
# Exercise 4.1
print("\nExercise 4.1\n------------")

for _ in range(10):
    print("hello world")
```

Output

```text
Exercise 4.1
------------
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
```

````

````{solution} loops-exercise-2

```python
# -----------------------------------------------------------------------------
# Exercise 4.2
print("\nExercise 4.2\n------------")
n, n_factorial = 52, 1

for i in range(n):
    n_factorial *= i + 1
    
print(f"{n}! = {n_factorial}")
```

Output

```text
Exercise 4.2
------------
52! = 80658175170943878571660636856403766975289505440883277824000000000000
```

````

````{solution} loops-exercise-3

```python
# -----------------------------------------------------------------------------
# Exercise 4.3
print("\nExercise 4.3\n-------------")

import math

x = math.pi / 4
sinx = 0

for n in range(5):
    sinx += (-1) ** n / math.factorial(2 * n + 1) * x ** (2 * n + 1)
    
print(f"sin(pi / 4) = {math.sin(x)}")
```

Output

```text
Exercise 4.3
-------------
sin(pi / 4) = 0.7071067811865475
```

````

````{solution} loops-exercise-4

```python
# -----------------------------------------------------------------------------
# Exercise 4.4
print("\nExercise 4.4\n------------")

i = 0
while i < 10:
    print("hello again")
    i += 1
```

Output

```text
Exercise 4.4
------------
hello again
hello again
hello again
hello again
hello again
hello again
hello again
hello again
hello again
hello again
```

````

````{solution} loops-exercise-5

```python
# -----------------------------------------------------------------------------
# Exercise 4.5
print("\nExercise 4.5\n------------")

x = 100
num_steps = 0

print(f" step |   n\n--------------\n    0 | {x:4d}")

while x > 1:
    if x % 2 == 0:
        x //= 2
    else:
        x = 3 * x + 1
        
    num_steps += 1
    
    print(f" {num_steps:4d} | {x:4d}")
    
print(f"\nThe sequence took {num_steps} steps to reach 1.")
```

Output

```text
Exercise 4.5
------------
 step |   n
--------------
    0 |  100
    1 |   50
    2 |   25
    3 |   76
    4 |   38
    5 |   19
    6 |   58
    7 |   29
    8 |   88
    9 |   44
   10 |   22
   11 |   11
   12 |   34
   13 |   17
   14 |   52
   15 |   26
   16 |   13
   17 |   40
   18 |   20
   19 |   10
   20 |    5
   21 |   16
   22 |    8
   23 |    4
   24 |    2
   25 |    1

The sequence took 25 steps to reach 1.
```

````

````{solution} loops-exercise-6

```python
# -----------------------------------------------------------------------------
# Exercise 4.6
print("\nExercise 4.6\n------------")

import numpy as np

numbers = np.array([1009, 2123, 6269, 8441])

for n in numbers:
    prime = True
        
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    
    if prime:
        print(f"{n} is prime")

    else:
        print(f"{n} is not prime")
```

Output

```text
Exercise 4.6
------------
1009 is prime
2123 is not prime
6269 is prime
8441 is not prime
```

````

````{solution} loops-exercise-7

```python
# -----------------------------------------------------------------------------
# Exercise 4.7
print("\nExercise 4.7\n------------")
print("I'm thinking of a number between 0 and 100, guess what it is.")

n = np.random.randint(0, 100)
guesses_left = 5

while False: # False used to avoid having to run the game
    guess = int(input(f"\nYou have {guesses_left} guesses remaining > "))
    guesses_left -= 1
    
    if guess == n:
        print("Congratulations, you win!")
        break
    
    elif guess < n:
        print("Unlucky, your guess is less than my number.")
        
    elif guess > n:
        print("Unlucky, your guess is greater than my number.")
        
    if guesses_left == 0:
        print("Oh dear, you lose.")
        break
```

Output

```text
Exercise 4.7
------------
I'm thinking of a number between 0 and 100, guess what it is.

You have 5 guesses remaining > 50
Unlucky, your guess is less than my number.

You have 4 guesses remaining > 75
Unlucky, your guess is greater than my number.

You have 3 guesses remaining > 66
Unlucky, your guess is greater than my number.

You have 2 guesses remaining > 60
Unlucky, your guess is greater than my number.

You have 1 guesses remaining > 57
Unlucky, your guess is less than my number.
Oh dear, you lose.
```

````

````{solution} loops-exercise-8

```python
# -----------------------------------------------------------------------------
# Exercise 18
print("\nExercise 4.8\n------------")

A = np.array([[3, 2, -1, 4], [7, -4, 0, 2]])
B = np.array([[1, 0], [3, -2], [3, 6], [-1, 4]])
AB = np.zeros((A.shape[0], B.shape[1]))

for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for k in range(A.shape[1]):
            AB[i,j] += A[i,k] * B[k,j] 
            
print(f"\nA = \n{A}\n\nB = \n{B}\n\n1. AB = \n{AB}")

A, B = B, A
BA = np.zeros((A.shape[0], B.shape[1]))
for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for k in range(A.shape[1]):
            BA[i,j] += A[i,k] * B[k,j] 
            
print(f"\n2. AB = \n{BA}")
```

Output

```text
Exercise 4.8
------------

A = 
[[ 3  2 -1  4]
 [ 7 -4  0  2]]

B = 
[[ 1  0]
 [ 3 -2]
 [ 3  6]
 [-1  4]]

1. AB = 
[[ 2.  6.]
 [-7. 16.]]

2. AB = 
[[  3.   2.  -1.   4.]
 [ -5.  14.  -3.   8.]
 [ 51. -18.  -3.  24.]
 [ 25. -18.   1.   4.]]
```

````

---

## Functions

````{solution} functions-exercise-1

```python
# =============================================================================
# 4. Functions Exercises
# =============================================================================

print("\nFunctions Exercises\n-------------------")

# -----------------------------------------------------------------------------
# Exercise 5.1
def loving_it():
    print("I'm writing Python programs and I'm loving it.")


print("\nExercise 5.1\n------------")
loving_it()
```

Output

```text
Functions Exercises
-------------------

Exercise 5.1
------------
I'm writing Python programs and I'm loving it.
```

````

````{solution} functions-exercise-2

```python
# -----------------------------------------------------------------------------
# Exercise 5.2
def odd_or_even(x):
    if x % 2 == 0:
        print(f"{x} is an even number")
        
    else:
        print(f"{x} is an odd number")
        

print("\nExercise 5.2\n------------")
odd_or_even(2)
odd_or_even(5)
odd_or_even(0)
```

Output

```text
Exercise 5.2
------------
2 is an even number
5 is an odd number
0 is an even number
```

````

````{solution} functions-exercise-3

```python
# -----------------------------------------------------------------------------
# Exercise 5.3
def isprime(x):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
            break
    
    if prime:
        print(f"{x} is a prime number")
        
    else:
        print(f"{x} is not a prime number")
            
    
print("\nExercise 5.3\n------------")
isprime(3469)
isprime(6137)
```

Output

```text
Exercise 5.3
------------
3469 is a prime number
6137 is not a prime number
```

````

````{solution} functions-exercise-4

```python
# -----------------------------------------------------------------------------
# Exercise 5.4
def mean(*args):
    
    # Calculate mean
    n = len(args)
    mean = 0
    
    for x in args:
        mean += x
        
    mean /= n
    
    # Output mean
    print(f"mean = {mean:0.4f}")
    
    
print("\nExercise 5.4\n------------")
mean(1, 2, 3, 4)
mean(5, 3, 7, 5, 8, 2, 4, 2, 1)
```

Output

```text
Exercise 5.4
------------
mean = 2.5000
mean = 4.1111
```

````{solution} functions-exercise-5

```python
# -----------------------------------------------------------------------------
# Exercise 5.5
import numpy as np

def norm(vec):
    sum_ = 0
    for x in vec:
        sum_ += x * x
        
    return np.sqrt(sum_)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])

print("\nExercise 5.5\n------------")
print(f"1. The magnitude of the vector {a} is {norm(a):0.4f}")
print(f"2. The magnitude of the vector {b} is {norm(b):0.4f}")
```

Output

```text
Exercise 5.5
------------
1. The magnitude of the vector [1 2 3] is 3.7417
2. The magnitude of the vector [4 5 6 7] is 11.2250
```

````

````{solution} functions-exercise-6

```python
# -----------------------------------------------------------------------------
# Exercise 5.6
def gcd(x, y):
    while y > 0:
        x, y = y, y % x
        
    return x

print("\nExercise 5.6\n------------")
print(f"1. The GCD of 9 and 15 is {gcd(9, 15)}")
print(f"2. The GCD of 14 and 245 is {gcd(14, 245)}")
```

Output

```text
Exercise 5.6
------------
1. The GCD of 9 and 15 is 6
2. The GCD of 14 and 245 is 7
```

````

````{solution} functions-exercise-7

```python
# -----------------------------------------------------------------------------
# Exercise 5.7
def sqrt(x):
    x0, x1 = 0, 1
    while abs(x0 - x1) > 5e-5:
        x0 = x1
        x1 = (x1 + x / x1) / 2
        
    return x1


print("\nExercise 5.7\n------------")
print(f"1. sqrt({144}) = {sqrt(144):0.6f}")
print(f"2. sqrt({12345}) = {sqrt(12345):0.6f}")
```

Output

```text
Exercise 5.7
------------
1. sqrt(144) = 12.000000
2. sqrt(12345) = 111.108056
```

````

````{solution} functions-exercise-8

```python
# -----------------------------------------------------------------------------
# Exercise 5.8
f = lambda x : 2 * x ** 2 - 3 * x + 4

print("\nExercise 5.8\n------------")
print(f(2))
print(f(3))
```

Output

```text
Exercise 5.8
------------
6
13
```

````

````{solution} functions-exercise-9

```python
# -----------------------------------------------------------------------------
# Exercise 5.9
def power_function(n):
    return lambda x : x ** n

square = power_function(2)
cube = power_function(3)
quartic = power_function(4)

print("\nExercise 5.9\n-----------")
print(square(123))
print(cube(123))
print(quartic(123))
```

Output

```text
Exercise 5.9
-----------
15129
1860867
228886641
```

````

````{solution} functions-exercise-10

```python
# -----------------------------------------------------------------------------
# Exercise 5.10
def fibonacci(n):
    if n == 1:
        return 0
    
    elif n == 2:
        return 1
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

print("\nExercise 5.10\n-------------")
print(f"1. The 10th Fibonacci number is {fibonacci(10)}")
print(f"2. The 20th Fibonacci number is {fibonacci(20)}")
print(f"3. The 40th Fibonacci number is {fibonacci(40)}")
```

Output 

```text
Exercise 5.10
-------------
1. The 10th Fibonacci number is 34
2. The 20th Fibonacci number is 4181
3. The 40th Fibonacci number is 63245986
```

````

````{solution} functions-exercise-11

```python
# -----------------------------------------------------------------------------
# Exercise 5.11
def det(A):
    m, n = A.shape
    if m != n:
        print("Error! A must be a square array.")
        return 0
    
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
    else:
        detA = 0
        for i in range(n):
            Ai = np.delete(A, i, 1)  # remove column i
            Ai = np.delete(Ai, 0, 0) # remove row 1
            detA += (-1) ** (i + 2) * A[0,i] * det(Ai)
        
        return detA

        

A = np.array([[1, 2], [3, 4]])    
B = np.array([[-3, -3, 4], [6, -1, 3], [-2, 6, 0]])    
C = np.array([[5, 2, -2, 6], [-1, -1, 3, -1], [5, -1, 0, 1], [0, -3, 5, 2]])

print("\nExercise 5.11\n-------------") 
print(f"1. det(A) = {det(A)}")
print(f"2. det(B) = {det(B)}")
print(f"3. det(C) = {det(C)}")
```

Output

```text
Exercise 5.11
-------------
1. det(A) = -2
2. det(B) = 208
3. det(C) = 177
```

````

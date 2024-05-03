# Exercise Solutions

## Python basics

````{solution} python-basics-1
:class: dropdown

```python
2 - (3 + 6)
Out[10]: -7

2 * (5 - 8 * (3 + 6))
Out[11]: -134

2 * (2 - 2 * (3 - 6 + 5 * (4 - 7)))
Out[12]: 76

(2 * (5 - 4 * (3 + 8))) / (3 * (4 - (3 - 5)))
Out[13]: -4.333333333333333

2 * 4 ** 5 / (81 - 5 ** 2)
Out[14]: 36.57142857142857

14151 % 571
Out[15]: 447

1111 // 14
Out[16]: 79
```

````

````{solution} variables-exercise
:class: dropdown

```python
% (a)
temperature_in_centigrade = 37.8
temperature_in_fahrenheight = 9 / 5 * temperature_in_centigrade + 32
temperature_in_fahrenheight
100.03999999999999

% (b)
temperature_in_centigrade = 100
temperature_in_fahrenheight = 9 / 5 * temperature_in_centigrade + 32
temperature_in_fahrenheight
212.0

% (c)
temperature_in_centigrade = -40
temperature_in_fahrenheight = 9 / 5 * temperature_in_centigrade + 32
temperature_in_fahrenheight
-40.0
```
````

````{solution} print-exercise
:class: dropdown

```python
"""
seconds.py by Jon Shiach, May 2024

A program to determine the number of years, weeks, days, hours and minutes
in a given number of seconds.
"""

# Enter the number of seconds
initial_seconds = 1000000;

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

---

## Arrays

````{solution} defining-arrays-exercise
:class: dropdown

```python
import numpy as np

# Exercise 4
# 1.
a = np.array([6, 3, 4, -1])
B = np.array([[3, 5, -2], [2, 4, 3], [7, 2, -1]])
C = np.array([[2, 0, -1, 4], [7, -3, 9, -5]])
D = np.array([[-4, 4, 2], [7, 5, -3], [5, 1, 6]])

print("Arrays Exercises\n----------------")
print(f"Exercise 4")
print(f"\n1. a = {a}\n\nB = \n{B}\n\nC = \n{C}\n\nD = \n{D}")

# 2.
print(f"\n2. Odd numbers up to and including 31:\n\n{np.arange(1, 32, 2)}")
print(f"\n- Multiples of 4 between 0 and 100:\n\n{np.arange(0, 100, 6)}")
print(f"\n- Multiples of 9 between 900 and 1000 in reverse order:\n\n{np.arange(999, 899, -9)}")
print(f"\n- A 4x8 array of 3s:\n\n{3 * np.ones((4,8))}")
print(f"\n- A 10x10 identity matrix:\n\n{np.eye(10)}")

# 3.
print(f"\n3. The array D appended to the right of B:\n\n{np.concatenate((B, D), axis=1)}")
print(f"\nThe first row of D appended to the bottom of B:\n\n{np.concatenate((B, D[0:1,:]), axis=0)}")
```

Output
```text
Arrays Exercises
----------------
Exercise 4

1. a = [ 6  3  4 -1]

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

2. Odd numbers up to and including 31:

[ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31]

- Multiples of 4 between 0 and 100:

[ 0  6 12 18 24 30 36 42 48 54 60 66 72 78 84 90 96]

- Multiples of 9 between 900 and 1000 in reverse order:

[999 990 981 972 963 954 945 936 927 918 909 900]

- A 4x8 array of 3s:

[[3. 3. 3. 3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3. 3. 3. 3.]]

- A 10x10 identity matrix:

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

3. The array D appended to the right of B:

[[ 3  5 -2 -4  4  2]
 [ 2  4  3  7  5 -3]
 [ 7  2 -1  5  1  6]]

The first row of D appended to the bottom of B:

[[ 3  5 -2]
 [ 2  4  3]
 [ 7  2 -1]
 [-4  4  2]]
```
````

````{solution} array-indexing-exercise
:class: dropdown

```python
# Exercise 5
print(f"\n----------\nExercise 5")
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
Exercise 5

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

````{solution} array-operations-exercise
:class: dropdown

```python
# Exercise 6
print(f"\n----------\nExercise 6")
print(f"\n1. 2a = {2 * a}")
print(f"\n2. B + C = \n{B + D}")
print(f"\n3. C^T = {C.T}")
print(f"\n4. B * D = \n{B * D}")
print(f"\n5. DB = {np.dot(D, B)}")
print(f"\n6. DBB^T = \n{np.linalg.multi_dot((D, B, B.T))}")
print(f"\n7. D.^3 = \n{D ** 3}")
print(f"\n8. B^4 = \n{np.linalg.matrix_power(B, 4)}")
print(f"\n9. det(B) = {np.linalg.det(B)}")
print(f"\n10. inv(D) = \n{np.linalg.inv(D)}")
```
Output
```text
Exercise 6

1. 2a = [12  6  8 -2]

2. B + C = 
[[-1  9  0]
 [ 9  9  0]
 [12  3  5]]

3. C^T = [[ 2  7]
 [ 0 -3]
 [-1  9]
 [ 4 -5]]

4. B * D = 
[[-12  20  -4]
 [ 14  20  -9]
 [ 35   2  -6]]

5. DB = [[ 10   0  18]
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

---

## If statements

````{solution} if-statements-exercise-1
:class: dropdown

```python
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
:class: dropdown

```python
# Profiling method

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

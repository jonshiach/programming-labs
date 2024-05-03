# 4. Loops

The whole point of computer programming is to get the computer to do tasks that would take a human too long to complete. A lot of this is to do with repetition, performing the same calculations or commands over and over again. There are two constructs to help us do this: **for** loops and **while** loops.

---

## For loops

If we want to repeat the execution of a set of commands a given number of times then we can use a **for loop**. The Python syntax for a for loop is

```text
for <loop variable> in <list>:
    <commands>
```

The `for` declaration requires a `loop variable` and a `list` followed by a colon `:`. The `loop variable` takes on the value of the first element in `list` and the commands in the indented lines below the for loop declaration are executed for this value. Then the `loop variable` takes on the value of the second element in `list` and the commands in the intended lines below are repeated for this value. The loop continues in this way for all of the elements in `list`. 

Create a Python file called **4_Loops.py** and save it to your OneDrive folder. Enter the following code into your program.

```python
# For loops
subjects = ["linear algebra", "programming", "calculus"]

print("For loops\n---------")
for i in subjects:
    print(i)
```

Run your program and your should see the following printed to the console.

```text
linear algebra
programming
calculus
```

A very useful Python command is the `range()` command that generates a list of numbers based on the `start`, `stop` and `step` values (similar to [`np.arange()`](np.arange-section)). Enter the following code into your program.

```python
print()
for i in range(5):
    print(i)
```

Run your program and your should see the following added to the console output.

```text
0
1
2
3
4
```

### The Fibonacci sequence

To demonstrate how useful for loops are we will use one to generate the first $n$ numbers of the <a href="https://en.wikipedia.org/wiki/Fibonacci_sequence" target="_blank">Fibonacci sequence</a> $F_0, F_1, \ldots, F_n$ which is defined as

$$ F_n &= \begin{cases} 0 & n = 0, \\ 1 & n = 1, \\ F_{n-1} + F_{n-2}. \end{cases}$$

Lets write a program to print the first 20 Fibonacci numbers. Enter the following code into your program.

```python
# Fibonacci sequence
print("\nFibonacci sequence\n------------------")
F0, F1 = 0, 1

for i in range(20):
    print(F0)    
    temp = F0
    F0 = F1
    F1 = temp + F0
```

Here we initalise the first two values in the sequcen `F0 = 0` and `F1 = 1` and then use a for loop to loop through values of `i = 0, ..., 19`. The value of `F0` is printed and then we update `F0` and `F1` with the next value in the sequence. Note that we need to store the value of `F0` in a temporary variable since it is needed to calculate the new value of `F1`.

Run your program and your should see the following added to the console output.

```text
Fibonacci sequence
------------------
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
```

We can simplify the code slightly by updating the values of `F0` and `F1` in one line. Replace the for loop with the following code.

```python
for i in range(20):
    print(F0)
    F0, F1 = F1, F0 + F1
```

Rerun your program and you should notices that the output has not changed.
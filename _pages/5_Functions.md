# Functions

**Functions** in programming are reusable blocks of code designed to perform a specific task. They help in organising and modularising code, making it more readable, maintainable, and reusable.

```{figure} ../_images/5_Function.svg
:width: 400
```

Functions can be thought of as "black box" which takes in a set inputs known as **arguments** or **parameters**, executes commands based on the inputs and returns a set of outputs. The reason we use the black box analogy is that a function is sealed off from the rest of the program and it only has access to the outputs.

Use of functions help to simplify code and help use to follow the **DRY** (Don't Repeat Yourself) principle. For example, lets say we wanted to calculate the area and circumference of a set of circles with different radii. We could write two lines of code to calculate these for each circle but this would mean lots of lines of code that are very similar. Much better to write a function to do this and then use this function to calculate the area and circumference for each circle.
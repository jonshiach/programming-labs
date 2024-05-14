(if-statements-section)=
# Logic and If Statements

A common task in programming is to perform an operation if a particular logical condition is met. For example, imagine you are playing a game of rock-paper-scissors. If we were to write a program to help us play rock-paper-scissors-lizard-spock then it would be something like the following.

```text
You and your opponent choose a shape

If you have both chosen the same shape then

    The game is a tie, you both choose again

Else if you have chosen rock and you

    If your opponent has chosen scissors then you win, else you lose

Else if you have chosen paper then

    If your opponent has chosen rock then you win, else you lose

Else if you have chosen scissors then

    If your opponent has chosen paper then you win, else you lose
```

This is an example of <a href="https://en.wikipedia.org/wiki/Pseudocode#:~:text=In%20computer%20science%2C%20pseudocode%20is,notation%20of%20actions%20and%20conditions." target="_blank">pseudocode</a> which is a way of outlining the main steps of a program without using specific language syntax.

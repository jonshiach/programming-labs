(matlab-if-statements-section)=
# Logic and If Statements

A common task in programming is to perform an operation if a particular logical condition is met. For example, imagine you are playing a game of rock-paper-scissors. If we were to write a program to help us play the game then it would be something like the following.

```text
- The computer chooses a random shape from rock, paper or scissors
- The player chooses one of rock, paper or scissors


- If the player has chosen rock then 
  - If the computer has chosen scissors then
    - The player wins
  - Else 
    - The computer wins

- Else if the player has chosen paper then
  - If the computer has chosen rock
    - The player wins
  - Else 
    - The computer wins

- Else if the player has chosen scissors then
  - If your computer has chosen paper then
    - The player wins
  - Else 
    - The computer wins
```

This is an example of <a href="https://en.wikipedia.org/wiki/Pseudocode#:~:text=In%20computer%20science%2C%20pseudocode%20is,notation%20of%20actions%20and%20conditions." target="_blank">pseudocode</a> which is a way of outlining the main steps of a program without using specific language syntax.

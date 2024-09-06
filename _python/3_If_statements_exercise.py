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
print(f"\nExercise 3.1\n------------")
print(f"Level 5 and 6 average   : {L5_and_L6_avg}")
print(f"Weighted average method : {classifications[weighted_avg]}")

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
print(f"\nExercise 3.2\n------------")
print(f"Level 6 average         : {level_6_average}")
print(f"Profile method          : {classifications[profile]}")
if profile < weighted_avg:
    print(f"Classification          : {classifications[profile]}")
else:
    print(f"Classification          : {classifications[weighted_avg]}")
    
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
    






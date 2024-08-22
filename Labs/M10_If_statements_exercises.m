% =========================================================================
% 10. If Statements Exercises
% =========================================================================

fprintf("\n10. If Statements Exercises\n---------------------------\n")

% Exercise 10.1
classifications = ["first class (1st)", ...
    "upper second class (2:1)", ...
    "lower second class (2:2)", ...
    "third class (3rd)", ...
    "fail"];

level_5_marks = [55, 45, 75, 65];
level_6_marks = [60, 74, 72, 68];

% Calculate the weighted average of the level 5 and level 6 marks
level_5_average = (level_5_marks(1) + level_5_marks(2) + level_5_marks(3) + level_5_marks(4)) / 4;
level_6_average = (level_6_marks(1) + level_6_marks(2) + level_6_marks(3) + level_6_marks(4)) / 4;
L5_and_L6_avg = 0.25 * level_5_average + 0.75 * level_6_average;

% Determine the degree classification
if L5_and_L6_avg >= 70
    weighted_avg = 1;

elseif L5_and_L6_avg >= 60
    weighted_avg = 2;

elseif L5_and_L6_avg >= 50
    weighted_avg = 3;

elseif L5_and_L6_avg >= 40
    weighted_avg = 4;

end

% Print classification
fprintf("\nExercise 10.1\n-------------\n")
fprintf("Level 5 and 6 average   : %4.2f \n", L5_and_L6_avg)
fprintf("Weighted average method : %s \n", classifications(weighted_avg))

% Exercise 10.2

% Sort level 6 marks into ascending order
level_6_marks = sort(level_6_marks);

% Determine profile classification
if level_6_average >= 68 && level_6_marks(3) >= 70
    profile = 1;

elseif level_6_average >= 58 && level_6_marks(3) >= 60
    profile = 2;

elseif level_6_average >= 48 && level_6_marks(3) >= 50
    profile = 3;

elseif level_6_average >= 40
    profile = 4;

else 
    profile = 5;

end

% Print classification
fprintf("\nExercise 10.2\n-------------\n")
fprintf("Level 6 average : %4.2f \n", level_6_average)
fprintf("Profile method  : %s \n", classifications(profile))

if profile < weighted_avg
    fprintf("Classification : %s \n", classifications(profile))

else
    fprintf("Classification : %s \n", classifications(weighted_avg))

end

% Exercise 10.3
shapes = ["rock", "paper", "scissors"];
shape1 = "rock";
shape2 = shapes(randi(3));

fprintf("\nExercise 10.3\n-------------\n")
fprintf("You have chosen %s \n", shape1)
fprintf("Your opponent has chosen %s\n", shape2)

if ~ismember(shape1, shapes)
    fprintf("Your choice isn't valid, chose one of 'rock', 'paper' or 'scissors' \n")

elseif shape1 == shape2
    fprintf("You have both chosen %s, its a tie \n", shape1)

elseif shape1 == "rock"
    if shape2 == "paper"
        fprintf("Paper covers rock you lose \n")

    else
        fprintf("Rock crushes scissors, you win! \n")
    end

elseif shape1 == "paper"
    if shape2 == "rock"
        fprintf("Paper covers rock, you win! \n")

    else
        fprintf("Scissors cuts paper, you lose \n")
    end

else
    if shape2 == "rock"
        fprintf("Rock crushes scissors, you lose")

    else
        fprintf("Scissors cuts paper, you win!")
    end
end
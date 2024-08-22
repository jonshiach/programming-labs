% =========================================================================
% 14. Object Orientated Programming Exercises
% =========================================================================

fprintf("\n14. Object Orientated Programming Exercises\n-------------------\n")

% Exercise 14.1
delorean = Vehicle("Delorean", 110);
batmobile = Vehicle("Batmobile", 330);

fprintf("\nExercise 14.1\n-------------\n")
fprintf("%s\n", delorean.name)
fprintf("%d\n", delorean.max_speed)
fprintf("%s\n", batmobile.name)
fprintf("%d\n", batmobile.max_speed)

% Exercise 14.2
triangle = Shape("triangle", 3);
rectangle = Shape("rectangle", 4);
circle = Shape("circle", 0);

fprintf("\nExercise 14.2\n-------------\n")
fprintf("%s\n", triangle.name)
fprintf("%d\n", triangle.number_of_edges)
fprintf("%s\n", rectangle.name)
fprintf("%d\n", rectangle.number_of_edges)
fprintf("%s\n", circle.name)
fprintf("%d\n", circle.number_of_edges)

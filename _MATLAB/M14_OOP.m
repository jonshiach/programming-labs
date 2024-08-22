% =========================================================================
% 14. Object Orientated Programming
% =========================================================================

fprintf("\n14. Object Orientated Programming\n---------------------------------\n")

% 14.1 Classes
joel = Member;

fprintf("\n14.1 Classes\n------------\n")
fprintf("%s\n", joel.name)
fprintf("%d\n", joel.ID)

% 14.1.1 Changing the properties
ellie = Member;

fprintf("\n14.1.1 Changing the properties\n------------------------------\n")
fprintf("%s\n", ellie.name)
fprintf("%d\n", ellie.ID)

ellie.name = "Ellie Williams";
ellie.ID = 24123456;

fprintf("\n")
fprintf("%s\n", ellie.name)
fprintf("%d\n", ellie.ID)

% 14.1.2 Constructors
tommy = Member("Tommy Miller", 87654321);

fprintf("\n14.1.2 Constructors\n-------------------\n")
fprintf("%s\n", tommy.name)
fprintf("%d\n", tommy.ID)
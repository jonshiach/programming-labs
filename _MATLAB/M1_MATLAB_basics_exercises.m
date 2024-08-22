% =========================================================================
% 8. MATLAB Basics Exercises
% =========================================================================

fprintf("\n8. MATLAB Basics Exercises\n--------------------------")


% Exercise 8.4
fprintf("\nExercise 8.4\n------------")

fahrenheit = 100;
centigrade = 5 / 9 * (fahrenheit - 32);

fprintf("\n%0.2f in Fahrenheit is equivalent to %0.2f in centigrade\n", ...
    fahrenheit, centigrade)

% ------------------------------------------------------------------------
% Exercise 8.5
fprintf("\nExercise 8.5\n------------")

% Enter the number of seconds
initial_seconds = 1000000000;

% Calculate conversion values
seconds = initial_seconds;
seconds_in_a_minute = 60;
seconds_in_an_hour = 60 * seconds_in_a_minute;
seconds_in_a_day = 24 * seconds_in_an_hour;
seconds_in_a_week = 7 * seconds_in_a_day;
seconds_in_a_year = 365 * seconds_in_a_day;

% Number of years in the seconds
years = fix(seconds / seconds_in_a_year);
seconds = seconds - years * seconds_in_a_year;

% Number of weeks in the seconds remaining
weeks = fix(seconds / seconds_in_a_week);
seconds = seconds - weeks * seconds_in_a_week;

% Number of days in the seconds remaining
days = fix(seconds / seconds_in_a_day);
seconds = seconds - days * seconds_in_a_day;

% Number of hours in the seconds remaining
hours = fix(seconds / seconds_in_an_hour);
seconds = seconds - hours * seconds_in_an_hour;

% Number of minutes in the seconds remaining
minutes = fix(seconds / seconds_in_a_minute);
seconds = seconds - minutes * seconds_in_a_minute;

% Print the result
fprintf("\nThe are %d years, %d weeks, %d days, %d hours, %d minutes" + ...
    " and %d seconds in %d seconds", years, weeks, days, hours, ...
    minutes, seconds, initial_seconds)

% ------------------------------------------------------------------------
% Exercise 8.6

% Details of the loan
value   = 200000;
years    = 20;
interest = 4;

% Calculate number of months and monthly interest
months = 12 * years;
monthly_interest = interest / 100 / 12;

% Calculate repayment
repayment = monthly_interest * value / (1 - (1 + monthly_interest) ^ (-months));

% Print loan details and repayment amount 
fprintf("\nLoan repayment calculator\n-------------------------\n")
fprintf("Loan amount          : £%0.2f\n", value)
fprintf("Loan duration        : %i years\n", years)
fprintf("Annual interest rate : %0.2f%\n", interest)
fprintf("\nMonthly repayment    : £%0.2f\n", repayment)
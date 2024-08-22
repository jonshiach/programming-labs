% =========================================================================
% 13. Plotting
% =========================================================================

fprintf("\n13. Plotting\n------------\n")

% 13.1 linspace function
fprintf("\n13.1 linspace function \n----------------------")
x = linspace(-2, 2, 10)

% 13.1 Line plot
x = linspace(-2, 2, 50);
y = x .^ 2;

plot(x, y)

exportgraphics(gca, '../programming-labs/_images/13_Line_plot_2.png','Resolution',300)

% 13.1.1
plot(x, y, 'b-o')

exportgraphics(gca, '../programming-labs/_images/13_Line_plot_3.png','Resolution',300)

xlabel('x')
ylabel('y')
title('y = x^2')

exportgraphics(gca, '../programming-labs/_images/13_Line_plot_4.png','Resolution',300)

xlabel('x', fontsize=16)
ylabel('y', fontsize=16)
title('y = x^2', fontsize=20, Color='red')

exportgraphics(gca, '../programming-labs/_images/13_Line_plot_5.png','Resolution',300)

xlabel('$x$', FontSize=16, Interpreter='latex')
ylabel('$y$', FontSize=16, Interpreter='latex')
title('$y = x^2$', FontSize=20, Color='red', Interpreter='latex')

exportgraphics(gca, '../programming-labs/_images/13_Line_plot_6.png','Resolution',300)

% 13.1.3 Saving a plot to a file
saveas(gcf, 'my_plot.png')

% 13.1.4.1 Setting the axis scale
xlim([0, 2])
ylim([-1, 5])

exportgraphics(gca, '../programming-labs/_images/13_Line_plot_7.png','Resolution',300)

% 13.1.4.2 Axis properties
axis equal

exportgraphics(gca, '../programming-labs/_images/13_Line_plot_8.png','Resolution',300)

% 13.2 Multiple plots on the same axes
x = linspace(-2, 2, 100);
y1 = x .^ 2;
y2 = x .^ 3;
y3 = x .^ 4;

plot(x, y1)
hold on
plot(x, y2)
plot(x, y3)
hold off
xlabel('$x$', FontSize=16, Interpreter='latex')
ylabel('$y$', FontSize=16, Interpreter='latex')

exportgraphics(gca, '../programming-labs/_images/13_Multiple_plots_1.png','Resolution',300)

% 13.2.1 Legends
legend('$y = x^2$', '$y = x^3$', '$y = x^4$', FontSize=14, Interpreter='latex', Location='southeast')

exportgraphics(gca, '../programming-labs/_images/13_Multiple_plots_2.png','Resolution',300)

% 13.3 Scatter plots
x = rand(1, 100);
y = rand(1, 100);

scatter(x, y, 'r')
xlabel('$x$', FontSize=16, Interpreter='latex')
ylabel('$y$', FontSize=16, Interpreter='latex')

exportgraphics(gca, '../programming-labs/_images/13_Scatter_plot_1.png','Resolution',300)

% 13.4 Meshgrid
x = linspace(0, 4, 5);
y = linspace(0, 3, 4);
[X, Y] = meshgrid(x, y);

fprintf("Mesh grid\n---------\n")
x
y
X
Y

% 13.4 Surface plots
x = linspace(-1, 1, 30);
y = linspace(-1, 1, 30);
[X, Y] = meshgrid(x, y);
Z = sin(pi * X) .* sin(pi * Y);

surf(X, Y, Z)
xlabel('$x$', FontSize=16, Interpreter='latex')
ylabel('$y$', FontSize=16, Interpreter='latex')
title('$f(x,y) = \sin(\pi x)\sin(\pi y)$', FontSize=20, Interpreter='latex')
colormap(jet)

exportgraphics(gca, '../programming-labs/_images/13_Surface_plot_1.png','Resolution',300)

colormap(winter)

exportgraphics(gca, '../programming-labs/_images/13_Surface_plot_2.png','Resolution',300)

surf(X, Y, Z, EdgeColor='w')
xlabel('$x$', FontSize=16, Interpreter='latex')
ylabel('$y$', FontSize=16, Interpreter='latex')
title('$f(x,y) = \sin(\pi x)\sin(\pi y)$', FontSize=20, Interpreter='latex')
colormap(jet)

exportgraphics(gca, '../programming-labs/_images/13_Surface_plot_3.png','Resolution',300)

% 13.4.3 View angle
view(30,20)

exportgraphics(gca, '../programming-labs/_images/13_Surface_plot_4.png','Resolution',300)

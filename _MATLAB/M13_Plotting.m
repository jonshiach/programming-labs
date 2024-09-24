% % 13. Plotting
% 
% clear % Clear all variables
% clc   % Clear command window
% 
% % linspace function
% x = linspace(-2, 2, 10)
% 
% % Line plot
% x = linspace(-2, 2, 50);
% y = x .^ 2;
% 
% plot(x, y)
% 
% exportgraphics(gca, '../_images/13_Line_plot_2.png','Resolution',300)
% 
% % Linespec
% plot(x, y, 'b-o')
% 
% exportgraphics(gca, '../_images/13_Line_plot_3.png','Resolution',300)
% 
% % Axis label and title
% xlabel('x')
% ylabel('y')
% title('y = x^2')
% 
% exportgraphics(gca, '../_images/13_Line_plot_4.png','Resolution',300)
% 
% xlabel('x', fontsize=16)
% ylabel('y', fontsize=16)
% title('y = x^2', fontsize=20, Color='red')
% 
% exportgraphics(gca, '../_images/13_Line_plot_5.png','Resolution',300)
% 
% xlabel('$x$', FontSize=16, Interpreter='latex')
% ylabel('$y$', FontSize=16, Interpreter='latex')
% title('$y = x^2$', FontSize=20, Color='red', Interpreter='latex')
% 
% exportgraphics(gca, '../_images/13_Line_plot_6.png','Resolution',300)
% 
% % Saving a plot to a file
% saveas(gcf, 'my_plot.png')
% 
% % Setting the axis scale
% xlim([0, 2])
% ylim([-1, 5])
% 
% exportgraphics(gca, '../_images/13_Line_plot_7.png','Resolution',300)
% 
% % Axis properties
% axis equal
% 
% exportgraphics(gca, '../_images/13_Line_plot_8.png','Resolution',300)
% 
% % Multiple plots on the same axes
% x = linspace(-2, 2, 100);
% y1 = x .^ 2;
% y2 = x .^ 3;
% y3 = x .^ 4;
% 
% clf
% hold on
% plot(x, y1)
% plot(x, y2)
% plot(x, y3)
% hold off
% xlabel('$x$', FontSize=16, Interpreter='latex')
% ylabel('$y$', FontSize=16, Interpreter='latex')
% 
% exportgraphics(gca, '../_images/13_Multiple_plots_1.png','Resolution',300)
% 
% % Legends
% legend('$y = x^2$', '$y = x^3$', '$y = x^4$', FontSize=14, Interpreter='latex', Location='southeast')
% 
% exportgraphics(gca, '../_images/13_Multiple_plots_2.png','Resolution',300)
% 
% % Scatter plots
% x = rand(1, 100);
% y = rand(1, 100);
% 
% clf
% scatter(x, y, 'r')
% xlabel('$x$', FontSize=16, Interpreter='latex')
% ylabel('$y$', FontSize=16, Interpreter='latex')
% 
% exportgraphics(gca, '../_images/13_Scatter_plot_1.png','Resolution',300)
% 
% % Meshgrid
% x = linspace(0, 4, 5);
% y = linspace(0, 3, 4);
% [X, Y] = meshgrid(x, y);
% x
% y
% X
% Y
% 
% % Surface plots
% x = linspace(-1, 1, 30);
% y = linspace(-1, 1, 30);
% [X, Y] = meshgrid(x, y);
% Z = sin(pi * X) .* sin(pi * Y);
% 
% clf
% surf(X, Y, Z)
% xlabel('$x$', FontSize=16, Interpreter='latex')
% ylabel('$y$', FontSize=16, Interpreter='latex')
% title('$f(x,y) = \sin(\pi x)\sin(\pi y)$', FontSize=20, Interpreter='latex')
% colormap(jet)
% 
% exportgraphics(gca, '../_images/13_Surface_plot_1.png','Resolution',300)
% 
% colormap(winter)
% 
% exportgraphics(gca, '../_images/13_Surface_plot_2.png','Resolution',300)
% 
% surf(X, Y, Z, EdgeColor='w')
% xlabel('$x$', FontSize=16, Interpreter='latex')
% ylabel('$y$', FontSize=16, Interpreter='latex')
% title('$f(x,y) = \sin(\pi x)\sin(\pi y)$', FontSize=20, Interpreter='latex')
% colormap(jet)
% 
% exportgraphics(gca, '../_images/13_Surface_plot_3.png','Resolution',300)
% 
% % View angle
% view(30,20)
% 
% exportgraphics(gca, '../_images/13_Surface_plot_4.png','Resolution',300)
% 
% % Contour plots
% clf
% contour(X, Y, Z)
% xlabel('$x$', FontSize=16, Interpreter='latex')
% ylabel('$y$', FontSize=16, Interpreter='latex')
% 
% exportgraphics(gca, '../_images/13_Contour_plot_1.png','Resolution',300)
% 
% contour(X, Y, Z, 15)
% 
% exportgraphics(gca, '../_images/13_Contour_plot_2.png','Resolution',300)
% 
% % Contour labels
% clf
% [C,h] = contour(X, Y, Z);
% clabel(C, h)
% xlabel('$x$', FontSize=16, Interpreter='latex')
% ylabel('$y$', FontSize=16, Interpreter='latex')
% 
% exportgraphics(gca, '../_images/13_Contour_plot_3.png','Resolution',300)

% Image plots
img = 255 * rand(10);
image(img)

exportgraphics(gca, '../_images/13_Image_plot_1.png','Resolution',300)

axis equal tight
exportgraphics(gca, '../_images/13_Image_plot_2.png','Resolution',300)

% Reading an image file
img = imread('flower.jpg');

% Determine the size of the image in pixels
[height, width, colours] = size(img);
fprintf('\nwidth       : %i\n', width)
fprintf('height      : %i\n', height)
fprintf('no. colours : %1i\n', colours)

% Plot the image
image(img)
axis equal tight

exportgraphics(gca, '../_images/13_Image_plot_3.png','Resolution',300)

% Image processing
img2 = img;
img2(:,:,1) = 0;
image(img2)
axis equal tight

exportgraphics(gca, '../_images/13_Image_plot_4.png','Resolution',300)
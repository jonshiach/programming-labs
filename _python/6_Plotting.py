# 6. Plotting

# The linspace function
import numpy as np

x = np.linspace(-2, 2, 10)

print(x)

# Line plot
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 10)
y = x ** 2

fig, ax = plt.subplots()
plt.plot(x, y)
plt.savefig('../_images/6_Line_plot_1.png', dpi=300)
plt.show()

x = np.linspace(-2, 2, 50)
y = x ** 2
plt.plot(x, y)
plt.savefig('../_images/6_Line_plot_2.png', dpi=300)
plt.show()

# Plot styles
fig, ax = plt.subplots()
plt.plot(x, y, 'b-o')
plt.savefig('../_images/6_Line_plot_3.png', dpi=300)
plt.show()

# Axis labels and titles
fig, ax = plt.subplots()
plt.plot(x, y, 'b-o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2')
plt.savefig('../_images/6_Line_plot_4.png', dpi=300)
plt.show()

# Font properties
fig, ax = plt.subplots()
plt.plot(x, y, 'b-o')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('y = x^2', fontsize=16, color='red')
plt.savefig('../_images/6_Line_plot_5.png', dpi=300)
plt.show()

# LaTeX in labels
fig, ax = plt.subplots()
plt.plot(x, y, 'b-o')
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.title('$y = x^2$', fontsize=16, color='red')
plt.savefig('../_images/6_Line_plot_6.png', dpi=300)
plt.show()

# Save plot to file
fig.savefig('myplot.png')

# Axis limits
fig, ax = plt.subplots()
plt.plot(x, y, 'b-o')
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.title('$y = x^2$', fontsize=16, color='red')
plt.xlim(0, 2)
plt.ylim(-1, 5)
plt.savefig('../_images/6_Line_plot_7.png', dpi=300)
plt.show()

# Aspect ratio
fig, ax = plt.subplots()
plt.plot(x, y, 'b-o')
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.title('$y = x^2$', fontsize=16, color='red')
ax.set_aspect(0.25)
plt.savefig('../_images/6_Line_plot_8.png', dpi=300)
plt.show()

# Multiple plots on the same axes
x = np.linspace(-2, 2, 100)
y1 = x ** 2
y2 = x ** 3
y3 = x ** 4

fig, ax = plt.subplots()
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.savefig('../_images/6_Multiple_plots_1.png', dpi=300)
plt.show()

# Adding a legend to a plot
fig, ax = plt.subplots()
plt.plot(x, y1, label='$y = x^2$')
plt.plot(x, y2, label='$y = x^3$')
plt.plot(x, y3, label='$y = x^4$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.savefig('../_images/6_Multiple_plots_2.png', dpi=300)
plt.show()

# Scatter plot
x = np.random.rand(100)
y = np.random.rand(100)

fig, ax = plt.subplots()
plt.scatter(x, y, color='r', marker='o')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.savefig('../_images/6_Scatter_plot_1.png', dpi=300)
plt.show()

# Mesh grid
x = np.linspace(0, 4, 5)
y = np.linspace(0, 3, 4)
X, Y = np.meshgrid(x, y)

print()
print(f"x = {x}")
print(f"y = {y}")
print(f"\nX = \n{X}")
print(f"\nY = \n{Y}")

# Plot surface
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.pi * X) * np.sin(np.pi * Y)

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('$f(x,y) = \sin(\pi x)\sin(\pi y)$')
plt.savefig('../_images/6_Surface_plot_1.png', dpi=300)
plt.show()

# Colormaps
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='jet')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('$f(x,y) = \sin(\pi x)\sin(\pi y)$')
plt.savefig('../_images/6_Surface_plot_2.png', dpi=300)
plt.show()

# Line colour
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='jet', edgecolor='k')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('$f(x,y) = \sin(\pi x)\sin(\pi y)$')
plt.savefig('../_images/6_Surface_plot_3.png', dpi=300)
# plt.show()

# View angle
ax.view_init(elev=20,azim=30)
plt.show()

# Contour plot
fig, ax = plt.subplots()
plt.contour(X, Y, Z)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.savefig('../_images/6_Contour_plot_1.png', dpi=300)
plt.show()

# Contour lines
fig, ax = plt.subplots()
plt.contour(X, Y, Z, 15)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.savefig('../_images/6_Contour_plot_2.png', dpi=300)
plt.show()

# Contour labels
fig, ax = plt.subplots()
my_contour = plt.contour(X, Y, Z, 12)
ax.clabel(my_contour)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.savefig('../_images/6_Contour_plot_3.png', dpi=300)
plt.show()

# Image plots
img = np.random.rand(10, 10)

plt.imshow(img)
plt.savefig('../_images/6_Image_plot_1.png', dpi=300)
plt.show()

# Reading an image file
import matplotlib.image as mpimg

img = mpimg.imread('flower.jpg')

# Determine figure size based on the image size
height, width, colours = img.shape

print()
print(f"width       : {width}\nheight      : {height}\nno. colours : {colours}")

# Plot image
plt.imshow(img)
plt.savefig('../_images/6_Image_plot_2.png', dpi=300)
plt.show()

# Image processing
img2 = np.copy(img)
img2[:,:,0] = 0

plt.imshow(img2)
plt.savefig('../_images/6_Image_plot_3.png', dpi=300)
plt.show()

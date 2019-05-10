# -*- coding: utf-8 -*-
"""
Created on Wed May  1 17:30:15 2019

@author: Devadasan Kizhapat

This is a Python script file for creating sample plots.

Using numpy and matplotlib modules
"""

# pip install mumpy
# pip install matplotlib

my_data_dir = 'D:\\Personal\\Python and R\\Python Codes\\Data\\'

import numpy as np
import matplotlib.pyplot as plt


# Line Plots

"""
print ('\nCreating line plot with yvals against xvals')
xvals = np.arange(-2, 1, 0.01) # Grid of 0.01 spacing from -2 to 10
yvals = np.sin(xvals) # Evaluate function on xvals

plt.plot(xvals, yvals) # Create line plot with yvals against xvals
plt.show()



print ('\nCreating line plot with red dashed line')
newyvals = 1 - 0.5 * xvals**2 # Evaluate quadratic approximation on xvals

plt.plot(xvals, newyvals, 'g--') # Create line plot with red dashed line
plt.title('Sample line plots')
plt.xlabel('Input')
plt.ylabel('Function values')
plt.show()


# Contour Plots


print ('\nCreating contour plots')
plt.figure() # Create a new figure window
xlist = np.linspace(-2.0, 1.0, 100) # Create 1-D arrays for x,y dimensions
ylist = np.linspace(-1.0, 2.0, 100)
X,Y = np.meshgrid(xlist, ylist) # Create 2-D grid xlist,ylist values
Z = np.sqrt(X**2 + Y**2)

plt.contour(X, Y, Z, [0.5, 1.0, 1.2, 1.5], colors = 'r', linestyles = 'solid')
plt.show()
"""
"""

# Setting the axes of the plot

"""
print ('\nSetting the axes of the plot')
plt.axes().set_aspect('equal') # Scale the plot size to get same aspect ratio
plt.axis([-1.0, 1.0, -0.5,0.5]) # Set axis limits

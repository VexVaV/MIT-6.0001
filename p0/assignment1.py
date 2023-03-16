#The goal of this programming exercise is to make sure your python and numpy installations are correct, 
# to get you more comfortable with using Spyder, and to begin using simple elements of Python. 
# Standard elements of a program include the ability to print out results (using the print operation), 
# the ability to read input from a user at the console (for example using the input function), 
# and the ability to store values in a variable, so that the program can access that value as needed.

import numpy

x_number = input("Enter number x: ")
x_number = int(x_number)
y_number = input("Enter number y: ")
y_number = int(y_number)
raised_to_power = x_number ** y_number
print("X**y = ", raised_to_power)
log = numpy.log2(x_number)
print("log(x) = ", x_number)
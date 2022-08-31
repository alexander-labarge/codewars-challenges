#!/usr/bin/env python3
""" This module completes the addition operation of two numbers inputed
by the user, and returns the result.
"""

__author__ = "Alexander La Barge"
__copyright__ = "Copyright 2022"
__date__ = "2022/08/31"
__deprecated__ = False
__email__ =  "labargeam@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "Alexander La barge"
__status__ = "Production"
__version__ = "0.0.1"

def main():  
  xvalue,yvalue = get_userinput()
  # this means -- xvalue =x, returned from the function, and yvalue =y returned
  print('Numbers are: ', xvalue,yvalue)
  # Define added to the result of add_numbers with arguments passed through the 
  # parameter
  added = add_numbers(xvalue,yvalue)
  print('The numbers added are: ', added)

# x, y returned as result of function get_userinput, and then = xvalue, and yvalue
# respectively  
def get_userinput():
  while True:
    try:
      x = int(input('Enter a number for x: '))
      y = int(input('Enter a number for y: '))
      return x, y
    except:
      print('You must enter an integer. Try again.')

# This function takes any two numbers which can be stored as variables
# but must be in the format, somenumber, somenumber2 like xvalue, yvalue above
# xvalue and yvalue then essentially become x and y
# The result of the addition is stored as add, and then returned as added
def add_numbers(x,y):
  print('x = ', x)
  print('y = ', y)
  add = x + y
  return add

# prevents the running of this file, unless it is the main file in the interpreter
if __name__ == "__main__":
    main()
else:
  print('This file is not being called as main')

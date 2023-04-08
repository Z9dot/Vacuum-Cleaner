#!/usr/bin/env python
# coding: utf-8

# In[1]:
import TableDrivenAgentClass as tda
import SimpleReflexAgentClass as sfa


def display_environment(data, r):
    # Prints column indices
    print("  ", end="")
    for i in range(r):
        print(f"  {i}", end="")
    # move to next line
    print()

    # Prints rows with row indices and their corresponding data values
    for i in range(r):
        # Prints row index
        print(f" {i} ", end="")
        # Prints data values in row
        for j in range(r):
            # Prints data value with two spaces
            print(f" {data[i][j]:2}", end="")
        # move to next line
        print()


# take the original matrix from TableDrivenAgentClass and store it in environment to use it in my program
environment = tda.environment
print("The Dirty Environment")
display_environment(environment, 10)

# In[2]:


while True:
    row = 0
    col = 0

    # this condition to check index is between 1 and 9, and to check its in wall or not
    if all(s in range(0, 10) for s in (row, col)) and environment[row][col] != '#':
        break  # if user but valid input the while loop well stop
    else:
        print("The position is not empty or out of range \nPlease try again!")

# Pattern of directions to control vacuum
direction = 'RRRDDLLUDRRRRRURLDDLDDDRDDLLLLULUU'
# this code to convert string to list :example string = 'ABC' , the list = ['A' , 'B' , 'C']
directions = [*direction]
# #### Start clean

# In[3]:

# after import TableDrivenAgentClass we use it to create object named tdaClass
tdaClass = tda.TableDrivenAgent(row, col, directions)
print("\n----------Table Driven Agent----------\n")
print('\tActions\t\t\t\tScore')
tdaClass.start_clean(environment)  # use object we created to call method start_clean
print("The Cleaned Environment")
display_environment(environment, 10)

# In[4]:

environment = sfa.environment
print("\nThe Dirty Environment")
display_environment(environment, 10)

# after import SimpleReflexAgentClass we use it to create object named sfaClass
sfaClass = sfa.SimpleReflexAgent(row, col)
print("\n----------Simple Reflex Agent----------\n")
print('\tActions\t\t\t\tScore')
sfaClass.start_clean(environment)  # use object we created to call method start_clean
print("The Cleaned Environment")
display_environment(environment, 10)

#!/usr/bin/env python
# coding: utf-8

# In[1]:

import random

environment = [['', '*', '*', '*', '', '', '#', '', '', ''],  # original matrix
               ['', '*', '#', '', '#', '', '', '*', '', ''],
               ['', '*', '', '*', '', '*', '*', '#', '#', '#'],
               ['#', '', '', '', '#', '', '', '', '', '#'],
               ['', '', '#', '#', '', '', '#', '', '', ''],
               ['', '*', '', '', '', '', '#', '', '', '#'],
               ['#', '', '', '#', '', '', '*', '#', '', '#'],
               ['#', '*', '', '#', '', '#', '', '', '', ''],
               ['', '#', '', '*', '', '*', '', '#', '', '#'],
               ['', '', '', '#', '', '', '#', '', '', '#'],
               ]


def DisplayEnvironment(r):
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
            print(f" {environment[i][j]:2}", end="")
        # move to next line
        print()


def CountDirt():
    counter = 0
    for i in range(10):
        for j in range(10):
            if environment[i][j] == '*':
                counter += 1
    return counter


class SimpleReflexAgent:
    def __init__(self, row, col):
        self.row = row  # declare variables and assign them to variables we get it from parameter
        self.col = col
        self.performance_measure = 0  # declare variables and assign them to initial values
        self.possibleToMove = True

    def moveLeft(self):  # this method to move vacuum left
        if self.col > 0 and environment[self.row][self.col - 1] != '#':  # check if it is possible to move left or not
            self.performance_measure += 1
            print('\nVacuum move left\t\t\t+1')
            self.col -= 1
        else:
            self.performance_measure += 3
            print('\nVacuum can not move left\t\t+3')
            # if it is not possible to move left will assign possibleToMove variable to false to stop program
            self.possibleToMove = False

    def moveRight(self):  # this method to move vacuum right
        if self.col < 9 and environment[self.row][self.col + 1] != '#':  # check if it is possible to move right or not
            self.performance_measure += 1
            print('\nVacuum move right\t\t\t+1')
            self.col += 1
        else:
            self.performance_measure += 3
            print('\nVacuum can not move right\t\t+3')
            self.possibleToMove = False
        if self.col == 9:
            self.col = 0
            self.row = random.randint(0, 9)

    def moveUp(self):  # this method to move vacuum up
        if self.row > 0 and environment[self.row - 1][self.col] != '#':  # check if it is possible to move up or not
            self.performance_measure += 1
            print('\nVacuum move up\t\t\t\t+1')
            self.row -= 1
        else:
            self.performance_measure += 3
            print('\nVacuum can not move up\t\t\t+3')
            self.possibleToMove = False

    def moveDown(self):  # this method to move vacuum down
        if self.row < 9 and environment[self.row + 1][self.col] != '#':  # check if it is possible to move down or not
            self.performance_measure += 1
            print('\nVacuum move down\t\t\t+1')
            self.row += 1
        else:
            self.performance_measure += 3
            print('\nVacuum can not move down\t\t+3')
            self.possibleToMove = False
        if self.row > 9:
            self.row = random.randint(0, 9)
            self.col = 0

    def start_clean(self, my_environment):  # this main method to start clean
        dirt = CountDirt()  # counter for cleaned spots
        direction = 'right'  # starts by moving down by default
        while dirt > 0:

            if self.isDirty(my_environment):  # if the current cell is dirty suck
                self.suck(my_environment)
                dirt -= 1

            if self.possibleToMove is False:  # chooses a random direction when it can't move forward
                direction = SimpleReflexAgent.Turn(direction)
                print("Changing direction to " + direction)
                self.possibleToMove = True
                if direction == 'left':
                    self.moveLeft()
                elif direction == 'up':
                    self.moveUp()
                elif direction == 'down':
                    self.moveDown()
            else:
                self.moveRight()

            direction = 'right'
        print('\nTotal\t\t\t\t\t{}'.format(self.performance_measure))

    def isDirty(self, my_environment):
        # condition to check if the cell content is * or not where * represent as dirty
        if my_environment[self.row][self.col] == '*':
            return True
        else:
            return False

    def suck(self, my_environment):
        self.performance_measure += 5
        print('\nThe dirty at {}.{} has been cleaned\t+5'.format(self.row, self.col))
        my_environment[self.row][self.col] = ''  # remove * to be clean

    @classmethod
    def Turn(cls, direction):
        num = random.randint(0, 1)
        if direction == 'right':
            dlist = ['up', 'down']
            direction = dlist[num]
        elif direction == 'left':
            dlist = ['up', 'down']
            direction = dlist[num]
        elif direction == 'up':
            direction = 'up'
        elif direction == 'down':
            direction = 'down'
        return direction

# In[ ]:

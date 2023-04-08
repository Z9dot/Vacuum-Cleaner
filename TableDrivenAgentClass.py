#!/usr/bin/env python
# coding: utf-8

# In[1]:


environment = [['', '*', '*', '*', '', '', '#', '', '', ''],  # original matrix
               ['', '*', '#', '', '#', '', '', '*', '', ''],
               ['', '*', '', '*', '', '*', '*', '#', '#', '#'],
               ['#', '', '', '', '#', '', '', '', '', '#'],
               ['',  '', '#', '#', '', '', '#', '', '', ''],
               ['', '*', '', '', '', '', '#', '', '', '#'],
               ['#', '', '', '#', '', '', '*', '#', '', '#'],
               ['#', '*', '', '#', '', '#', '', '', '', ''],
               ['', '#', '', '*', '', '*', '', '#', '', '#'],
               ['', '', '', '#', '', '', '#', '', '', '#'],
               ]


class TableDrivenAgent:
    def __init__(self, row, col, directions):
        self.row = row  # declare variables and assign them to variables we get it from parameter
        self.col = col
        self.directions = directions
        self.performance_measure = 0  # declare variables and assign them to initial values
        self.possibleToMove = True

    def moveLeft(self):  # this method to move vacuum left
        if self.col > 1 and environment[self.row][self.col - 1] != '#':  # check if it is possible to move left or not
            self.performance_measure += 1
            print('\nVacuum move left\t\t+1')
            self.col -= 1
        else:
            self.performance_measure += 3
            print('\nVacuum can not move left\t\t\t+1')
            # if it is not possible to move left will  assign possibleToMove variable to false to stop program
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

    def moveUp(self):  # this method to move vacuum up
        if self.row > 1 and environment[self.row - 1][self.col] != '#':  # check if it is possible to move up or not
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
            print('\nVacuum can not move down\t\t\t+3')
            self.possibleToMove = False

    def start_clean(self, my_environment):  # this main method to start clean
        for direction in self.directions:  # for loop to get all directions to move
            if self.isDirty(my_environment):  # if the sell dirty will  suck
                self.suck(my_environment)
            if direction == 'L':
                self.moveLeft()
            elif direction == 'R':
                self.moveRight()
            elif direction == 'U':
                self.moveUp()
            elif direction == 'D':
                self.moveDown()
            if self.possibleToMove is False:
                break  # if it is not possible to move stop program
        if self.isDirty(my_environment):  # i but this method here to clean last cell if it is dirty
            self.suck(my_environment)
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

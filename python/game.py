# Copyright (c) 2015, RetailNext, Inc.
# This material contains trade secrets and confidential information of
# RetailNext, Inc.  Any use, reproduction, disclosure or dissemination
# is strictly prohibited without the explicit written permission
# of RetailNext, Inc.
# All rights reserved.

import sys
from random import randint

class Game:

    def __init__(self, w, h, mine_count):

        self.grid = [[0 for x in range(w)] for x in range(h)]

        random_result =0
        row = 0
        col = 0
        i =0
        j = 0
        neighbor_mines = 0


        print >> sys.stderr, "w = %d, h = %d, mine_count = %d" % (w, h, mine_count)

        while mine_count > 0:
            random_row = randint(0,h-1) 
            random_col = randint(0,w-1) 
            if self.grid[random_row][random_col] != -1:
                self.grid[random_row][random_col] = -1
                mine_count -= 1


        #walk grid 
        for row in range(h):
           for col in range(w):

               if self.grid[row][col] != -1:

                   if col == 0:
                       col_lb = 0
                       col_ub = col + 1
                   elif col >0 and col <w -1:
                       col_lb = col - 1
                       col_ub = col + 1
                   elif col == w - 1:
                       col_lb = col -1
                       col_ub = w - 1                   

                   if row == 0:
                       row_lb = 0
                       row_ub = row + 1
                   elif row >0 and row <h -1:
                       row_lb = row - 1
                       row_ub = row + 1
                   elif row == h - 1:
                       row_lb = row -1
                       row_ub = h - 1

                   neighbor_mines = 0
                   for i in range(row_lb, row_ub):
                       for j in range(col_lb, col_ub):
                           if self.grid[i][j] == -1:
                               neighbor_mines += 1

                   self.grid[row][col] = neighbor_mines




    # reveal takes coordinates and returns the number
    # of mines surrounding the cell, or -1 if there
    # is a mine in that cell
    def reveal(self, x, y):


        return self.grid[x][y]

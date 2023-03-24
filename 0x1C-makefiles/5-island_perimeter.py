#!/usr/bin/python3
""" this module calculates the perimetr of en island """


def island_perimeter(grid):
    """ calculates the perimeter ofthe island grid """

    perimeter = 0
    num_of_land = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                num_of_land += 1

    perimeter = 2*num_of_land + 2

    return perimeter            

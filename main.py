#!/usr/bin/env python2
import grid
import astar
import sys

# Algorithm References:
# http://www.redblobgames.com/pathfinding/a-star
# http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
# https://en.wikipedia.org/wiki/A*_search_algorithm

def main():

    #Decide if default args have been set
    if len(sys.argv) >1:
        matrix = grid.Grid(sys.argv[1])
    else:
        matrix = grid.Grid(sys.argv[0])

    matrix.draw_grid()

    block = '1'
    while block == '1':
        block = raw_input("Do you want to insert path blockades? (1 for yes, 0 for no): ")
        if block == '1':
            matrix.place_block()
            matrix.draw_grid()

    #instantiate astar class

    goal_x, goal_y = matrix.get_goal()
    start_x, start_y = matrix.get_start()

    startTuple = matrix.start_x, matrix.start_y
    goalTuple = matrix.goal_x, matrix.goal_y
    alg = astar.Astar(startTuple,goalTuple)
    print ("Astar algorithm........")
    count = alg.astar_search(matrix,startTuple,goalTuple)
    print("Number of steps taken: ", count)

    matrix.draw_grid()
    return 0


if __name__ == '__main__':
    main()

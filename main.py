import grid
import astar

# References:
# http://www.redblobgames.com/pathfinding/a-star
# http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html

def main():
    matrix = grid.Grid()


    matrix.draw_grid()

    x, y = matrix.get_goal()
    print("x: ", x)

    block = '1'
    while block == '1':
        block = raw_input("Do you want to insert path blockades? (1 for yes, 0 for no): ")
        if block == '1':
            matrix.place_block()
            matrix.draw_grid()

    #instantiate astar class

    #alg = astar.Astar()
    #goal_x, goal_y = matrix.get_goal()
    #start_x, start_y = matrix.get_start()
    #alg.astar_search(matrix,start,goal )
    return 0


if __name__ == '__main__':
    main()

import grid
import astar

def main():
    matrix = grid.Grid()


    matrix.draw_grid()
    block = raw_input("Do you want to insert blockades? (1 for yes, 0 for no): ")
    if block == '1':
        matrix.place_block()
        matrix.draw_grid()

    #instantiate astar class
    #alg = astar.Astar(matrix.calc_pos_grid(matrix.goal_x, matrix.goal_y))
    #goal = matrix.goal_x, matrix.goal_y
    #start = matrix.start_x, matrix.start_y
    #alg.search(matrix,start,goal )
    return 0


if __name__ == '__main__':
    main()

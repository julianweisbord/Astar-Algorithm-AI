import grid
import astar

def main():
    matrix = grid.Grid()


    matrix.draw_grid()
    block = raw_input("Do you want to insert blockades? (1 for yes, 0 for no)")
    #if block == '1':
        #matrix.place_block()

    #instantiate astar class
    #alg = astar.Astar(matrix.calc_pos_grid(matrix.goal_x, matrix.goal_y))

    return 0


if __name__ == '__main__':
    main()

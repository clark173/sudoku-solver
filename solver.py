import sys

from puzzle_class import Puzzle

ROWS = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eigth', 'Ninth']
VALID_NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_initial_values(puzzle):
    print 'Enter the values by row. Seperate values by comma. For empty cells, input a 0.'

    puzzle.data_array[0] = [7,0,1,0,0,0,0,0,0]
    puzzle.data_array[1] = [2,0,0,0,4,6,0,0,0]
    puzzle.data_array[2] = [0,0,0,3,5,7,0,8,0]
    puzzle.data_array[3] = [3,0,0,5,0,0,6,9,0]
    puzzle.data_array[4] = [9,1,0,2,0,0,7,0,0]
    puzzle.data_array[5] = [4,0,0,0,8,0,2,0,0]
    puzzle.data_array[6] = [0,2,0,0,0,3,0,0,0]
    puzzle.data_array[7] = [0,0,7,0,1,0,0,0,0]
    puzzle.data_array[8] = [8,0,0,0,0,0,0,1,0]
    return

    for i in range(0,9):
        while True:
            break_statement = False
            try:
                row = raw_input('%s row: ' %(ROWS[i]))
            except KeyboardInterrupt:
                sys.exit(0)
            row = row.replace(' ', '').split(',')
            if len(row) != 9:
                print 'Only 9 values are allowed per row.'
                continue
            for value in row:
                if value not in VALID_NUMS:
                    print '%s is not a valid number. Try again.' %(value)
                    break_statement = True
                    break
            if break_statement:
                continue
            break
        row = map(int, row)
        puzzle.data_array[i] = row

def main():
    puzzle = Puzzle()
    get_initial_values(puzzle)
    print 'First Board:'
    puzzle.print_board()
    i = 0
    while True:
        rows_updated = puzzle.check_rows()
        puzzle.populate_grids()
        puzzle.update_grids()
        grids_updated = puzzle.check_grids()
        puzzle.update_grids()
        columns_updated = puzzle.check_columns()
        puzzle.update_grids()
        hor_tri_updated = puzzle.check_horizontal_tri_grid()
        puzzle.update_grids()
        ver_tri_updated = puzzle.check_vertical_tri_grid()
        puzzle.update_grids()

        solved = True
        for row in puzzle.data_array:
            if 0 in row:
                solved = False
                break
        if solved:
            print 'Solution Found'
            break
        if not rows_updated and not grids_updated and not columns_updated and not hor_tri_updated and not ver_tri_updated:
            print 'No changes made this iteration - No solution found'
            break
        i += 1
        print ''
        puzzle.print_board()
    puzzle.print_board()

if __name__ == "__main__":
    main()

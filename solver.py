import sys

from puzzle_class import Puzzle

ROWS = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eigth', 'Ninth']
VALID_NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_initial_values(puzzle):
    print 'Enter the values by row. Seperate values by comma. For empty cells, input a 0.'

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
    puzzle.populate_grids()
    puzzle.check_rows()
    puzzle.populate_grids()
    puzzle.print_board()

if __name__ == "__main__":
    main()

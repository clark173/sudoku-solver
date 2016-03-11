VALID_NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Puzzle:
    def __init__(self):
        self.data_array = [[0 for x in range(0,9)] for x in range(0,9)]
        self.grids = [[[0 for x in range(0,3)] for x in range(0,3)] for x in range(0,9)]
        self.grid_0 = [[0 for x in range(0,3)] for x in range(0,3)]
        self.grid_1 = [[0 for x in range(0,3)] for x in range(0,3)]
        self.grid_2 = [[0 for x in range(0,3)] for x in range(0,3)]
        self.grid_3 = [[0 for x in range(0,3)] for x in range(0,3)]
        self.grid_4 = [[0 for x in range(0,3)] for x in range(0,3)]
        self.grid_5 = [[0 for x in range(0,3)] for x in range(0,3)]
        self.grid_6 = [[0 for x in range(0,3)] for x in range(0,3)]
        self.grid_7 = [[0 for x in range(0,3)] for x in range(0,3)]
        self.grid_8 = [[0 for x in range(0,3)] for x in range(0,3)]
        self.populate_grids()

    def print_board(self):
        for row in self.data_array:
            print row

    def print_grids(self):
        i = 0
        for grid in self.grids:
            print '\nGrid: %s' %(i)
            for row in grid:
                print row
            i += 1

    def update_array_after_grids(self):
        self.data_array[0] = self.grids[0][0] + self.grids[1][0] + self.grids[2][0]
        self.data_array[1] = self.grids[0][1] + self.grids[1][1] + self.grids[2][1]
        self.data_array[2] = self.grids[0][2] + self.grids[1][2] + self.grids[2][2]
        self.data_array[3] = self.grids[3][0] + self.grids[4][0] + self.grids[5][0]
        self.data_array[4] = self.grids[3][1] + self.grids[4][1] + self.grids[5][1]
        self.data_array[5] = self.grids[3][2] + self.grids[4][2] + self.grids[5][2]
        self.data_array[6] = self.grids[6][0] + self.grids[7][0] + self.grids[8][0]
        self.data_array[7] = self.grids[6][1] + self.grids[7][1] + self.grids[8][1]
        self.data_array[8] = self.grids[6][1] + self.grids[7][2] + self.grids[8][2]

    def update_array_after_columns(self, column, num):
        for i in range(len(self.data_array)):
            self.data_array[i][num] = column[i]

    def check_grids(self):
        updated = False

        for grid in self.grids:
            row_count = 0
            grid_array = grid[0] + grid[1] + grid[2]
            for value in grid_array:
                if value in VALID_NUMS:
                    row_count += 1
            if row_count == 8:
                self.add_ninth_val_in_row(grid_array)
                grid[0] = grid_array[0:3]
                grid[1] = grid_array[3:6]
                grid[2] = grid_array[6:9]
                updated = True
        self.update_array_after_grids()
        return updated

    def check_columns(self):
        updated = False

        for i in range(len(self.data_array)):
            column = [row[i] for row in self.data_array]
            column_count = 0
            for value in column:
                if value in VALID_NUMS:
                    column_count += 1
            if column_count == 8:
                self.add_ninth_val_in_row(column)
                updated = True
                self.update_array_after_columns(column, i)

        self.populate_grids()
        return updated

    def populate_grids(self):
        k = 0
        for i in range(0,3):
            for j in range(0,3):
                self.grids[i*3][j] = self.data_array[k][0:3]
                self.grids[(i*3)+1][j] = self.data_array[k][3:6]
                self.grids[(i*3)+2][j] = self.data_array[k][6:9]
                k += 1

    def add_ninth_val_in_row(self, row):
        missing = 0
        vals_in_row = []

        for value in row:
            if value != 0:
                vals_in_row.append(value)

        for value in VALID_NUMS:
            if value not in vals_in_row:
                missing = value
                break

        row[row.index(0)] = missing

    def check_rows(self):
        updated = False

        for row in self.data_array:
            row_count = 0
            for value in row:
                if value in VALID_NUMS:
                    row_count += 1
            if row_count == 8:
                self.add_ninth_val_in_row(row)
                updated = True
        self.populate_grids()
        return updated

if __name__ == "__main__":
    puzzle = Puzzle()

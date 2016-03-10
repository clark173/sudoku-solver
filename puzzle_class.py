VALID_NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Puzzle:
    def __init__(self):
        self.data_array = [[0 for x in range(0,9)] for x in range(0,9)]
        self.grids = [[[0 for x in range(0,3)] for x in range(0,3)]] * 9
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

    def populate_grids(self):
        for i in range(0,3):
            self.grids[i*3][i] = self.data_array[i*3][0:3]
            #print self.grids[i*3], self.data_array[i*3]
            self.grids[(i*3)+1][i] = self.data_array[(i*3)+1][3:6]
            self.grids[(i*3)+2][i] = self.data_array[(i*3)+2][6:9]

        for i in range(len(self.grids)):
            print '\nGrid %s' %i
            for row in self.grids[i]:
                print row

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
        for row in self.data_array:
            row_count = 0
            for value in row:
                if value in VALID_NUMS:
                    row_count += 1
            if row_count == 8:
                self.add_ninth_val_in_row(row)

if __name__ == "__main__":
    puzzle = Puzzle()

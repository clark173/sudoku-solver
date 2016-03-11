VALID_NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Puzzle:
    def __init__(self):
        self.data_array = [[0 for x in range(0,9)] for x in range(0,9)]
        self.grids = [[[0 for x in range(0,3)] for x in range(0,3)] for x in range(0,9)]
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
        self.data_array[8] = self.grids[6][2] + self.grids[7][2] + self.grids[8][2]

    def update_array_after_columns(self, column, num):
        for i in range(len(self.data_array)):
            self.data_array[i][num] = column[i]

    def update_array_after_row(self, row, num):
        self.data_array[num] = row

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

    def check_horizontal_tri_grid(self):
        updated = False

        for section_num in range(0,3):
            for num in VALID_NUMS:
                tri_row_count = 0
                not_row = 0
                empty_row = 0
                column1 = None
                column2 = None
                column3 = None

                grid_found = []
                for i in range(0 + (section_num * 3), 3 + (section_num * 3)):
                    if num in self.data_array[i]:
                        tri_row_count += 1
                        not_row = i
                        grid_num = int(i/3) * 3 + self.data_array[i].index(num) / 3
                        grid_found.append(grid_num)
                    else:
                        empty_row = i

                if tri_row_count == 2:
                    actual_grid = 0
                    for i in range(0 + (section_num * 3), 3 + (section_num * 3)):
                        if i not in grid_found:
                            actual_grid = i
                            break

                    if actual_grid == 0 or actual_grid == 3 or actual_grid == 6:
                        row_num = 0
                        column1 = [row[0] for row in self.data_array]
                        column2 = [row[1] for row in self.data_array]
                        column3 = [row[2] for row in self.data_array]
                    elif actual_grid == 1 or actual_grid == 4 or actual_grid == 7:
                        row_num = 3
                        column1 = [row[3] for row in self.data_array]
                        column2 = [row[4] for row in self.data_array]
                        column3 = [row[5] for row in self.data_array]
                    elif actual_grid == 2 or actual_grid == 5 or actual_grid == 8:
                        row_num = 6
                        column1 = [row[6] for row in self.data_array]
                        column2 = [row[7] for row in self.data_array]
                        column3 = [row[8] for row in self.data_array]

                    num_open = 0
                    open_indeces = []
                    i = 0

                    for value in self.grids[actual_grid][empty_row % 3]:
                        if value == 0:
                            num_open += 1
                            open_indeces.append(i)
                        i += 1

                    if num_open == 3:
                        if num in column1 and num in column2:
                            column3[empty_row] = num
                        elif num in column1 and num in column3:
                            column2[empty_row] = num
                        elif num in column2 and num in column3:
                            column1[empty_row] = num
                    elif num_open == 2:
                        if column1[empty_row] == 0 and column2[empty_row] == 0:
                            if num in column1:
                                column2[empty_row] = num
                            elif num in column2:
                                column1[empty_row] = num
                        elif column1[empty_row] == 0 and column3[empty_row] == 0:
                            if num in column1:
                                column3[empty_row] = num
                            elif num in column3:
                                column1[empty_row] = num
                        elif column2[empty_row] == 0 and column3[empty_row] == 0:
                            if num in column2:
                                column3[empty_row] = num
                            elif num in column3:
                                column2[empty_row] = num
                    elif num_open == 1:
                        if num not in column1:
                            column1[empty_row] = num
                        elif num not in column2:
                            column2[empty_row] = num
                        elif num not in column3:
                            column3[empty_row] = num
                if column1:
                    self.update_array_after_columns(column1, row_num)
                    self.update_array_after_columns(column2, row_num + 1)
                    self.update_array_after_columns(column3, row_num + 2)
                    updated = True
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
            elif column_count < 8:
                for j in range(len(column)):
                    if column[j] == 0:
                        grid_num = int(j / 3) * 3 + int(i / 3)
                        self.column_grid_compare(column, grid_num, i, j)
                        self.update_array_after_columns(column, i)

        self.populate_grids()
        return updated

    def column_grid_compare(self, column, grid_num, column_num, index):
        missing = []

        for value in VALID_NUMS:
            if value not in column:
                missing.append(value)

        if len(missing) == 2:
            grid_column = column_num % 3
            num_empty = 0

            for i in range(0,3):
                if self.grids[grid_num][i][grid_column] == 0:
                    num_empty += 1

            if num_empty == 1:
                if missing[0] in self.grids[grid_num][0] or missing[0] in self.grids[grid_num][1] or missing[0] in self.grids[grid_num][2]:
                    column[index] = missing[1]
                elif missing[1] in self.grids[grid_num][0] or missing[1] in self.grids[grid_num][1] or missing[1] in self.grids[grid_num][2]:
                    column[index] = missing[0]

    def row_grid_compare(self, row, grid_num, row_num, index):
        missing = []

        for value in VALID_NUMS:
            if value not in row:
                missing.append(value)

        if len(missing) == 2:
            grid_row = row_num % 3
            num_empty = 0

            for i in range(0,3):
                if self.grids[grid_num][grid_row][i] == 0:
                    num_empty += 1

            if num_empty == 1:
                if missing[0] in self.grids[grid_num][0] or missing[0] in self.grids[grid_num][1] or missing[0] in self.grids[grid_num][2]:
                    row[index] = missing[1]
                elif missing[1] in self.grids[grid_num][0] or missing[1] in self.grids[grid_num][1] or missing[1] in self.grids[grid_num][2]:
                    row[index] = missing[0]

    def populate_grids(self):
        k = 0
        for i in range(0,3):
            for j in range(0,3):
                self.grids[i*3][j] = self.data_array[k][0:3]
                self.grids[(i*3)+1][j] = self.data_array[k][3:6]
                self.grids[(i*3)+2][j] = self.data_array[k][6:9]
                k += 1

    def add_ninth_val_in_row(self, row):
        missing = -1
        vals_in_row = []

        for value in row:
            if value != 0:
                vals_in_row.append(value)

        for value in VALID_NUMS:
            if value not in vals_in_row:
                missing = value
                break

        if missing != -1:
            row[row.index(0)] = missing

    def check_rows(self):
        updated = False
        i = 0

        for row in self.data_array:
            row_count = 0
            for value in row:
                if value in VALID_NUMS:
                    row_count += 1
            if row_count == 8:
                self.add_ninth_val_in_row(row)
                updated = True
            elif row_count < 8:
                for j in range(len(row)):
                    if row[j] == 0:
                        grid_num = int(i / 3) * 3 + int(j / 3)
                        self.row_grid_compare(row, grid_num, i, j)
                        self.update_array_after_row(row, i)
            i += 1
        self.populate_grids()
        return updated

if __name__ == "__main__":
    puzzle = Puzzle()

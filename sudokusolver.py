from copy import deepcopy
class Cell():

    def __init__(self):
        #initializes empty cell
        self.value = None
        self.possibleValues = range(1,10)

    def eliminateValue(self, value):
        # eliminates the value from the possible values for that cell
        # then checks if the cell has been solved
        if not self.value and value in self.possibleValues:
            self.possibleValues.remove(value)
            if len(self.possibleValues) == 1:
                self.value = self.possibleValues[0]
                return self.value
        return None

    def setValue(self, value):
        self.value = value
        self.possibleValues = [value]

class Puzzle():

    def __init__(self, values):
        # The values argument should be given such that it is a list of lists
        # Each element in the top-level list is a 3-item list which represents
        # the row, column and value of that cell ie. If the puzzle has two cells
        # that are solved, and these cells are in row 0, column 2 with value 6
        # and row 7, column 4 with value 5, the values argument would look like
        # this: [[0,2,6],[7,4,5]]
        # NOTE: rows and columns are numbered starting from zero
        self.cells = [[Cell() for c in range(0,9)] for r in range(0,9)]
        for cell in values:
            self.cells[cell[0]][cell[1]].setValue(cell[2])
            self.eliminate(cell[0], cell[1], cell[2])

    def solve(self):
        # base case: puzzle is solved or puzzle is invalid
        if not self.isValid:
            return False
        solution = self.solution
        if solution:
            return solution
        else:
            v = None # find first empty cell
            for r in range(0,9):
                for c in range(0,9):
                    if not self.cells[r][c].value:
                        x = r
                        y = c
                        v = self.cells[r][c].possibleValues[0]
                        break
                if v:
                    break
            # copy puzzle, make guess in first empty cell of new puzzle
            new = deepcopy(self)
            new.cells[x][y].setValue(v)
            new.eliminate(x,y,v)
            solution = new.solve() # recursive call
            if solution:
                # the solution to the new puzzle is a solution to this puzzle
                self.cells = new.cells
                return solution
            else:
                # new puzzle has no solution, therefore that guess was wrong
                # eliminate guessed value from list of possible values
                found = self.cells[x][y].eliminateValue(v)
                if found:
                    self.eliminate(x,y,found)
                return self.solve()

    def eliminate(self, x, y, value):
        # Given a cell at position (x,y) with value, this method will eliminate
        # value from the list of possible values for every cell in the same row,
        # column or 3x3 box. If any cells are solved as a result, then recursive
        # call for solved cells
        for i in range(0,9):
            found = self.cells[x][i].eliminateValue(value)
            if found:
                self.eliminate(x, i, found)
            found = self.cells[i][y].eliminateValue(value)
            if found:
                self.eliminate(i, y, found)
        boxX = x / 3
        boxY = y / 3
        for r in range(boxX*3,(boxX*3)+3):
            for c in range(boxY*3,(boxY*3)+3):
                found = self.cells[r][c].eliminateValue(value)
                if found:
                    self.eliminate(r, c, found)

    @property
    def isValid(self):
        # Checks if the puzzle is valid
        for row in self.cells:
            values = []
            for cell in row:
                if cell.value:
                    if cell.value in values:
                        return False
                    values.append(cell.value)
                elif not len(cell.possibleValues):
                    return False
        for y in range(0,9):
            values = []
            for x in range(0,9):
                if self.cells[x][y].value:
                    if self.cells[x][y] in values:
                        return False
                    values.append(self.cells[x][y])
        for boxX in range(0,3):
            for boxY in range(0,3):
                values = []
                for x in range((boxX*3),(boxX*3)+3):
                    for y in range((boxY*3),(boxY*3)+3):
                        if self.cells[x][y].value:
                            if self.cells[x][y] in values:
                                return False
                            values.append(self.cells[x][y])
        return True

    @property
    def solution(self):
        # Checks if the puzzle is solved. If it is, return the solution
        solution = []
        for row in self.cells:
            srow = []
            for cell in row:
                if not cell.value:
                    return False
                else:
                    srow.append(cell.value)
            solution.append(srow)
        return solution

    def toString(self):
        s = ""
        for x in range(0,9):
            if x % 3 == 0:
                s+="\n"
            for y in range(0,9):
                if y % 3 == 0 and y != 0:
                    s+="|  "
                cell = self.cells[x][y]
                v = str(cell.value) if cell.value else " "
                s+="|%s" %  v
            s+= "|\n"
        return s

def main():
    # Takes a single string argument which represents a list of lists
    # Each element in the top-level list is a 3-item list which represents
    # the row, column and value of that cell. Items in the top-level list
    # should be delimited by semicolons and elements within these items should
    # be delimited by commas.
    # Example: If the puzzle has two cells that are solved, and these cells are
    # in row 0, column 2 with value 6 and row 7, column 4 with value 5, the
    # values argument would look like this: "0,2,6;7,4,5"
    # NOTE: rows and columns are numbered starting from zero
    import sys
    if len(sys.argv) > 1:
        values = sys.argv[1].split(";")
        for i in range(0, len(values)):
            values[i] = values[i].split(",")
            values[i] = [int(v) for v in values[i]]
    else:
        values = []
    p = Puzzle(values)
    print "\nGiven puzzle:\n%s" % p.toString()
    solution = p.solve()
    if not solution:
        print "The puzzle has no solution!"
    else:
        print "Solution:\n%s" % p.toString()

if __name__ == "__main__":
    main()

python-sudokusolver
===================

Since I love creating sudoku solvers, here's one in python.

Run from command line with puzzle values specified as follows:

Takes a single string argument which represents a list of lists
Each element in the top-level list is a 3-item list which represents
the row, column and value of that cell. Items in the top-level list
should be delimited by semicolons and elements within these items should
be delimited by commas.
Example: If the puzzle has two cells that are solved, and these cells are
in row 0, column 2 with value 6 and row 7, column 4 with value 5, the
values argument would look like this: "0,2,6;7,4,5"
NOTE: rows and columns are numbered starting from zero

So, the command would look like this:

  $ python sudokusolver.py "0,2,6;7,4,5"

If you hate the command line, check out my Java implementation feat. GUI

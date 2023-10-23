from enum import Enum, auto

class Cell(Enum):
    UNCHECKED = 0
    CHECKED = 1
    UNCHECKABLE = 2

class Board:

    def __init__(self, row_clues=[], col_clues=[]):
        if len(row_clues) != len(col_clues):
            raise ValueError("Row clues and column clues must have the same length.")

        self.row_clues = row_clues
        self.col_clues = col_clues

        # Initialize the grid as empty
        size = len(row_clues)
        self.grid = [[Cell.CHECKED for _ in range(size)] for _ in range(size)]

    def __str__(self, pad_x=15):
        max_row_clues = max(len(clues) for clues in self.row_clues)
        max_col_clues = max(len(clues) for clues in self.col_clues)
        padding = [' ' * pad_x]

        def format_clues(clues, max_clues):
            return ' '.join([' ' for _ in range(max_clues - len(clues))] + [str(clue) for clue in clues])

        output = []

        # Print column clues
        for i in range(max_col_clues):
            col_line = padding + [' ' * max_row_clues]  # Padding for row clues
            for col_clue in self.col_clues:
                if len(col_clue) >= max_col_clues - i:
                    col_line.append(str(col_clue[len(col_clue) - max_col_clues + i]))
                else:
                    col_line.append(' ')
            output.append(' '.join(col_line))

        # Print grid with row clues
        for i, row in enumerate(self.grid):
            row_line = padding + [format_clues(self.row_clues[i], max_row_clues)]
            for cell in row:
                if cell == Cell.CHECKED:
                    row_line.append('o')  # You can replace this with a filled-in box if desired
                elif cell == Cell.UNCHECKABLE:
                    row_line.append('x')
                else:
                    row_line.append(' ')
            output.append(' '.join(row_line))

        return '\n' + '\n'.join(output)

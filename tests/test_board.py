import pytest
#from src.solver import NonogramSolver, Board
from src.board import Board

def test_solver_initialization():
    board = Board([], [])
    assert board is not None

def test_nonogram_solver_initialization_validation():
    # Invalid initialization (non-square grid)
    with pytest.raises(ValueError, match="Row clues and column clues must have the same length."):
        Board([1, 2], [1, 2, 3])


def test_print():
    board = Board([[2], [1], [3], [3], [1, 3]], [[3], [2], [3], [2, 1], [1, 1]])
    print(board)
import pytest
from src.solver import NonogramSolver

def test_solver_initialization():
    solver = NonogramSolver([], [])
    assert solver is not None
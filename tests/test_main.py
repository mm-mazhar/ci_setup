# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from src.ci_setup import add, multiply


def test_add():
    assert add(1, 2) == 3


def test_multiply():
    assert multiply(2.5, 2) == 5

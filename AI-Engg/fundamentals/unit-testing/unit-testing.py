# What is unit testing?
# A unit test checks whether a small, individual piece of code works as expected. 
# Usually, the unit is a function or a method


def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    
    
    
# run this commands
# python -m pip install pytest
# python -m pytest -v    
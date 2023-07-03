""" Unit tests """


def func(value):
    """Simple Hello world test"""
    return value + 1


def test_answer():
    """Assert that the function adds 1 to 3 and returns 4"""
    assert func(3) == 4

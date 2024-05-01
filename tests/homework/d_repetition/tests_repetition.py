import unittest
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers
class Test_Config(unittest.TestCase):
    # Test for get_factorial function
    def test_get_factorial():
        assert get_factorial(4) == 24
        assert get_factorial(5) == 120
        assert get_factorial(6) == 720
        print("All tests passed!")
    # Test for sum_odd_numbers function
    def test_sum_odd_numbers():
        assert sum_odd_numbers(7) == 16
        assert sum_odd_numbers(9) == 25
        assert sum_odd_numbers(10) == 25
        print("All tests passed!")

import unittest
from src.homework.e_functions.value_return import get_hour
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds


class Test_Config(unittest.TestCase):
    def test_get_hour():
        assert get_hour(3800) == 1
        assert get_hour(3600) == 1
    def test_get_minutes():
        assert get_minutes(3800) == 3
        assert get_minutes(3600) == 0
    def test_get_seconds():
        assert get_seconds(3800) == 20
        assert get_seconds(3600) == 0
    test_get_hour(30)
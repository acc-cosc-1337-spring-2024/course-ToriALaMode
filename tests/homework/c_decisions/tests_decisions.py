import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers
class Test_Config(unittest.TestCase):  
    def test_get_factorial_1 (self):
        self.assertEqual(4, get_factorial(24))
    def test_get_factorial_2 (self):
        self.assertEqual(5, get_factorial(120))
    def test_get_factorial_3 (self):
        self.assertEqual(6, get_factorial(720))

    #test_get_factorial_1 (4)
    #test_get_factorial_2 (5)
    #test_get_factorial_3 (6)
    def test_sum_odd_numbers (self):
        self.assertEqual(7, sum_odd_numbers(16))
    #test_sum_odd_numbers (7)


class Test_Config(unittest.TestCase):
    def test_get_options_ratio_1(self):
        self.assertEqual(.25, get_options_ratio(5, 20))
    def test_get_options_ratio_2(self):
        self.assertEqual(.5, get_options_ratio(10, 20))

    def test_get_faculty_rating_1(self):
        self.assertEqual('Excellent', get_faculty_rating(.91))
    def test_get_faculty_rating_2(self):
        self.assertEqual('Very Good', get_faculty_rating(.85))
    def test_get_faculty_rating_3(self):
        self.assertEqual('Good', get_faculty_rating(.71))    
    def test_get_faculty_rating_3(self):
        self.assertEqual('Needs Improvement', get_faculty_rating(.66)) 
    def test_get_faculty_rating_3(self):
        self.assertEqual('Unacceptable', get_faculty_rating(.45))   
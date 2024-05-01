import unittest
from src.homework.j_classes.class_a import Die #there should be no reason I get this error but I do "ModuleNotFoundError: No module named 'class_a'"
class TestDie(unittest.TestCase):
    def test_rolled_value_range(self):
        die = Die()
        for _ in range(3):
            die.roll()  # Roll the die
            rolled_value = die.get_rolled_value()  # Get the rolled value
            self.assertTrue(1 <= rolled_value <= 6, "Rolled value is out of range")

if __name__ == '__main__':
    unittest.main()

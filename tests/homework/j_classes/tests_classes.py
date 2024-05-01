import unittest
from class_a import Die
class TestDie(unittest.TestCase):
    def test_rolled_value_range(self):
        die = Die()
        for _ in range(3):
            die.roll()  # Roll the die
            rolled_value = die.get_rolled_value()  # Get the rolled value
            self.assertTrue(1 <= rolled_value <= 6, "Rolled value is out of range")

if __name__ == '__main__':
    unittest.main()
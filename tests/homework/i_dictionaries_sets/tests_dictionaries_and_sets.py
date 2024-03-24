import unittest
from homework.i_dictionaries_sets.dictionary import add_inventory
# from h/w this does nothing for my code:
# from src.homework.i_dictionaries_and_sets import get_p_distance
# from src.homework.i_dictionaries_and_sets import get_p_distance

class Test_Config(unittest.TestCase):
    def setUp(self):
        # Initialize a sample inventory dictionary
        self.inventory_dictionary = {}

    def test_add_inventory(self):
        # Test adding Widget1 with quantity of 10 to the inventory_dictionary
        add_inventory(self.inventory_dictionary, "Widget1", 10)
        self.assertEqual(self.inventory_dictionary["Widget1"], 10)

        # Test updating existing Widget1 item quantity to 35
        add_inventory(self.inventory_dictionary, "Widget1", 25)
        self.assertEqual(self.inventory_dictionary["Widget1"], 35)

        # Test updating existing Widget1 item quantity to 25 with negative quantity
        add_inventory(self.inventory_dictionary, "Widget1", -10)
        self.assertEqual(self.inventory_dictionary["Widget1"], 25)
if __name__ == '__main__':
    unittest.main()
    
    def setUp(self):
        # Initialize a sample inventory dictionary
        self.inventory_dictionary = {}

        # Add two widgets with quantities of your choice
        add_inventory(self.inventory_dictionary, "Widget1", 20)
        add_inventory(self.inventory_dictionary, "Widget2", 15)

    def test_remove_inventory_widget(self):
        # Remove widget1
        result = remove_inventory_widget(self.inventory_dictionary, "Widget1")

        # Test that widget1 is removed
        self.assertEqual(result, "Record deleted")
        
        # Test that the length of the dictionary is 1
        self.assertEqual(len(self.inventory_dictionary), 1)

        # Test that widget2 still exists
        self.assertTrue("Widget2" in self.inventory_dictionary)
if __name__ == '__main__':
    unittest.main()
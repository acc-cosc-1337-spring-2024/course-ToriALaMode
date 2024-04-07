import unittest
from homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget
from homework.i_dictionaries_sets.sets import get_students_who_took_prog1_or_prog2, get_students_who_took_prog1_and_prog2, get_students_who_took_prog2_not_prog_1, 	get_students_who_took_prog1_not_prog_2
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

class Test_Config(unittest.TestCase):
    #test_get_students_who_took_prog1_and_prog2(prog1, prog2)
    def test_get_students_who_took_prog1_and_prog2():
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        assert get_students_who_took_prog1_and_prog2(prog1, prog2) == {'Student3'}
    #test_get_students_who_took_prog1_or_prog2(prog1, prog2)
    def test_get_students_who_took_prog1_or_prog2():
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        assert get_students_who_took_prog1_or_prog2(prog1, prog2) == {'Student1', 'Student2', 'Student3', 'Student4', 'Student5'}
    #test_get_students_who_took_prog1_not_prog_2(prog1, prog2) 
    def test_get_students_who_took_prog1_not_prog_2():
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        assert get_students_who_took_prog1_not_prog_2(prog1, prog2) == {'Student1', 'Student2'}
    #test_get_students_who_took_prog2_not_prog_1(prog1, prog2)
    def test_get_students_who_took_prog2_not_prog_1():
        prog1 = {'Student1', 'Student2', 'Student3'}
        prog2 = {'Student3', 'Student4', 'Student5'}
        assert get_students_who_took_prog2_not_prog_1(prog1, prog2) == {'Student4', 'Student5'}

    if __name__ == "__main__":
        test_get_students_who_took_prog1_and_prog2()
        test_get_students_who_took_prog1_or_prog2()
        test_get_students_who_took_prog1_not_prog_2()
        test_get_students_who_took_prog2_not_prog_1()
        print("No errors")
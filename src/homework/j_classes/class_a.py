import random

class Die:
    def roll(self):
        self.roll_value = random.randint(1, 6)
    
    def get_rolled_value(self):
        return self.roll_value
    
    def __str__(self):
        return "The rolled value is {}".format(self.roll_value)

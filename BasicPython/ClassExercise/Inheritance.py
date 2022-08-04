''' Types of inheritance Python
    1. Single inheritance
    2. Multi inheritance
    3. Multilevel inheritance
    4. Hierarchical inheritance
    5. Hybrid inheritance
'''


# Base class
class Vechicle:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color


# 1. Single inheritance
# Derived class
class Bus(Vechicle):
    def busDetails(self):
        self.name = self.name.capital   
        self.model = self.model.busDetails
        self.color = self.color.capital
     
# Driver's code
object = Bus()
object.__init__()
object.busDetails()
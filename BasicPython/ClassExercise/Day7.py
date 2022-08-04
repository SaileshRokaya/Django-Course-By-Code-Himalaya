'''Task: Aug 3

Create a class Employee, with attributes: name, emp_code, designation.
Generate 4 digit emp code (using static method)
Create a method to create an employee object and emp_code for it should be generated using the method: that you created in Q.3.a.
Create objects :
One directly by passing parameters to the class. 
Another by the method you created in Q.3.b.
'''



import code


class Employee:
    def __init__(self, name, emp_code, designation):
        self.name = name
        self.emp_code = emp_code
        self.designation = designation



    # generate random integer values    
    @staticmethod
    def randomgeneration():
        from random import randint
        emp_code = randint(1000, 9999)
        print(emp_code)
        return emp_code
    
    @classmethod
    def create_emp_by_empcode(cls, name, designation):
        emp_code = cls.randomgeneration()
        return cls(name, emp_code, designation) #This is creating  object of the class itself

#e = Employee("ABC", 1234)
e1 = Employee.create_emp_by_empcode('Liza', 'Developer')

#print(e.name, e.emp_code)
print(e1.name, e1.designation, e1.emp_code)    
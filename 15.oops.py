# Everything in python is an object
# Camel case for class names
# String, int, float, tuple all are classes and we can create our own classes
# Class has atributes and methods
# Class is a blueprint to create objects over and over again
# Never rename your class names plural as this is a blueprint, we are going to create object out of it
class TestClass:  # class
    pass


testobject = TestClass()  # object -- instatiate the class

print(type(testobject))


class Student:
    membership = True  # Class Object Attribute and will be same for any object instantiated
# The class object can be called using the ClassName.membership but the object level attributes have to be called using self.
# __init__ is called anytime an object is instatiated

    def __init__(self, name='Anil', age=45):
        # or self.membership (You can call like this also)
        if Student.membership:
            self.name = name  # attribute that are unique to the object
            self.age = age

    def candoProgramming(self):
        return f'{self.name} can do programming'

    @classmethod
    def cls_method(cls, param1, param2):
        # code
        pass

    @staticmethod
    def stc_method(param1, param2):
        # code
        pass


student1 = Student(name='Sunil', age=44)
print(student1.name, student1.age,
      student1.membership, student1.candoProgramming())

student2 = Student()
print(student2.name, student2.age,
      student2.membership, student2.candoProgramming())

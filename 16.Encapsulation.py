# 4 pillars of OOPs
# -------------------------------------------------------------------------------------------------
# 1 ENCAPSULATION is the binding of data and functions that manipulate the data
# This data and functions are called attributes and methods
# It is encapsulating the data and actions together
# As you can see from below that name, age and about method has been encapsulated together
class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def about(self):
        print(f'{self._name} age {self._age} is a very polite person')


student1 = Student(name='Sunil', age=36)
student1.about()

# ------------------------------------------------------------------
# Abstraction is we dont need to what is happening inside about just call about and we get the results
# another example
print([1, 2, 1, 3].count(1))
# here also we need not understand what is going on inside the count method unless we go and dig into the code it just gives us the answers
# count len all are abstracted away from us
# for eg androidcamera.takepicture() is also abstracted we just call and the mobile just takes the picture

# But here is a problem we can easily overwrite student1
student1 = 'jdfjf'
# and all our hard work gone away 0
# There is no concept of public private in python
# Just for convention
# _name to signify its private to other programmers and it should not be touched

# dunder methods are also such that we should not over write their value
# __name__ = 5 its wromg

# ------------------------------------------------------------------------------

# INHERTIANCE


class User:
    def login(self):
        print('Logged In')


class Student(User):
    pass


class Teacher(User):
    pass


st = Student()
print(st.login())
# In this way the student and teacher can have their own methods but can share the signin method from the parent
print(isinstance(st, Student))
# to check if an object is instance
# all object inherit the base object class so there are so many dunder method availanle to each type
# eg here also any object inhereit the methods of the base class

# polymorphism example


class Bird:
    def fly(self):
        print('Birds Fly')


class Aeroplane:
    def fly(self):
        print('Aeroplanes also can fly')


# both classes have same method names fly and we can leveage this for some good purpose
# Say
eagle = Bird()
boeing = Aeroplane()


def start(object):
    return object.fly()


start(eagle)
for item in [eagle, boeing]:
    item.fly()

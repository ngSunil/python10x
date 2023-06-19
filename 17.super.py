class User:
    def __init__(self, email):
        self.email = email

    def login(self):
        print('Logged In')


class Student(User):
    def __init__(self, name, email):
        # User.__init__(self, email)
        # super references the class above the current class so we need not type the class name
        super().__init__(email)
        self.name = name


class Teacher(User):
    def __init__(self, name):
        self.name = name


arvind = Student(name='Arvind', email='ar@gmail.com')
print(arvind.email)
# The above code will throw error because both the parent class and the derived class
# Class User and student have __init__ methods
# Put the User.__init__(self, email) into the student class __init_

print(dir(arvind))  # object introspection
# we can get all the available emthods that can be run on an object

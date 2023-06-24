class User:
    def __init__(self, email):
        self.email = email
    def signIn(self):
        print(f'Successfully logged in')


class Teacher(User):
    def __init__(self, name, email, subject):
        self.name = name
        self.subject = subject
        # User.__init__(self, email)
        super().__init__(email)

    def teaches(self):
        print(f'{self.name} is a teacher and loves teaching {self.subject}')


class Student(User):
    def __init__(self, name, email, standard):
        self.name = name
        self.standard = standard
        super().__init__(email)

    def learns(self):
        print(f'{self.name} is an obedient student of the standard {self.standard}')


class Mentor(Teacher, Student):
    def __init__(self, name, email, subject, standard):
        Teacher.__init__(self, name, email, subject)
        Student.__init__(self, name, email, standard)


mentorA = Mentor('Sunil', 'sun.aec@gmail.com', 'Python', 'Semester #1')

mentorA.learns()

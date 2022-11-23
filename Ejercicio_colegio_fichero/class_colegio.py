class School:

    def __init__(self, name):
        self.name = name
        self.students = []


class Student:

    def __init__(self, name, surname, dni, subjects):
        self.name = name
        self.surname = surname
        self.dni = dni
        self.subjects = subjects

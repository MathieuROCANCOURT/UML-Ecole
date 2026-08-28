from datetime import date, datetime

from student import Student
from teacher import Teacher


class Course:
    def __init__(self, name: str, start_date: date, end_date: date, teacher: Teacher):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.teacher = teacher
        self.list_student = []

    def __str__(self) -> str:
        return ("Nom du cours: " + self.name
                + ", Période du cours: "
                + datetime(self.start_date.year, self.start_date.month, self.start_date.day).__str__() + " - "
                + datetime(self.end_date.year, self.end_date.month, self.end_date.day).__str__()
                + " avec comme professeur: " + self.teacher.display_name())

    def add_student(self, student: Student):
        self.list_student.append(student)

    def remove_student(self, student: Student):
        self.list_student.remove(student)

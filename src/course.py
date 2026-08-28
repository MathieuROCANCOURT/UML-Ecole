from datetime import date

from student import Student
from teacher import Teacher


class Course:
    def __init__(self, name: str, start_date: date, end_date: date, teacher: Teacher):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.teacher = teacher
        self.list_student = []

    def add_student(self, student: Student):
        self.list_student.append(student)

    def remove_student(self, student: Student):
        self.list_student.remove(student)

from xmlrpc.client import DateTime

from student import Student
from teacher import Teacher


class Course:
    def __init__(self, name: str, start_date: DateTime, end_date: DateTime, teacher: Teacher):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.teacher = teacher
        self.list_student = []

    def add_student(self, student: Student):
        self.list_student.append(student)

    def remove_student(self, student: Student):
        self.list_student.remove(student)

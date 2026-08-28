from xmlrpc.client import DateTime

from course import Course
from teacher import Teacher


class Courses:
    def __init__(self):
        self.list_courses = []

    def add_course(self, name: str, start_date: DateTime, end_date: DateTime, teacher: Teacher):
        self.list_courses.append(Course(name, start_date, end_date, teacher))

    def remove_course(self, index: int):
        if 0 <= index < len(self.list_courses):
            self.list_courses.pop(index)
        else:
            print("L'index pointe en dehors du tableau des cours.")

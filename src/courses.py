from datetime import date

from course import Course
from teacher import Teacher


class Courses:
    def __init__(self):
        self.list_courses: list[Course] = []

    def add_course(self, name: str, start_date: date, end_date: date, teacher: Teacher):
        self.list_courses.append(Course(name, start_date, end_date, teacher))

    def remove_course(self, index: int):
        if 0 <= index < len(self.list_courses):
            self.list_courses.pop(index)
        else:
            print("L'index pointe en dehors du tableau des cours.")

from datetime import date

from course import Course
from teacher import Teacher


class Courses:
    def __init__(self):
        self.list_courses: list[Course] = []

    def add_course(self, name: str, start_date: date, end_date: date, teacher: Teacher):
        self.list_courses.append(Course(name, start_date, end_date, teacher))

    def remove_course(self, course: Course):
        index = self.list_courses.index(course)

        if index.is_integer():
            self.list_courses.remove(course)
        else:
            print("Le cours n'est pas dans le tableau des cours.")

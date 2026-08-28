from datetime import date

from src.courses import Courses
from src.course import Course
from src.teacher import Teacher
from src.secretary import Secretary


class Director(Teacher, Secretary):
    def __init__(self):
        super().__init__()
        self.courses = Courses()

    def create_course(self, name: str, start_date: date, end_date: date, teacher: Teacher):
        self.courses.add_course(name, start_date, end_date, teacher)

    def delete_course(self, course: Course):
        self.courses.remove_course(course)

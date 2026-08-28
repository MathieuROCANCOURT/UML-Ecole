from src.courses import Courses
from src.teacher import Teacher
from src.secretary import Secretary


class Director(Teacher, Secretary):
    def __init__(self):
        super().__init__()
        self.courses = []

    def create_course(self, course: Courses):
        self.courses.append(course)

    def delete_course(self, course: Courses):
        if course in self.courses:
            self.courses.remove(course)

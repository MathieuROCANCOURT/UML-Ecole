from src.teacher import Teacher
from src.secretary import Secretary


class Director(Teacher, Secretary):
    def __init__(self):
        super().__init__()

        
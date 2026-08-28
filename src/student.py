from datetime import date

from src.address import Address
from src.user import User
import itertools


class Student(User):
    __id_counter = itertools.count(0)  # Start from 0

    def __init__(self, first_name, last_name, date_of_birth: date, address: Address):
        super().__init__()
        self.id = next(Student.__id_counter)
        self.isConnected = True
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address

    def update_account(self, address: Address):
        self.address = address

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        return age

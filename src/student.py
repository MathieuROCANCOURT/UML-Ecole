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
        gap_year = date.today().year - self.date_of_birth.year

        if date.today().month > self.date_of_birth.month:
            return gap_year - 1

        if date.today().month == self.date_of_birth.month and date.today().day > self.date_of_birth.day:
            return gap_year - 1

        return gap_year

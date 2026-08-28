from src.address import Address
from src.user import User
import itertools


class Student(User):
    __id_counter = itertools.count(0)  # Start from 0

    def __init__(self, first_name, last_name, age, address: Address):
        super().__init__()
        self.id = next(Student.__id_counter)
        self.isConnected = True
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def update_account(self, address: Address):
        self.address = address

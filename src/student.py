from src.address import Address

from src.user import User
import itertools


class Resource:
    _id_counter = itertools.count(1)  # Start from 1


class Student(User):
    def __init__(self, first_name, last_name, age, address: Address):
        super().__init__()
        self.isConnected = True
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.id = next(Resource._id_counter)

    def update_account(self, address: Address):
        self.address = address

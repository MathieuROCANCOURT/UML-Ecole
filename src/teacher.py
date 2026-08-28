from src.user import User
from src.address import Address
from xmlrpc.client import DateTime


class Teacher(User):
    def __init__(self, first_name, last_name, date_of_birth: DateTime, address: Address,
                 arrival_date: DateTime):
        super().__init__()
        self.isConnected = True
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.arrival_date = arrival_date

    def update_account(self, address: Address):
        self.address = address

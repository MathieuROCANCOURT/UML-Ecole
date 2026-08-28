import datetime

from src.user import User
from src.address import Address
from datetime import date


class Teacher(User):
    def __init__(self, first_name, last_name, date_of_birth: datetime.date, address: Address,
                 arrival_date: datetime.date):
        super().__init__()
        self.isConnected = True
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.arrival_date = arrival_date

    def update_account(self, address: Address):
        self.address = address

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        return age

from src.user import User


class Student(User):
   def __init__(self):
       super().__init__()
       isConnected = True

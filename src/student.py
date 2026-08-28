from src.user import User


class Student(User):
   def __init__(self,firstName,lastName,age,adress):
       super().__init__()
       isConnected = True

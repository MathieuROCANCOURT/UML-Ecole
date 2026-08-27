class Admin:
    def __init__(self):
        self.director = []

    def create_director(self, director):
        self.director.append(director)

    def delete_director(self, director):
        if director in self.director:
            self.director.remove(director)


class User:
    def __init__(self):
        isConnected = False


class Student(User):
   def __init__(self):
       super().__init__()
       isConnected = True
       

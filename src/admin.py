from src.director import Director


class Admin:
    def __init__(self):
        self.director = []

    def create_director(self, director: Director):
        self.director.append(director)

    def delete_director(self, director: Director):
        if director in self.director:
            self.director.remove(director)

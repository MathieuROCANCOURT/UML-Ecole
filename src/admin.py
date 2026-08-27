class Admin:
    def __init__(self):
        self.director = []

    def create_director(self, director):
        self.director.append(director)

    def delete_director(self, director):
        if director in self.director:
            self.director.remove(director)

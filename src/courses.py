from xmlrpc.client import DateTime


class Courses:
    def __init__(self, name: str, start_date: DateTime, end_date: DateTime):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

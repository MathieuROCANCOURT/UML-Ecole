from datetime import date

from address import Address
from student import Student
from teacher import Teacher


class Secretary:
    def __init__(self):
        self.__is_connected = False
        self.student_list = []
        self.teacher_list = []

    @property
    def is_connected(self):
        return self.__is_connected

    @is_connected.setter
    def is_connected(self, value):
        self.__is_connected = ~self.__is_connected

    def create_teacher_account(self, first_name: str, last_name: str, date_of_birth: date, address: Address,
                               arrival_date: date):
        if self.__is_connected:
            Teacher(first_name, last_name, date_of_birth, address, arrival_date)

    def create_student_account(self, first_name: str, last_name: str, date_of_birth: date, address: Address):
        if self.__is_connected:
            Student(first_name, last_name, date_of_birth, address)

    def update_teacher_address(self, index: int, address: Address):
        if self.__is_connected:
            if 0 <= index < len(self.teacher_list):
                self.teacher_list[index].update_account(address)
            else:
                print("L'index est en dehors de la liste des enseignants.")
        else:
            print("Vous n'êtes pas connecté")

    def update_student_address(self, index: int, address: Address):
        if self.__is_connected:
            if 0 <= index < len(self.student_list):
                self.student_list[index].update_account(address)
            else:
                print("L'index est en dehors de la liste des élèves.")
        else:
            print("Vous n'êtes pas connecté")

    def delete_teacher_account(self, teacher: Teacher):
        if self.__is_connected:
            self.teacher_list.remove(teacher)

    def delete_student_account(self, student: Student):
        if self.__is_connected:
            self.student_list.remove(student)

    def see_all_accounts(self):
        print("------------- Voici les comptes des enseignants --------------------")
        for teacher in self.teacher_list:
            print(teacher)

        print("------------- Voici les comptes des élèves --------------------")
        for student in self.student_list:
            print(student)

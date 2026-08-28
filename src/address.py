class Address:
    def __init__(self, street: str, city: str, postal_code: str):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, new_street):
        self._street = new_street

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        self._city = new_city

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, new_postal_code: str):
        if new_postal_code.isdigit() and len(new_postal_code) != 5 and (
                new_postal_code[0] != '0' or new_postal_code[1] != '0'):
            self._postal_code = "01000"
        else:
            self._postal_code = new_postal_code

    def __str__(self) -> str:
        return "Adresse:\n" + self._street + '\n' + self._postal_code + ' ' + self._city

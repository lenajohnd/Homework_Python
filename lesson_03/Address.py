class Address:
    def __init__(self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def __str__(self):
        return f"Индекс: {self.index}, Город: {self.city}, Улица: {self.street}, Дом: {self.house}, Квартира: {self.flat}"

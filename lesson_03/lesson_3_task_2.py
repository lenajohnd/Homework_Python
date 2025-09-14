from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", 3310, "+79999999999"),
    Smartphone("Motorolla", 1000, "+79888888888"),
    Smartphone("Xiaomi", 5, "+79777777777"),
    Smartphone("IPhone", 17, "+79666666666"),
    Smartphone("Honor", 10, "+79555555555")
]

for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model} - {Smartphone.number}")

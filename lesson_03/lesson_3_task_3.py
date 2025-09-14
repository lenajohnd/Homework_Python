from Adress import Adress
from Mailing import Mailing

to_adr = Adress("123456", "Москва", "Ленина", "10", "55")
from_adr = Adress("654321", "Лесосибирск", "Победы", "1", "4")

mailing = Mailing(
    to_adress = to_adr,
    from_adress = from_adr,
    cost = 500,
    track = "1q2w3e4r5t6y"
)

print(f"Отправление {mailing.track}, из {from_adr.index}, {from_adr.city}, {from_adr.street}, {from_adr.house}, {from_adr.flat} "
      f" в {to_adr.index}, {to_adr.city}, {to_adr.street}, {to_adr.house}, {to_adr.flat}. Стоимость {mailing.cost} рублей.")

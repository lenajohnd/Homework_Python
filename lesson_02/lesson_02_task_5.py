def month_to_season(i):
    if i == 12 or i == 1 or i == 2:
        return "Зима"
    elif i == 3 or i == 4 or i == 5:
        return "Весна"
    elif i == 6 or i == 7 or i == 8:
        return "Лето"
    elif i == 9 or i == 10 or i == 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


i = int(input("Введите порядковый номер месяца: "))
result = month_to_season(i)
print(result)

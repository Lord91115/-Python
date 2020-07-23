import math
import sys

planet_data = {
    "orbital_radius": {"Меркурий": 58, "Венера": 108, "Земля": 150, "Марс": 228, "Юпитер": 778, "Сатурн": 1429,
                       "Уран": 2871, "Нептун": 4504},
    "orbital_speed": {"Меркурий": 47.87, "Венера": 35.02, "Земля": 29.78, "Марс": 24.13, "Юпитер": 13.07, "Сатурн": 9.69,
                      "Уран": 6.81, "Нептун": 5.43}}

planet1 = input("Планета 1:")
planet2 = input("Планета 2:")
def days_in_year(planet):
    orbital_radius = planet_data['orbital_radius'][planet] * 1000000
    orbital_speed = planet_data['orbital_speed'][planet]

    planet_year = 2 * math.pi * orbital_radius / orbital_speed /(60 * 60 * 24)

    print("{} дней в году на {}".format(int(planet_year), planet))

    return int(planet_year)
def bigeer_year():
    planet_days1 = days_in_year(planet1)
    planet_days2 = days_in_year(planet2)
    is_bigger = planet1 if planet_days1 > planet_days2 else planet2

    print("На {} год длится дольше".format(is_bigger))
bigeer_year()
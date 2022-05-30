# Gra - zgadywanie liczby wylosowanej przez komputer

import random

a = random.randint(0,101)

liczba = int(input("Podaj liczbę: "))
p = 1

while (liczba != a) and (p < 5):
    if (liczba > a):
        print("Za duża")
    elif (liczba < a):
        print("Za mała")
    p = p + 1
    liczba = int(input("Podaj liczbę: "))
if (liczba == a) and (p < 5):
    print(f"Brawo, ta liczba to {a}")
else:
    print("Przegrałeś. Wykorzystałeś wszystkie próby")
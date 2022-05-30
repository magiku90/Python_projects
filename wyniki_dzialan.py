# komputer losuje dwie liczby i działanie, pyta o wynik i sprawdza czy dobrze odpowiedzieliśmy

import random

l1 = random.randint(1,9)
l2 = random.randint(1,9)
zn = random.randint(0,2)

if zn == 0:
    znak = "+"
    w = l1 + l2
if zn == 1:
    znak = "-"
    w = l1 - l2
if zn == 2:
    znak = "*"
    w = l1 * l2

wynik = float(input(f"Ile to jest: {l1} {znak} {l2} = "))

if wynik == w:
    print("Poprawny wynik")
else:
    print("Błędny wynik")


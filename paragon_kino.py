kina = ["Cinema-City", "Multikino"]
filmy = {0 : ["Matrix", "Avatar", "Shrek"], 1 : ["Piraci z Karaibów", "Król Lew", "Władca Pierścieni"]}
litery = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cenaBilet = 18.00

while(True):
    try:
        for i, k in enumerate(kina):
            print(i,k)
        id = int(input("Podaj indeks kina: "))
        print(kina[id])
    except:
        print("Niepoprawny wybór kina")
    break
while(True):
    try:
        print(filmy[id])
        id_filmu = int(input("Podaj indeks filmu: "))
        print(filmy[id][id_filmu])
    except:
        print("Niepoprawny wybór filmu")
    else:
        break

while(True):
    try:
        ile = int(input("Podaj ilość osób: "))
    except:
        print("Niepoprawna ilość osób")
    else:
        break

while(True):

    litera = False
    imie = input("Podaj imię osoby rezerwującej: ")
    for l in imie:
        if l in litery:
            litera = True
        else:
            litera = False
            print("Niedozwolony znak")
            break

    if(litera == True):
        break

print("PODSUMOWANIE:")
print("________________________________")
print(f"Wybrane kino: {kina[id]}")
print(f"Wybrany film: {filmy[id][id_filmu]}")
print(f"Ilość osób: {ile}")
print(f"Osoba rezerwująca: {imie}")
cena = ile * cenaBilet
print(f"Cena za bilet: {cena}")



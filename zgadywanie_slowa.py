#szubienica
litery = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
slowo = input("Podaj slowo: ")
p = 5
uzyte = set()
l = len(slowo)
print(f"Hasło składa się z {l} liter:")

print()


while(True):
    for i in slowo:
        if i in uzyte:
            print(i, end = "")
        else:
            print("_", end="")

    print()

    spr = input("Czy chcesz odgadnąć hasło? TAK/NIE?: ").upper()
    print()
    if (spr == "TAK"):
        haslo = input("Podaj hasło: ")
        if (haslo == slowo):
            print("Brawo!")
            break
        else:
            p = p - 1
            print(f"Niepoprawne hasło.")

    elif (spr == "NIE"):
        litera = input("Podaj literkę: ")
        if litera not in litery:
            print("Niedozwolony znak! Można używać tyko liter!")
            p = p - 1
        elif litera in uzyte:
            p = p - 1
            print(f"Litera {litera} była już sprawdzana.")
        elif litera in slowo:
            uzyte.add(litera)
            print(f"Brawo! Litera {litera} znajduje się w haśle.")
        else:
            p = p - 1
            print(f"W haśle nie ma litery {litera}.")

    if (p > 0):
        print(f"Pozostało Ci {p} prób.")
        print()
    else:
        print("Niestety... Wykorzystałeś wszystkie próby :(")
        print()
        break

print(f"Hasło to: {slowo}.")
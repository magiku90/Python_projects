sklep = {"chleb":3.50, "sok":6.00, "woda":1.80, "cukier":4.25}
koszyk = {}

while(True):
    menu = input("D-dodaj do koszyka, P-podglad koszyka, U-usun produkt w koszyka,  K-koniec/kasa: ").upper()

    if(menu == "D"):
        produkt = input("Podaj nazwe produktu, ktory chcesz kupic: ")
        if(produkt in sklep):
            ilosc = int(input(f"Podaj ilosc produktu ({produkt}), ktory chcesz kupic: "))
            if(produkt in koszyk):
                ileWKoszyku = koszyk[produkt]
                iloscNowa = ileWKoszyku + ilosc
                koszyk[produkt] = iloscNowa
            else:
                koszyk[produkt] = ilosc
        else:
            print("Brak produktu w sklepie")
    elif(menu == "P"):
        for produkt in koszyk:
            print(f"Produkt: {produkt} Ilość: {koszyk[produkt]}")
    elif(menu == "U"):
        produkt = input("Jaki produkt chcesz usunąć: ")
        if produkt in koszyk:
            ileWkoszyku = koszyk[produkt]
            ile = int(input(f"Ile {produkt} chcesz usunąć? "))
            if (ile < ileWkoszyku):
                ileWkoszyku = ileWkoszyku - ile
                koszyk[produkt] = ileWkoszyku
            elif(ile == ileWkoszyku):
                koszyk.pop(produkt)
            else:
                print(f"Nie można usunąć tyle {produkt}")
        else:
            print("Tego produktu nie ma w koszyku")
    elif (menu == "K"):
        print("PARAGON")
        suma = 0
        for produkt in koszyk:
            print(f"Produkt: {produkt} Ilość: {koszyk[produkt]} Cena: {sklep[produkt]} Wartość: {koszyk[produkt] * sklep[produkt]}")
            suma = suma + (koszyk[produkt] * sklep[produkt])

        print(f"Razem do zapłaty: {suma} zł")
        break


class Pracownik:

    def __init__(self, imie, nazwisko, kontrakt, pensja):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__kontrakt = kontrakt
        self.__pensja = pensja

    #gettery
    def getImie(self):
        return self.__imie

    def getNazwisko(self):
        return self.__nazwisko

    def getKontrakt(self):
        return self.__kontrakt

    def getPensja(self):
        return self.__pensja

    #settery
    def setImie(self, imie):
        self.__imie = imie

    def setNazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def setKontrakt(self, kontrakt):
        self.__kontrakt = kontrakt

    def setPensja(self, pensja):
        self.__pensja = pensja

    def __str__(self):
        return f"Imię: {self.getImie()} Nazwisko: {self.getNazwisko()}, Kontrakt: {self.getKontrakt()}, Pensja: {self.getPensja()}"


class PracownikController:

    def __init__(self):
        self.listaPracownikow = []

    def dodajPracownika(self, imie, nazwisko, kontrakt, pensja):
        pracownik = Pracownik(imie, nazwisko, kontrakt, pensja)
        self.listaPracownikow.append(pracownik)
        print("Pracownik został pomyślnie dodany")

    def pokazPracownikow(self):
        for i in self.listaPracownikow:
            print(i)

    def usunPracownika(self, nazwisko):
        znaleziono = False
        for i in self.listaPracownikow:
            if (i.getNazwisko() == nazwisko):
                znaleziono = True
                self.listaPracownikow.remove(i)
                print("Pomyślnie usunięto pracownika.")
        if (znaleziono == False):
            print("Pracownik nie został odnaleziony!")

    def zmienKontraktPracownikowi(self, nazwisko, pensja):
        znaleziono = False
        for i in self.listaPracownikow:
            if (i.getNazwisko() == nazwisko):
                znaleziono = True
                if (i.getKontrakt() == "staż"):
                    i.setKontrakt("etat")
                    print("Pomyślnie zmieniono kontrakt.")
                i.setPensja(pensja)
        if (znaleziono == "False"):
            print("Nie znaleziono pracownika!")


class Firma(PracownikController):

    def __init__(self, nazwaFirmy):
        super().__init__()              #wywołuję konstruktor z poprzedniej klasy, żeby stworzyć listę pracowników
        self.nazwaFirmy = nazwaFirmy
        self.menu()

    def menu(self):
        while(True):
            print()
            print(f"Witaj w firmie {self.nazwaFirmy}")
            menu = input(
                "D-dodaj pracownika, P-pokaz wszystkich pracownikow, U-usun pracownika, Z-zmien kontrakt pracownikowi, K-koniec: ").upper()

            if (menu == "D"):
                imie = input("Podaj imie pracownika: ")
                nazwisko = input("Podaj nazwisko pracownika: ")
                kontrakt = input("Kogo dodajesz etat/staż? : ")

                if (kontrakt == "etat"):
                    pensja = int(input("Podaj pensję pracownika: "))
                    self.dodajPracownika(imie, nazwisko, kontrakt, pensja)
                elif (kontrakt == "staż"):
                    self.dodajPracownika(imie, nazwisko, kontrakt, 1000)
                else:
                    print("Niepoprawny kontrakt!")

            elif (menu == "P"):
                self.pokazPracownikow()

            elif (menu == "U"):
                nazwisko = input("Podaj nazwisko pracownika, którego chcesz usunąć: ")
                self.usunPracownika(nazwisko)

            elif (menu == "Z"):
                nazwisko = input("Podaj nazwisko pracownika, dla któego chcesz zmienić etat: ")
                pensja = int(input("Podaj nową pensję: "))
                self.zmienKontraktPracownikowi(nazwisko, pensja)

            elif (menu == "K"):
                print("koniec programu")
                break
            else:
                print("Nierozpoznana opcja menu")

ob = Firma("M & M")

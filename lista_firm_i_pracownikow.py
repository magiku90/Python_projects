import pickle

class Firma:
    def __init__(self, nazwaFirmy):
        self.nazwaFirmy = nazwaFirmy
        self.listaPracownikowFirmy = []

class Pracownik:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.listaFirmPracownika = []

class FirmaController:
    def __init__(self):
        self.listaFirm = []
        self.listaPracownikow = []

    def czytajListeFirm(self):
        try:
            f = open("86p.dat", "rb")
            self.listaFirm = pickle.load(f)
            f.close()
        except:
            f = open("86p.dat", "wb")
            pickle.dump(self.listaFirm, f)
            f.close()
            f = open("86p.dat", "rb")
            self.listaFirm = pickle.load(f)
            f.close()

    def zapiszListeFirm(self):
        f = open("86p.dat", "wb")
        pickle.dump(self.listaFirm, f)
        f.close()

    def czytajPracownikow(self):
        try:
            f = open("86_1.dat", "rb")
            self.listaPracownikow = pickle.load(f)
            f.close()
        except:
            f = open("86_1.dat", "wb")
            pickle.dump(self.listaPracownikow, f)
            f.close()
            f = open("86_1.dat", "rb")
            self.listaPracownikow = pickle.load(f)
            f.close()

    def zapiszPracownikow(self):
        f = open("86_1.dat", "wb")
        pickle.dump(self.listaPracownikow, f)
        f.close()


    def dodajFirme(self, nazwaFirmy):

        self.czytajListeFirm()

        firma = Firma(nazwaFirmy)
        self.listaFirm.append(firma)
        n = sum(i.nazwaFirmy == nazwaFirmy for i in self.listaFirm)

        if (n < 2):
            print(f"Firma {nazwaFirmy} została pomyślnie dodana do listy firm.")
            print()
        else:
            print(f"Firma {nazwaFirmy} jest już na liście!")
            print()
            self.listaFirm.remove(firma)

        self.zapiszListeFirm()

    def usunFirme(self, nazwaFirmy):

        self.czytajListeFirm()

        znalezione = False
        if (self.listaFirm == []):
            print("Lista firm jest pusta.")
            print()
        else:
            for i in self.listaFirm:
                if (i.nazwaFirmy == nazwaFirmy):
                    znalezione = True
                    if (i.listaPracownikowFirmy == []):
                        self.listaFirm.remove(i)
                        print(f"Firma {nazwaFirmy} została pomyślnie usunięta.")
                        print()
                    else:
                        print(f"Nie można usunąć firmy {nazwaFirmy}, ponieważ są w niej zatrudnieni pracownicy.")
                        print()
            if (znalezione == False):
                print(f"Nie odnaleziono firmy {nazwaFirmy}.")
                print()

        self.zapiszListeFirm()

    def pokazFirmy(self):

        self.czytajListeFirm()

        if self.listaFirm == []:
            print("Lista firm jest pusta.")
            print()

        else:
            print("Lista firm:")
            for i in self.listaFirm:
                print(i.nazwaFirmy)
            print()

    def dodajPracownika(self, imie, nazwisko):

        self.czytajPracownikow()

        pracownik = Pracownik(imie, nazwisko)
        self.listaPracownikow.append(pracownik)

        n = sum(i.nazwisko == nazwisko for i in self.listaPracownikow)
        if (n == 2):
            k = sum(i.imie == imie for i in self.listaPracownikow)
            if (k == 2):
                print(f"Pracownik {imie} {nazwisko} jest już na liście!")
                print()
                self.listaPracownikow.remove(pracownik)
        else:
            print(f"Pracownik {imie} {nazwisko} został pomyślnie dodany do listy pracowników")
            print()


        self.zapiszPracownikow()


    def usunPracownika(self, imie, nazwisko):
        self.czytajPracownikow()

        if (self.listaPracownikow == []):
            print("Lista pracowników jest pusta.")
            print()
        else:
            znalezione = False
            znalezione1 = False
            for i in self.listaPracownikow:
                if (i.imie == imie):
                    znalezione = True
                    if (i.nazwisko == nazwisko):
                        znalezione1 = True
                        if (i.listaFirmPracownika == []):
                            self.listaPracownikow.remove(i)
                            print(f"Pracownik {imie} {nazwisko} został pomyślnie usunięty z listy pracowników.")
                            print()
                        else:
                            print(f"Nie można usunąć pracownika {imie} {nazwisko} z listy pracowników ponieważ jest zatrudniony.")
                            print()
            if (znalezione == False or znalezione1 == False):
                print(f"Na liście pracowników nie odnaleziono pracownika {imie} {nazwisko}.")
                print()

        self.zapiszPracownikow()

    def pokazPracownikow(self):
        self.czytajPracownikow()

        if (self.listaPracownikow == []):
            print("Lista pracowników jest pusta.")
            print()
        else:
            print("Lista pracowników:")
            for i in self.listaPracownikow:
                print(f"Imię: {i.imie} Nazwisko: {i.nazwisko}")
            print()

        self.zapiszPracownikow()

    def przypiszFirmePracownikowi(self, nazwaFirmy, imie, nazwisko):

        self.czytajPracownikow()
        self.czytajListeFirm()
        pracownik = Pracownik(imie, nazwisko)
        znalezione = False
        for k in self.listaFirm:
            if (k.nazwaFirmy == nazwaFirmy):
                znalezione = True
                znalezione1 = False
                for i in self.listaPracownikow:
                    if (i.imie == imie and i.nazwisko == nazwisko):
                        znalezione1 = True
                        i.listaFirmPracownika.append(nazwaFirmy)
                        k.listaPracownikowFirmy.append(pracownik)
                        n = i.listaFirmPracownika.count(nazwaFirmy)
                        if (n == 2):
                            i.listaFirmPracownika.remove(nazwaFirmy)
                            print(f"Firma {nazwaFirmy} jest już na liście firm, w których zatrudniony jest pracownik {imie} {nazwisko}.")
                            print()
                        else:
                            print(f"Firma {nazwaFirmy} została pomyślnie dodana do listy firm, w których zatrudniony jest pracownik {imie} {nazwisko}.")
                            print()
                if (znalezione1 == False):
                    print("Nie ma takiego pracowika.")
                    print()
        if (znalezione == False):
            print("Nie ma takiej firmy!")
            print()

        self.zapiszPracownikow()
        self.zapiszListeFirm()



    def usunFirmePracownikowi(self, nazwaFirmy, imie, nazwisko):
        self.czytajPracownikow()
        self.czytajListeFirm()
        znalezione = False
        for i in self.listaPracownikow:
            if (i.imie == imie and i.nazwisko == nazwisko):
                znalezione = True
                znalezione1 = False
                for k in self.listaFirm:
                    if (k.nazwaFirmy == nazwaFirmy):
                        znalezione1 = True
                        i.listaFirmPracownika.remove(nazwaFirmy)
                        print(f"Firma {nazwaFirmy} została pomyślnie usunięta z listy firm, w których zatrudniony jest pracownik {imie} {nazwisko}.")
                        print()
                if (znalezione1 == False):
                    print("Nie ma takiej firmy.")
                    print()
        if (znalezione == False):
            print("Nie ma takiego pracownika.")
            print()

        self.zapiszPracownikow()
        self.zapiszListeFirm()

    def zatrudnieniePracownika(self, imie, nazwisko):
        self.czytajPracownikow()
        self.czytajListeFirm()
        znalezione = False
        for i in self.listaPracownikow:
            if (i.imie == imie and i.nazwisko == nazwisko):
                znalezione = True
                if (i.listaFirmPracownika == []):
                    print(f"Pracownik {imie} {nazwisko} nie jest zatrudniony w żadnej firmie.")
                    print()
                else:
                    print(f"Lista firm, w których zatrudniony jest pracownik {imie} {nazwisko}:")
                    for k in i.listaFirmPracownika:
                        print(k)
                    print()
        if (znalezione == False):
            print("Nie ma takiego pracownika.")
            print()

        self.zapiszPracownikow()
        self.zapiszListeFirm()

class Zarzadzanie(FirmaController):

    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):

        while (True):
            menuGlowne = input("Menu główne:\n1-Zarządzanie firmami 2-Pracownicy 3-Zatrudnienie pracownika. 4-Koniec programu: ")
            print()

            if (menuGlowne == "1"):
                firma = input("1-Dodaj firmę 2-Usuń firmę 3-Wyświetl firmy 4-Powrót do menu głównego: ")
                print()

                while (True):
                    if (firma == "1"):
                        nazwaFirmy = input("Podaj nazwę firmy, którą chcesz dodać: ").isupper()
                        self.dodajFirme(nazwaFirmy)
                        break

                    elif (firma == "2"):
                        nazwaFirmy = input("Podaj nazwę firmy, którą chcesz usunąć: ").lower()
                        self.usunFirme(nazwaFirmy)
                        break

                    elif (firma == "3"):
                        self.pokazFirmy()
                        break

                    elif (firma == "4"):
                        break

                    else:
                        print("Nierozpoznana opcja")
                        print()
                        break

            if (menuGlowne == "2"):
                pracownik = input("1-Dodaj pracownika 2-Usuń pracownika 3-Wyświetl pracowników 4-Powrót do menu głównego: ")
                print()

                while (True):
                    if (pracownik == "1"):
                        imie = input("Podaj imie pracownika: ").lower()
                        nazwisko = input("Podaj nazwisko pracownika: ").lower()
                        self.dodajPracownika(imie, nazwisko)
                        break

                    elif (pracownik == "2"):

                        imie = input("Podaj imię pracownika: ").lower()
                        nazwisko = input("Podaj nazwisko pracownika: ").lower()
                        self.usunPracownika(imie, nazwisko)
                        break

                    elif (pracownik == "3"):
                        self.pokazPracownikow()
                        break

                    elif (pracownik == "4"):
                        break

                    else:
                        print("Nieprawidłowa opcja")
                        print()
                        break

            elif (menuGlowne == "3"):
                komenda = input("1-Przypisz firmę do pracownika 2-Usuń firmę pracownikowi 3-Wyświetl firmy, w których pracownik jest zatrudniony 4-Powrót do menu głównego: ")
                print()

                while(True):

                    if (komenda == "1"):
                        imie = input("Podaj imię pracownika: ").lower()
                        nazwisko = input("Podaj nazwisko pracownika: ").lower()
                        nazwaFirmy = input("Podaj nazwę firmy: ").lower()
                        self.przypiszFirmePracownikowi(nazwaFirmy, imie, nazwisko)
                        break

                    elif (komenda == "2"):
                        imie = input("Podaj imię pracownika: ").lower()
                        nazwisko = input("Podaj nazwisko pracownika: ").lower()
                        nazwaFirmy = input("Podaj nazwę firmy: ").lower()
                        self.usunFirmePracownikowi(nazwaFirmy, imie, nazwisko)
                        break

                    elif (komenda == "3"):
                        imie = input("Podaj imię pracownika: ").lower()
                        nazwisko = input("Podaj nazwisko pracownika: ").lower()
                        self.zatrudnieniePracownika(imie, nazwisko)
                        break

                    elif (komenda == "4"):
                        break

                    else:
                        print("Nieprawidłowa opcja")
                        print()
                        break

            elif (menuGlowne == "4"):
                break



obj = Zarzadzanie()
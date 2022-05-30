from tkinter import *  #importujemy moduły tkintera

root = Tk()
root.title("Książka telefoniczna")
root.geometry("700x300")

# logika kodu

kontakty = []

def dodajKontakt():
    # pobieranie danych z pól entry
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    telefon = entry_telefon.get()
    email = entry_email.get()

    dane = []
    dane.append(imie)
    dane.append(nazwisko)
    dane.append(telefon)
    dane.append(email)

    kontakty.append(dane)
    listaKontaktow()


    entry_imie.delete(0, END)       #czyści pole od początku 0 do końca end
    entry_nazwisko.delete(0, END)
    entry_telefon.delete(0, END)
    entry_email.delete(0, END)
    entry_imie.focus()              #kursor ma wrócić na pole imię

def listaKontaktow():

    listbox_listaKontaktow.delete(0, END) # czyścimy listę kontaktów
    for index, value in enumerate(kontakty):
        listbox_listaKontaktow.insert(index, value[0] + " " + value[1])  # insert powoduje że do listboxa wrzucam wartości, bez indeksów

def usunKontakt():
    index = listbox_listaKontaktow.index(ACTIVE)  #wskazuje indeks z polem, które zaznaczyłam w listboxie
    kontakty.pop(index)
    listaKontaktow()

def pokazKontakt():
    index = listbox_listaKontaktow.index(ACTIVE)
    label_szczegolyKontaktuImieValue.config(text = kontakty[index][0]) #config daje możliwość zmiany charakterystyki (np. inna wartość ma być wyświetlana) dla danego widżetu
    label_szczegolyKontaktuNazwiskoValue.config(text = kontakty[index][1])
    label_szczegolyKontaktuTelefonValue.config(text = kontakty[index][2])
    label_szczegolyKontaktuEmailValue.config(text = kontakty[index][3])

def edytujKontakt():
    index = listbox_listaKontaktow.index(ACTIVE)
    entry_imie.insert(0, kontakty[index][0])
    entry_nazwisko.insert(0, kontakty[index][1])
    entry_telefon.insert(0, kontakty[index][2])
    entry_email.insert(0, kontakty[index][3])
    button_dodajKontakt.config(text = "Zmień kontakt", command = zmienKontakt)

def zmienKontakt():
    index = listbox_listaKontaktow.index(ACTIVE)
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    telefon = entry_telefon.get()
    email = entry_email.get()

    kontakty[index][0] = imie
    kontakty[index][1] = nazwisko
    kontakty[index][2] = telefon
    kontakty[index][3] = email

    button_dodajKontakt.config(text = "Dodaj kontakt", command = dodajKontakt)

    listaKontaktow()

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_telefon.delete(0, END)
    entry_email.delete(0, END)
    entry_imie.focus()


#interfejs graficzny

appLeft = Frame(root)
appRight = Frame(root)
appBootom = Frame(root)

appLeft.grid(row = 0, column = 0, pady = 20, padx = 20, sticky = N)   #padx(5,30) z lewej 5, z prawej 30
appRight.grid(row = 0, column = 1, pady = 20, padx = 20, sticky = N)
appBootom.grid(row = 1,column = 0, columnspan = 2, sticky = W, pady = 20, padx = 20)

# lewa strona
label_listaKotaktow = Label(appLeft, text = "Lista kontaktów:")
listbox_listaKontaktow = Listbox(appLeft, width = 20, height = 7)
button_pokazKontakt = Button(appLeft, text = "Pokaż szczegóły kontaktu", command = pokazKontakt)  #funkcję wywołuję bez nawiasów, bez argumentów
button_usunKontakt = Button(appLeft, text = "Usuń kontakt", command = usunKontakt) # powoduje, że guzik jest aktywny
button_edytujKontakt = Button(appLeft, text = "Edytuj kontakt", command = edytujKontakt)

label_listaKotaktow.grid(row = 0, column = 0, columnspan = 3)
listbox_listaKontaktow.grid(row = 1, column = 0, columnspan = 3)
button_pokazKontakt.grid(row = 2, column = 0)
button_usunKontakt.grid(row = 2, column = 1)
button_edytujKontakt.grid(row = 2, column = 2)

# prawa strona
label_nowyKontakt = Label(appRight, text = "Nowy kontakt:")
label_imie = Label(appRight, text = "Imię:")
label_nazwisko = Label(appRight, text = "Nazwisko:")
label_telefon = Label(appRight, text = "Telefon:")
label_email = Label(appRight, text = "Email:")
entry_imie = Entry(appRight)
entry_nazwisko = Entry(appRight, width = 30)
entry_telefon = Entry(appRight)
entry_email = Entry(appRight)
button_dodajKontakt = Button(appRight, text = "Dodaj kontakt", command = dodajKontakt)

label_nowyKontakt.grid(row = 0, column = 1, columnspan = 2)
label_imie.grid(row = 1, column = 0, sticky = W)
label_nazwisko.grid(row = 2, column = 0, sticky = W)
label_telefon.grid(row = 3, column = 0, sticky = W)
label_email.grid(row = 4, column = 0, sticky = W)
button_dodajKontakt.grid(row = 5, column = 0, columnspan = 2)
entry_imie.grid(row = 1, column = 1, sticky = W)
entry_nazwisko.grid(row = 2, column = 1, sticky = W)
entry_telefon.grid(row = 3, column = 1, sticky = W)
entry_email.grid(row = 4, column = 1, sticky = W)

# ramka dolna
label_szczegolyKontaktu = Label(appBootom, text = "Szczegóły kontaktu:")
label_szczegolyKontaktuImie = Label(appBootom, text = "Imię: ")
label_szczegolyKontaktuImieValue = Label(appBootom, text = "...", width = 10)
label_szczegolyKontaktuNazwisko = Label(appBootom, text = "Nazwisko:")
label_szczegolyKontaktuNazwiskoValue = Label(appBootom, text = "...", width = 10)
label_szczegolyKontaktuTelefon = Label(appBootom, text = "Telefon:")
label_szczegolyKontaktuTelefonValue = Label(appBootom, text = "...", width = 10)
label_szczegolyKontaktuEmail = Label(appBootom, text = "Email:")
label_szczegolyKontaktuEmailValue = Label(appBootom, text = "...", width = 10)

label_szczegolyKontaktu.grid(row = 0, column = 0, columnspan = 8, sticky = W)
label_szczegolyKontaktuImie.grid(row = 1, column = 0, sticky = W)
label_szczegolyKontaktuImieValue.grid(row = 1, column = 1, sticky = W)
label_szczegolyKontaktuNazwisko.grid(row = 1, column = 2, sticky = W)
label_szczegolyKontaktuNazwiskoValue.grid(row = 1, column = 3, sticky = W)
label_szczegolyKontaktuTelefon.grid(row = 1, column = 4, sticky = W)
label_szczegolyKontaktuTelefonValue.grid(row = 1, column = 5, sticky = W)
label_szczegolyKontaktuEmail.grid(row = 1, column = 6, sticky = W)
label_szczegolyKontaktuEmailValue.grid(row = 1, column = 7, sticky = W)









root.mainloop()
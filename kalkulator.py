from tkinter import *

root = Tk()
root.title("Kalkulator")
root.geometry("320x440")

list = []

def dodaj(a):
    listbox_wynik.delete(0, END)
    if (a == "R"):
        while (list != []):
            for i in list:
                list.remove(i)
        wyczysc()
    else:
        list.append(a)
        wyswietl()

def wyswietl():
    y = ""
    for i in list:
        y = y + str(i)
    listbox_dzialanie.delete(0, END)
    listbox_dzialanie.insert(END, y)

def wyczysc():
    listbox_dzialanie.delete(0, END)
    listbox_wynik.delete(0, END)

def wynik(w):
    a = ""
    for i in list:
        a = a + str(i)

    for n, x in enumerate(a):
        if (x == "+") or (x == "-") or (x == "*") or (x == "/"):
            l1 = int(a[0:n])
            l2 = int(a[n+1:len(a)])
            if (a[n] == "+"):
                w = l1 + l2
            elif (a[n] == "-"):
                w = l1 - l2
            elif (a[n] == "*"):
                w = l1 * l2
            elif (a[n] == "/"):
                if (l2 == 0):
                    w = "Nie można dzielić przez zero!"
                else:
                    w = l1 / l2
    listbox_wynik.insert(END, w)
    while (list!=[]):
        for i in list:
            list.remove(i)



app_dzialanie = Frame(root)
app_wynik = Frame(root)
app_przyciski = Frame(root)

listbox_dzialanie = Listbox(app_dzialanie, width=50, height=2, bd=2, bg="light grey", justify=RIGHT)
listbox_wynik = Listbox(app_wynik, width=50, height=3, bd=2, justify=RIGHT)
btnn1 = Button(app_przyciski, text="0", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj(0))
btnn2 = Button(app_przyciski, text="1", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj(1))
btnn3 = Button(app_przyciski, text="2", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj(2))
btnn4 = Button(app_przyciski, text="3", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj(3))
btnn5 = Button(app_przyciski, text="4", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj(4))
btnn6 = Button(app_przyciski, text="5", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj(5))
btnn7 = Button(app_przyciski, text="6", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj(6))
btnn8 = Button(app_przyciski, text="7", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj(7))
btnn9 = Button(app_przyciski, text="8", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj(8))
btnn10 = Button(app_przyciski, text="9", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj(9))
btnn11 = Button(app_przyciski, text="+", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj("+"))
btnn12 = Button(app_przyciski, text="-", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj("-"))
btnn13 = Button(app_przyciski, text="*", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj("*"))
btnn14 = Button(app_przyciski, text="/", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj("/"))
btnn15 = Button(app_przyciski, text="=", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:wynik("="))
btnn16 = Button(app_przyciski, text="R", font=("Comic Sans MS", 14), width=5, height=2, bd=2, command=lambda:dodaj("R"))

listbox_dzialanie.grid(row=0, column=0, columnspan=6)
listbox_wynik.grid(row=1, column=0, columnspan=6)
btnn1.grid(row=6, column=0)
btnn2.grid(row=5, column=0)
btnn3.grid(row=5, column=1)
btnn4.grid(row=5, column=2)
btnn5.grid(row=4, column=0)
btnn6.grid(row=4, column=1)
btnn7.grid(row=4, column=2)
btnn8.grid(row=3, column=0)
btnn9.grid(row=3, column=1)
btnn10.grid(row=3, column=2)
btnn11.grid(row=3, column=4)
btnn12.grid(row=4, column=4)
btnn13.grid(row=5, column=4)
btnn14.grid(row=6, column=4)
btnn15.grid(row=6, column=2)
btnn16.grid(row=6, column=1)
app_dzialanie.grid(pady=5, padx=5)
app_wynik.grid(pady=5, padx=5)
app_przyciski.grid(pady=20)

root.mainloop()

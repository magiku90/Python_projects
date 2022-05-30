# gra kółko i krzyżyk
import random

gra = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]

los = random.randint(0,1)
if los == 0:
    zawodnik = "O"
else:
    zawodnik = "X"
print(f"Zaczyna zawodnik {zawodnik}.")

ilosc = 0

while(True):
    while(True):
        try:
            wsp = input(f"Zawodniku {zawodnik} podaj współrzędne: ")
            x = int(wsp[0])
            y = int(wsp[1])
            if (gra[x][y] != "*"):
                print("To pole zostało wcześniej wybrane. Tracisz kolejkę.")
            else:
                gra[x][y] = zawodnik
                ilosc = ilosc + 1
        except ValueError:
            print("Współrzędne wyraża się za pomocą liczb. Tracisz kolejkę!")
            if (zawodnik == "O"):
                zawodnik = "X"
            else:
                zawodnik = "O"
        except:
            print("Podałeś złe współrzędne. Należy wybrac wartości od 0 do 2. Tracisz kolejkę!")
            if (zawodnik == "O"):
                zawodnik = "X"
            else:
                zawodnik = "O"
        else:
            break
    
    for x in gra:
        for y in x:
            print(y, end=" ")
        print()

    if (gra[0][0] == gra[0][1] and gra[0][1] == gra[0][2] and gra[0][0] != "*"):
        print(f"Wygrał zawodnik {zawodnik}!")
        break
    elif (gra[1][0] == gra[1][1] and gra[1][1] == gra[1][2] and gra[1][0] != "*"):
        print(f"Wygrał zawodnik {zawodnik}!")
        break
    elif (gra[2][0] == gra[2][1] and gra[2][1] == gra[2][2] and gra[2][0] != "*"):
        print(f"Wygrał zawodnik {zawodnik}!")
        break
    elif (gra[0][0] == gra[1][0] and gra[1][0] == gra[2][0] and gra[0][0] != "*"):
        print(f"Wygrał zawodnik {zawodnik}!")
        break
    elif (gra[0][1] == gra[1][1] and gra[1][1] == gra[2][1] and gra[0][1] != "*"):
        print(f"Wygrał zawodnik {zawodnik}!")
        break
    elif (gra[0][2] == gra[1][2] and gra[1][2] == gra[2][2] and gra[0][2] != "*"):
        print(f"Wygrał zawodnik {zawodnik}!")
        break
    elif (gra[0][0] == gra[1][1] and gra[1][1] == gra[2][2] and gra[0][0] != "*"):
        print(f"Wygrał zawodnik {zawodnik}!")
        break
    elif (gra[2][0] == gra[1][1] and gra[1][1] == gra[0][2] and gra[2][0] != "*"):
        print(f"Wygrał zawodnik {zawodnik}!")
        break
    if ilosc == 9:
        print("Remis")
        break
    if (zawodnik == "O"):
        zawodnik = "X"
    else:
        zawodnik = "O"
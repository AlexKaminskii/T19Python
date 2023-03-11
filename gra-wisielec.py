import random
from colorama import Fore, Style
import time
import art

# ASCII ART

art.tprint("W I S I E L E C", font="big")

# wybieranie słowa i tworzenie blanka
# Lista słów będzie kiedys większa

Slowa = ["komputer", "telefon", "muzyka",
         "film", "koncert", "spektakl", "teatr"]
blank = []
missed = []

s = random.randint(0, len(Slowa)-1)
slowo = Slowa[s]
pudlo = 0
blank.clear()
for i in range(len(slowo)):
    blank += "_"
# tworzenie funkcji, która sprawdza czy blank jest pełny liter


def koniec():
    for j in range(len(blank)):
        if blank[j] == "_":
            return False
    return True


def puste():
    print("{", end=" ")
    for i in range(len(blank)):
        print(blank[i], end=" ")
    print("}", end="     ")


# Cały wisielec

# powtarzanie


while pudlo != 5:
    puste()
    print(Fore.LIGHTBLACK_EX + f"Pudła: {pudlo}/5" + Style.RESET_ALL)
    n = str(input("Podaj literę: "))
    print()
    jest0 = False
    jest1 = False
    jest2 = False
    if n in missed:
        print(Fore.LIGHTYELLOW_EX +
              "Tak litera już była przez ciebie użyta. Spróbuj innej!" + Style.RESET_ALL)
        continue
    for i in range(len(slowo)):
        if slowo[i] == n:
            blank.pop(i)
            blank.insert(i, n)
            if not jest0:
                jest0 = True
            elif jest0:
                jest1 = True
            elif jest1:
                jest2 = True
            if koniec():
                print(Fore.RED + "Brawo, udało się. Wygrana!!!" +
                      Style.RESET_ALL)
                # art.tprint(Fore.RED + "K o n i e c",
                #    font="cybermedium" + Style.RESET_ALL)
                time.sleep(3)
                exit()
    if not jest0:
        pudlo += 1
        missed += n
        # Scenariusze "pudeł"
        if pudlo == 1:
            print("Nie udało się, spróbuj jeszcze raz.")
        elif pudlo == 2:
            print("Niestety, to kolejny błąd. Jeszcze raz!")
        elif pudlo == 3:
            print("To już 3 pudło")
        elif pudlo == 4:
            print("Ostatnia szansa! Masz już 4/5 pudeł!")
if pudlo == 5:
    print(Fore.RED + "Niestety przegrana. Spróbuj zagrać jeszcze raz!" + Style.RESET_ALL)
    # art.tprint(Fore.RED + "K o n i e c", font="cybermedium" + Style.RESET_ALL)
    # print(Fore.CYAN + "CHCESZ ZAGRAĆ PONOWNIE?" + Style.RESET_ALL)
    time.sleep(3)
    exit()

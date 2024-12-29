def kontrola_vyhry(herni_pole):
    vyhra = False
    #vytazeni radku, sloupcu a diagonal pro prehhlednost
    radky = [[herni_pole[0],herni_pole[1],herni_pole[2]],[herni_pole[3],herni_pole[4],herni_pole[5]],[herni_pole[6],herni_pole[7],herni_pole[8]]]
    sloupce = [[herni_pole[0],herni_pole[3],herni_pole[6]],[herni_pole[1],herni_pole[4],herni_pole[7]],[herni_pole[2],herni_pole[5],herni_pole[8]]]
    diagonaly = [[herni_pole[0],herni_pole[4],herni_pole[8]],[herni_pole[2],herni_pole[4],herni_pole[6]]]
    #spojeni do jednoho listu
    list_trojic = radky + sloupce + diagonaly
    #kontrola vsech kombinaci pro vyhru
    for trojice in list_trojic:
        if trojice[0] != "" and all(hodnota == trojice[0] for hodnota in trojice):
            vypis_pole(herni_pole)
            print(f"Congratulations, the player {trojice[0]} WON!")
            vyhra = True
            break
    #kontrola vyplneni vsech poli pro remizu
        else:
            if all(hodnota != "" for hodnota in radky[0]) and all(hodnota != "" for hodnota in radky[1]) and all(hodnota != "" for hodnota in radky[2]):
                vypis_pole(herni_pole)
                print(f"Remiza game over!")
                vyhra = True
    return vyhra

def vypis_pole(herni_pole):
    oddelovac = "+---" * 3 + "+"
    print(f"{oddelovac}")
    print(f"|{herni_pole[0]:^3}|{herni_pole[1]:^3}|{herni_pole[2]:^3}|")
    print(f"{oddelovac}")
    print(f"|{herni_pole[3]:^3}|{herni_pole[4]:^3}|{herni_pole[5]:^3}|")
    print(f"{oddelovac}")
    print(f"|{herni_pole[6]:^3}|{herni_pole[7]:^3}|{herni_pole[8]:^3}|")
    print(f"{oddelovac}")
   
def cyklus_hry(hrac,herni_pole):
    oddelovac = "=" * 42
    while True:
        print(oddelovac)
        position = input(f"Player {hrac} | Please enter your move number: ")
        print(oddelovac)
        if position in [str(i) for i in range(1, 10)]:
            if herni_pole[int(position)-1] == "":
                herni_pole[int(position)-1]  = hrac
                break
            else:
                print(f"Field already occupied by {herni_pole[int(position)-1]}. Please choose another one")
        else: 
            print("Enter valid position e.g. 1-9")
    

def print_pravidla():
     oddelovac = "=" * 42
     print("Welcome to Tic Tac Toe",oddelovac,
    "GAME RULES",
    "Each player can place one mark (or stone)",
    "per turn on the 3x3 grid. The WINNER is",
    "who succeeds in placing three of their",
    "marks in a:",
    "* horizontal,",
    "* vertical or",
    "* diagonal row",
    oddelovac,"Let's start game",oddelovac, sep = "\n")

def print_new_game():
    oddelovac = "=" * 42
    print(oddelovac,"Let's start game",oddelovac, sep = "\n")

def hra():
    print_pravidla()
    while True:
        pole = ["","","","","","","","",""]
        while True:
            vypis_pole(pole)
            cyklus_hry("o",pole)
            vyhra = kontrola_vyhry(pole)
            if vyhra:
                break
            vypis_pole(pole)
            cyklus_hry("x",pole)
            vyhra = kontrola_vyhry(pole)
            if vyhra:
                break
        pokracovani_hry = input("Do you want to continue(y/n;): ")
        if pokracovani_hry.lower() =="n":
            print("Thanks for game. By")
            break
        else:
            print_new_game()
 
hra()
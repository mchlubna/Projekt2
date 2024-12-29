def kontrola_vyhry(herni_pole):
    vyhra = False
    #vytazeni radku, sloupcu a diagonal pro prehhlednost
    radky = [[herni_pole["A"][1],herni_pole["A"][2],herni_pole["A"][3]],[herni_pole["B"][1],herni_pole["B"][2],herni_pole["B"][3]],[herni_pole["C"][1],herni_pole["C"][2],herni_pole["C"][3]]]
    sloupce = [[herni_pole["A"][1],herni_pole["B"][1],herni_pole["C"][1]],[herni_pole["A"][2],herni_pole["B"][2],herni_pole["C"][2]],[herni_pole["A"][3],herni_pole["B"][3],herni_pole["C"][3]]]
    diagonaly = [[herni_pole["A"][1],herni_pole["B"][2],herni_pole["C"][3]],[herni_pole["A"][3],herni_pole["B"][2],herni_pole["C"][1]]]
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
    columns_names = f"{'1':>5}{'2':>4}{'3':>4}"
    print(f"{columns_names}")
    print(f"{oddelovac:>15}")
    print(f"A |{herni_pole["A"][1]:^3}|{herni_pole["A"][2]:^3}|{herni_pole["A"][3]:^3}|")
    print(f"{oddelovac:>15}")
    print(f"B |{herni_pole["B"][1]:^3}|{herni_pole["B"][2]:^3}|{herni_pole["B"][3]:^3}|")
    print(f"{oddelovac:>15}")
    print(f"C |{herni_pole["C"][1]:^3}|{herni_pole["C"][2]:^3}|{herni_pole["C"][3]:^3}|")
    print(f"{oddelovac:>15}")
   
def cyklus_hry(hrac,herni_pole):
    while True:
        souradnice = input(f"Player {hrac} | Please enter your coordinates: ")
        if souradnice[0] in ("A","B","C","a","b","c") and souradnice[1] in ("1","2","3"):
            if herni_pole[souradnice[0].upper()][int(souradnice[1])] == "":
                herni_pole[souradnice[0].upper()][int(souradnice[1])] = hrac
                break
            else:
                print(f"Field already occupied by {herni_pole[souradnice[0].upper()][int(souradnice[1])]}. Choose another one")
        else: 
            print("Enter valid coordinates e.g. A1, a1, B2, B2...")
    

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
        pole = {"A":{1:"",2:"",3:""},"B":{1:"",2:"",3:""},"C":{1:"",2:"",3:""}}
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
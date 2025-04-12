"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martin Chlubna
email: chlubnam@seznam.cz
"""

def kontrola_vyhry(herni_pole: dict) -> bool:
    """
    Vytvori listy vsech moznych kombinaci pro vyhru - radky, sloupce, diagonaly spoji je do jedno listu.
    Dale zkontroluje jestli v nektera kombinace splnuje podminky vyhry - 0 nebo x ve vsech pozicich nejake kombinace
    Parametry:
    :herni_pole: slovnik ktery se vytvori na zacatku hry do ktereho se zaznamenavaji volby hracu
    """
    #vytvoreni radku
    radky = [[herni_pole["A"][1],herni_pole["A"][2],herni_pole["A"][3]],[herni_pole["B"][1],herni_pole["B"][2],herni_pole["B"][3]],[herni_pole["C"][1],herni_pole["C"][2],herni_pole["C"][3]]]
    #vytvoreni sloupcu
    sloupce = [[herni_pole["A"][1],herni_pole["B"][1],herni_pole["C"][1]],[herni_pole["A"][2],herni_pole["B"][2],herni_pole["C"][2]],[herni_pole["A"][3],herni_pole["B"][3],herni_pole["C"][3]]]
    #vytvoreni diagonal
    diagonaly = [[herni_pole["A"][1],herni_pole["B"][2],herni_pole["C"][3]],[herni_pole["A"][3],herni_pole["B"][2],herni_pole["C"][1]]]
    #spojeni do jednoho listu
    list_trojic = radky + sloupce + diagonaly    
    vyhra = False
    #kontrola vsech kombinaci pro vyhru
    for trojice in list_trojic:
        if trojice[0] != "" and all(hodnota == trojice[0] for hodnota in trojice):
            vyhra = True
    return vyhra

def kontrola_remizy(herni_pole:dict) -> bool:
    """
    Kontroluje jestli jsou vsechny pozice herniho pole vyplnene. 
    V pripade ze ano a zaroven neni splnena zadna podminka vyhry, nastava remiza
    :Parametry
    :herni_pole: slovnik ktery se vytvori na zacatku hry do ktereho se zaznamenavaji volby hracu
    """ 
    radky = [[herni_pole["A"][1],herni_pole["A"][2],herni_pole["A"][3]],[herni_pole["B"][1],herni_pole["B"][2],herni_pole["B"][3]],[herni_pole["C"][1],herni_pole["C"][2],herni_pole["C"][3]]]
    remiza = False
    if all(hodnota != "" for hodnota in radky[0]) and all(hodnota != "" for hodnota in radky[1]) and all(hodnota != "" for hodnota in radky[2]):
        remiza = True
    return remiza
  
def vypis_pole(herni_pole:dict) -> None:
    """
    Vytiskne aktualni stav herniho pole
    :Parametry
    :herni_pole: slovnik ktery se vytvori na zacatku hry do ktereho se zaznamenavaji volby hracu
    """
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
   
def cyklus_hry(hrac: str,herni_pole: dict) -> None:
    """
    Jeden cyklus hry, hrac ktery je na tahu je vyzvan aby zadal sve souradnice. 
    Ty zkontroluji a pokud jsou spravne tak se ulozi do hreniho pole
    
    :Parametry
    :hrac: symbol x/o hrace ktery je na tahu
    :herni_pole: slovnik ktery se vytvori na zacatku hry do ktereho se zaznamenavaji volby hracu

    """
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
    

def print_pravidla() -> None:
     """
     Vypise pravidla hry
     """
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
    """
    Vypise hlasku pro zacatek hry
    """
    oddelovac = "=" * 42
    print(oddelovac,"Let's start game",oddelovac, sep = "\n")

def hra():
    """
    Hlavni funkce programu, ridi prubeh programu a vola definovane funkce
    """
    print_pravidla()
    while True:
        pole = {"A":{1:"",2:"",3:""},"B":{1:"",2:"",3:""},"C":{1:"",2:"",3:""}}
        while True:
            player = input("Player one choose your symbol: o or x: ")
            if player in ("o","x"):
                break
            else:
                print("Wrong symbol. You must choose o or x")  
        vypis_pole(pole)
        pocet_cyklu = 0  
        while True:
            cyklus_hry(player,pole)
            vypis_pole(pole)
            vyhra = kontrola_vyhry(pole)
            if vyhra:
                    print(f"Congratulations, the player {player} WON!")
                    break
            else:
                print(pocet_cyklu)
                if pocet_cyklu == 8:
                    remiza = kontrola_remizy(pole)
                    if remiza:
                        print(f"Remiza game over!")  
                        break
            if player == "o":
                player = "x"
            else:
                player = "o"
            pocet_cyklu = pocet_cyklu + 1
        pokracovani_hry = input("Do you want to continue(y/n;): ")   
        if pokracovani_hry.lower() =="n":
            print("Thanks for game. By")
            break
        else:
            print_new_game()

if __name__ == "__main__":
    hra()
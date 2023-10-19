def elso():
    szam: int = int(input("Kérek egy nullánál nagyobb számot: "))
    while szam <= 0:
        print("Nullánál nagyobb számot kell megadni!")
        szam: int = int(input("Kérek egy nullánál nagyobb számot: "))
    
    i: int = 1
    while i <= szam:
        print(i)
        i+= 1

def masodik():
    szam: int = int(input("Kérek egy nullánál nagyobb számot: "))
    while szam <= 0:
        print("Nullánál nagyobb számot kell megadni!")
        szam: int = int(input("Kérek egy nullánál nagyobb számot: "))

    i: int = 1
    k: int = 0
    osszeg: int = 0
    while i <= szam:
        k = szam % i
        if k == 0:
            print(i)
            osszeg += i
        i += 1
    print(f"Összeg: {osszeg}")

def harmadik():
    szam: int = int(input("Kérek egy számot: "))
    szam2: int = int(input("Kérek még egy számot: "))
    while szam2 <= szam:
        print("Az első számnak kisebbnek kell lennie a másiknál!")
        szam2: int = int(input("Kérek még egy számot: "))
    
    k: int = 0
    while szam <= szam2:
        k = szam % 2
        if k == 0:
            print(szam)
        szam+=1

def negyedik():
    i: int = 1

    while i != 21:
        print(i*i)
        i+=1

def otodik():
    szoveg: str = str(input("Kérek egy tetszőleges szöveget: "))
    
    i: int = 0
    while i < len(szoveg):
        print(szoveg[i])
        i+=1

def hatodik():
    szoveg: str = "Indul a kutya és a tyúk aludni"
    

    """   i: int = 0
    hossz: int  = len(szoveg) - 1
    while i > 0:
      
        print(szoveg[index])
        i -= 1
     """
    i: int = 0
    hossz: int  = len(szoveg)
    while i < hossz:
        index: int = hossz - i -1
        print(szoveg[index])
        i += 1
    



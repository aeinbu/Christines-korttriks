"""
Dette programmet gir brukeren 21 tall aa velge mellom, i 3 forskjellige kolonner.
Brukeren skal tenke paa et tall, og fortelle programmet hvilken kolonne tallet ligger i.
Dette gjentar seg 3 ganger, foer programmet til slutt forteller brukeren hvilket tall hen tenkte paa.

Her kommer en forklaring:
Ta 21 tall (eller kort) og del ut i 3 kolonner, forst et tall i den forste, deretter i den andre osv.
Be brukeren om aa tenke paa et av tallene i en av kolonnene.
Deretter ber du hen om å si hvilken av kolonnene tallet ligger i.
Legg kolonnene sammen til en liste igjen, med kolonnen med tallet i i midten av de to andre.
Gjør det samme 2 ganger til.
Tall nummer 11 i listen vil naa vaere det tallet personen tenkte paa uansett.
"""
import random #Importerer biblioteket random, for aa bruke shuffle.

def listeTilKolonnerPrint(lst):
    """
    Denne funksjonen tar inn en liste, 
    deler den inn i tre kolonner, og printer ut kolonnene.

    """
    a, b, c = delInnListe(lst) #Bruker delInnListe til aa lage listene a, b og c.
    for a, b, c in zip(a, b, c): #Itererer over alle listene samtidig.
        print(a,b,c, sep='\t') #Printer ut verdiene i alle tre listene, plass for plass, med stort mellomrom. 


def kolonnerTilListe(lst, svar):
    """
    Denne funksjonen tar inn en liste og et svar, 
    undersoker hva svaret er, og lager en ny liste av den gamle listen utifra
    hva svaret var.
    """
    a, b, c = delInnListe(lst) #Bruker delInnListe til aa lage listene a, b, c.
    if svar == "v": #Hvis svaret er "v" (venstre), blir listen stokket om slik, og lagt inn i en ny liste.
        return b+a+c
    elif svar == "m":
        return a+b+c
    elif svar == "h":
        return a+c+b



def delInnListe(lst):
    """
    Denne funksjonen tar inn en liste, og deler den inn i tre lister.
    """
    a = lst[0::3] #Liste a blir bestaaende av tallene paa plass 0, 3, 6, 9 osv i lst.
    b = lst[1::3] #Liste b blir bestaaende av tallene paa plass 1, 4, 7, 10 osv.
    c = lst[2::3] #Liste c blir bestaaende av tallene paa plass 2, 5, 8, 11 osv.
    return a, b, c #Returnerer alle tre listene.
    

def printBeskjed():
    """
    Denne funksjonen printer ut en beskjed til brukeren.
    """
    print("Hvilken kolonne er tallet ditt i? (v/m/h) ") #Printer ut en beskjed.


def korttriks():
    """
    Denne funksjonen utforer korttrikset i sin helhet, ved aa bruke de andre funksjonene.
    """
    lst = list(range(1, 22)) #Lager en liste kortstokk bestaaende av tallene 1 til 21. 
    random.shuffle(lst) #Stokker kortstokken.
    for i in range(0, 3): #Denne forlokken teller fra 0 til 2, den kjorer altsaa 3 ganger totalt.
        listeTilKolonnerPrint(lst) #Printer ut listen som kolonner.
        printBeskjed() #Printer ut beskjeden til brukeren.
        svar = input() #Tar imot svaret fra brukeren.
        while svar != "v" and svar != "m" and svar != "h": #Denne while-lokken kjorer saalenge svaret fra brukeren ikke kan brukes i programmet.
            svar = input("Det skjønte jeg ikke. Vennligst fortell hvilken kolonne tallet ditt er i ved å skrive enten v(venstre), m(midten), h(hoyre): ") #Ber brukeren om aa skrive inn svaret paa nytt.
            
        lst = kolonnerTilListe(lst, svar) #Genererer en ny liste med den gamle listen, og svaret fra brukeren.
        # lst = nyList #Bytter ut listen som ligger i variablen lst med den nye listen.
    #Etter at programmet har spurt brukeren om hvilken kolonne tallet er i 3 ganger, kjores det som kommer under her.
    tallet = lst[10] #Tallet som brukeren tenkte paa, er naa paa plass 10 i den nyeste listen.
    print("Tallet du tenkte paa var: {}".format(tallet)) #Printer ut tallet til brukeren.




korttriks() #Kaller på funksjonen korttriks.



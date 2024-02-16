from helper import decoreer
from algemene_functies import mijn_functies_2

decoreer("Aanbieding")

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting}0 euro."
    return uitvoer

print(aanbieding_1('aarbei',4,0.1))

decoreer("Inkomsten")

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw    
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return uitvoer

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09

resultaat = inkomsten_totaal(inkomsten, btw_percentage)
print(resultaat)

decoreer("Laag en hoog")

def laag_en_hoog(mijn_lijst):
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer

inkomsten = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten)

print(resultaat)

decoreer("Gemiddelde")

def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    totaal = 0
    for element in mijn_lijst:
        totaal += element
    gemiddelde = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."


inkomsten = [220, 430, 125, 160, 205, 90, 345]
resultaat = gemiddelde(inkomsten)

print(resultaat)

decoreer("Meervoudig")

def meervoudig(invoer_lijst):
    tijdelijk = laag_en_hoog(invoer_lijst)
    uitvoer = [tijdelijk[0],tijdelijk[1]]
    return uitvoer

inkomsten = [10, 5, 3, 2, 1, 2, 8, 4, 6]
resultaat = meervoudig(inkomsten)

print(resultaat)

def combinatie(invoer_lijst_2):
     korte_lijst = meervoudig(invoer_lijst_2)
     uitvoer = mijn_functies_2(korte_lijst[0], korte_lijst[1])
     return uitvoer


def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst


def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f'Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro.'
    return uitvoer


 
def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        btw_bedrag = bedrag * btw  
        totaal += bedrag  
    return totaal, btw_bedrag


inkomsten = [100, 200, 300]  
btw_percentage = 0.21  

totaal_inkomsten, totaal_btw = inkomsten_totaal(inkomsten, btw_percentage)

uitvoer = f'Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {totaal_btw} euro btw betaald dient te worden.'


def laag_en_hoog(mijn_lijst):
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer

def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    totaal = 0
    for element in mijn_lijst:
        totaal += element
        gemiddelde = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."


def meervoudig(invoer_lijst):
    tijdelijk = laag_en_hoog(invoer_lijst)
    uitvoer = [tijdelijk[0],tijdelijk[1]]
    return uitvoer

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0]) + mijn_functie_2(korte_lijst[1])
    return uitvoer


invoer_lijst_2 = [220, 430, 125, 160, 205, 90, 345,]
print (combinatie(invoer_lijst_2))




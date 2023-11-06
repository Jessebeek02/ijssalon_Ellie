smaak= input ('voer smaak in ')
prijs= input ('voer prijs in ')
korting= input ('voer korting in ') 

def aanbieding_1():
    global smaak, prijs, korting
    prijs= korting*prijs
print ('Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak',(smaak),' , van ',(prijs), 'euro voor ',(korting),'euro.')


def inkomsten_totaal(a,b,c,d,e,f,g):
    return a+b+c+d+e+f+g
print ('Het totaal van alle inkomsten van deze week is'), (inkomsten_totaal),(' euro, waarover <bedrag> euro btw betaald dient te worden.')

inkomsten_totaal= (220, 420, 125, 160, 205, 90, 345) *float (input) 


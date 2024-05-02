import csv

from helper import som
from helper import decoreer
from helper import fooi_pp
from helper import onderstreep
from presentatie import presenteer

inkomsten={
    'Aardbeien-ijs-totaal' : 1000,
    'Vanille-ijs-totaal' : 2000,
    'Chocolade-ijs-totaal' : 1500,
    'Waterijsjes-totaal' : 750,
    }

totaal = 5250

presenteer(inkomsten, totaal)

with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
        writer.writerow([key, value])

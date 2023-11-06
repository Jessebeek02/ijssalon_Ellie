a=2
b=4
c=10
d=12
def mijn_functie_1():
    global a, b, c, d
    a=a*a
    b=b*b
    c=c*c
    d=d*d

mijn_functie_1()
print (b) 

argument_1= input('voer argument 1 in ')
argument_2= input('voer argument 2 in ')

def mijn_functie_2():
    global argument_1, argument_2

antwoord= int (argument_1) + int(argument_2), int (argument_1) - int (argument_2), int (argument_1) * int (argument_2), int (argument_1) / int (argument_2)
print (antwoord)

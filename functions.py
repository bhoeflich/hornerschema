import numpy
from classes import Polynomial

def get_poly(txt):
    # Hilfsvariablen
    legnth = inputvalidNotNegative(txt)+2
    coeffs = []
    # Schleife für die Koeffizienteneingabe
    for i in range(1, legnth):
        coeffs.append(inputvalid(f'{i}. Koeffizienten eingeben: '))
    return coeffs


#------Eingabevailidierung------
# Prüft ob die übergebene Variable ein integer ist oder nicht, return ist ein Bool
# genutzt in inputvaild
def is_int(x):
    try:
        int(x)
        return True
    except:
        return False

# Prüft mit is_int() ob die Eingabe ein integer (positiv/negativ) ist (Rekursiv bis die Eingabe valide ist)
# genutzt für sämtliche Eingeben von Zahlen als
def inputvalid(txt):
    x = input(txt)
    if is_int(x):
        return int(x)
    else:
        return inputvalid(f'Eingabe {x} nicht valide, bitte noch einmal versuchen ')

# Nimmt einen input engegen mit inputvalid!!! und prüft ob dieser:
#   positiv: dann Rückgabe als integer!!
#   negativ: Rekursion von inputvalidNotNegative...
# genutzt für den Grad des Polynomes
def inputvalidNotNegative(txt):
    x = inputvalid(txt)
    if x < 1:
        return inputvalidNotNegative(f'Eingabe {x} nicht valide, bitte noch einmal versuchen ')
    else:
        return int(x)

# findet die ganzahligen Teiler einer Zahl und fügt diese einer Liste (divisors) hinzu, einschließlich der neagtiven Werte
# genutzt für Methode: guess_nstRational zum finden einer Nullstelle
def get_divisorsAll(x):
    divisors = []
    abs_x = abs(x)
    for p in range(1, abs_x + 1):
        if abs_x%p == 0:
            divisors.append(p)
            divisors.append(-p)
    return divisors



# -------- Alte nicht genutzte Funktionen ----------
# alte version mit numpy
'''def get_divisors(x):
    divisors = []
    abs_x = abs(x)
    for p in numpy.arange(1, abs_x + 1, 0.1):
        rounded_p = round(p*10)/10
        if abs_x%rounded_p == 0:
            divisors.append(rounded_p)
    return divisors
'''

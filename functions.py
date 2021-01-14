
from classes import Polynomial




def get_poly(txt):
    # Hilfsvariablen
    legnth = inputvalid_not_negative(txt) + 2
    coeffs = []
    # Schleife für die Koeffizienteneingabe
    for i in range(1, legnth):
        coeffs.append(input_valid(f'{i}. Koeffizienten eingeben: '))
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
def input_valid(txt):
    x = input(txt)
    if is_int(x):
        return int(x)
    else:
        return input_valid(f'Eingabe {x} nicht valide, bitte noch einmal versuchen ')

# Nimmt einen input engegen mit input_valid!!! und prüft ob dieser:
#   positiv: dann Rückgabe als integer!!
#   negativ: Rekursion von inputvalid_not_negative...
# genutzt für den Grad des Polynomes
def inputvalid_not_negative(txt):
    x = input_valid(txt)
    if x < 1:
        return inputvalid_not_negative(f'Eingabe {x} nicht valide, bitte noch einmal versuchen ')
    else:
        return int(x)

# findet die ganzahligen Teiler einer Zahl und fügt diese einer Liste (divisors) hinzu, einschließlich der neagtiven Werte
# genutzt für Methode: guess_nstRational zum finden einer Nullstelle
def get_divisors_all(x):
    divisors = []
    abs_x = abs(x)
    for p in range(1, abs_x + 1):
        if abs_x%p == 0:
            divisors.append(p)
            divisors.append(-p)
    return divisors

import numpy

"""Funktion fragt den Grad ab und abhänig vom Grad die Koeffizienten"""
def get_poly(txt, txt1):
    # Hilfsvariablen
    legnth = inputvalidNotNegative(txt)+2
    coeffs =[]
    # Schleife für die Koeffizienteneingabe
    for i in range(1, legnth):
        print(f'{i}. Koeffizienten eingeben')
        coeffs.append(inputvalid(txt1))
    return coeffs


def is_int(x):
    try:
        int(x)
        return True
    except:
        return False

def inputvalid(txt):
    x = input(txt)
    if is_int(x) :
        return int(x)
    else:
        return inputvalid(f'Input {x} invalid, try again please ')

def inputvalidNotNegative(txt):
    x = inputvalid(txt)
    if x < 1:
        return inputvalid(f'Input {x} invalid, try again please ')
    else:
        return int(x)

# alte version mit numpy
def get_divisors(x):
    divisors = []
    abs_x = abs(x)
    for p in numpy.arange(1, abs_x + 1, 0.1):
        rounded_p = round(p*10)/10
        if abs_x%rounded_p == 0:
            divisors.append(rounded_p)
    return divisors

def get_divisorsAll(x):
    divisors = []
    abs_x = abs(x)
    for p in range(1, abs_x + 1):
        if abs_x%p == 0:
            divisors.append(p)
            divisors.append(-p)
    return divisors



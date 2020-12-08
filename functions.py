import numpy

def inputvalid(txt):
    x = input(txt)
    if x.isdigit():
        return x
    else:
        return inputvalid(f'Input {x} invalid, try again please ')

#findet ganzahlige Teiler einer Zahl
def get_divisors(x):
    divisors = []
    abs_x = abs(x)
    for p in numpy.arange(1, abs_x + 1, 0.1):
        rounded_p = round(p*10)/10
        if abs_x%rounded_p == 0:
            divisors.append(rounded_p)
    return divisors



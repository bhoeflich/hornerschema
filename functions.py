import numpy

def inputvalid(txt):
    x = input(txt)
    if x.isdigit():
        return x
    else:
        return inputvalid(f'Input {x} invalid, try again please ')

# alte version
def get_divisors(x):
    divisors = []
    abs_x = abs(x)
    for p in numpy.arange(1, abs_x + 1, 0.1):
        rounded_p = round(p*10)/10
        if abs_x%rounded_p == 0:
            divisors.append(rounded_p)
    return divisors

def get_divisorsInt(x):
    divisors = []
    abs_x = abs(x)
    for p in range(1, abs_x + 1):
        if abs_x%p == 0:
            divisors.append(p)
            divisors.append(-p)
    return divisors



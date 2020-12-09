import functions
from classes import Polynomial
"""
polynom = Polynomial(functions.get_poly('Bitte geben sie den Grad des Polynomes ein: ', ''))


if polynom.has_nst():
    nst = polynom.guess_nstRational()
    newCoeffs = polynom.horner(nst)
    newCoeffs.pop()
    print(f'{nst} ist die Nullstelle die für das Horner Schema verwendet wird...')
    print(f'Die Koeffeffizienten des reduzierten Polynomes sind {newCoeffs}')
else:
    print('Es konnte leider keine Nullstelle gefunden werden...')
    
"""

x = functions.inputvalidNotNegative('her mit der zahl')
print(x)












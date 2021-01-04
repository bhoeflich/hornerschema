import functions
from classes import Polynomial

print('Moin, dieses kleine Python Programm funktioniert für \nPolynome mit rationalen Nullstellen. Viel Spaß damit...\n')

polynom = Polynomial(functions.get_poly('Bitte gib den Grad des Polynomes ein: \n'))

if polynom.has_nst():
    newCoeffs = polynom.horner(polynom.guess_nstRational())
    newCoeffs.pop()
    print(f'{polynom.guess_nstRational()} ist die Nullstelle die für das Horner Schema verwendet wird. \n{newCoeffs} sind die Koeffeffizienten des reduzierten Polynomes {len(newCoeffs)}. Grades.')
else:
    print('Es konnte leider keine Nullstelle gefunden werden...')












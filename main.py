import functions
from classes import Polynomial

print('Moin, dieses kleine Python Programm funktioniert für \nPolynome mit rationalen Nullstellen. Viel Spaß damit...\n')

polynom = Polynomial()

polynom.add_coeffs(polynom.get_degree('Gib den Grad des Polynomes ein: '))

if polynom.has_nst():
    new_coeffs = polynom.horner(polynom.guess_nst_rational())
    new_coeffs.pop()
    print(f'{polynom.guess_nst_rational()} ist die Nullstelle die für das Horner Schema verwendet wird. \n{new_coeffs}'
          f' sind die Koeffizienten des reduzierten Polynomes {len(new_coeffs)}. Grades.')

    # polynom_new = Polynomial(new_coeffs)
    # polynom.plotPoly()
    # polynom_new.plotPoly()
else:
    print('Es konnte leider keine Nullstelle gefunden werden...')











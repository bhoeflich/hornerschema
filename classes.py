import matplotlib.pyplot as plt
import functions

class Polynomial:

    # Eigenschaften
    def __init__(self):
        self.coeffs = []
        self.coeffsReversed = list(reversed(self.coeffs))

    def get_degree(self, txt):
        return functions.inputvalid_not_negative(txt)

    def add_coeffs(self, degree):
        for i in range(1, degree + 2):
            self.coeffs.append(functions.input_valid(f'{i}. Koeffizienten eingeben: '))


    # ______________Methoden______________
    # kann man auf das Polynom anwenden

    # Gibt einen Bool zurück ob eiene Nullstelle vorahnden ist mit Hilfe von guess_nstRational()
    # genutzt in main für die if Abfrage
    def has_nst(self):
        return self.guess_nst_rational() is not None

    # Für das Errechnen des y Wertes an der Stelle x mit Hilfe des Horner Schmemas
    # genutzt in guess_nstRational()
    def get_y_new(self, x):
        new_coeffs = self.horner(x)
        return new_coeffs[-1]

    # Sucht Nullstellen mit dem Satz über Rationale Nullstellen:
    #   Kombi aus Teilermengen von p und q bilden NST, wenn vorhanden!
    #   wobei p letztes Glied ohne x, q ist coeff mit höchstem grad
    #   quasi p{}/q{} Kombinationen
    #   q ist Leitkoeffizient
    #   p ist Absolutglied

    def guess_nst_rational(self):
        p_divisors = functions.get_divisors_all(self.coeffs[-1])
        q_divisors = functions.get_divisors_all(self.coeffs[0])

        for p_divisor in p_divisors:
            for q_divisor in q_divisors:
                cur_val = self.get_y_new(p_divisor / q_divisor)
                if cur_val == 0:
                    return p_divisor / q_divisor
        return None

    # Horner Schema übernimmt x als Variable und führt Horner Schema durch, Return ist die untere Zeile des Schemas als Liste
    # genutzt in main und in Methode: get_y_new (hier um den y Wert an der Stelle x zu errechnen (letzter Listeneintrag)
    def horner(self, x):
        new_coeffs = []

        for i, co in enumerate(self.coeffs):
            if i == 0:
                new_coeffs.append(self.coeffs[0])
            else:
                new_coeffs.append(self.coeffs[i] + (x * new_coeffs[i - 1]))
        return new_coeffs

    #Spielkram
    def plot_poly(self):
        xs = [x / 10 for x in range(-100, 101)]
        ys = [self.get_y_new(x) for x in xs]
        plt.plot(xs, ys)
        plt.show()

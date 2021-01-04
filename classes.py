import functions

class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.coeffsReversed = list(reversed(coeffs))
        self.degree = len(coeffs)-1

# ______________Methoden______________

# Gibt einen Bool zurück ob eiene Nullstelle vorahnden ist mit Hilfe von guess_nstRational()
# genutzt in main für die if Abfrage
    def has_nst(self):
        return self.guess_nstRational() is not None

# Für das Errechnen des y Wertes an der Stelle x mit Hilfe des Horner Schmemas
# genutzt in guess_nstRational()
    def get_y_new(self, x):
        newCoeffs = self.horner(x)
        return newCoeffs[-1]

# Sucht Nullstellen mit dem Satz über Rationale Nullstellen:
#   Kombi aus Teilermengen von p und q bilden NST, wenn vorhanden!
#   wobei p letztes Glied ohne x, q ist coeff mit höchstem grad
#   quasi p{}/q{} Kombinationen
    def guess_nstRational(self):
        p_divisors = functions.get_divisorsAll(self.coeffsReversed[0])
        q_divisors = functions.get_divisorsAll(self.coeffs[0])

        for p_divisor in p_divisors:
            for q_divisor in q_divisors:
                curVal = self.get_y_new(p_divisor/q_divisor)
                if curVal == 0:
                    return p_divisor/q_divisor
        return None

# Horner Schema übernimmt x als Variable und führt Horner Schema durch, Return ist die untere Zeile des Schemas als Liste
# genutzt in main und in Methode: get_y_new (hier um den y Wert an der Stelle x zu errechnen (letzter Listeneintrag)
    def horner(self, x):
        newCoeffs = []

        for i, co in enumerate(self.coeffs):
            if i == 0:
                newCoeffs.append(self.coeffs[0])
            else:
                newCoeffs.append(self.coeffs[i] + (x * newCoeffs[i - 1]))
        return newCoeffs


    # To Do





#____________________________________ ALTE METHODEN (nicht genutzt)_____________________________________________________
#Alte Version ohne satz von Rationalen nst????????
    def guess_nst(self):
        divisors = functions.get_divisorsAll(self.coeffsReversed[0])
        print(divisors)
        for divisor in divisors:
            curVal = self.get_y_new(divisor)
            if curVal == 0:
                return divisor
        return None

# Alte Methoden für das errechnen des y Wertes an der Stelle x
    def get_y(self, x):
        y = 0
        for power, coeff in enumerate(self.coeffsReversed):
            y += coeff * pow(x, power)
        print(f'zugehöriger y Wert = {y}')
        return y
        # https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
        # enumerate macht liste mit indizes
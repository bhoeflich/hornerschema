import functions


class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.degree = len(coeffs)-1

        self.coeffsReversed = list(reversed(coeffs))


    def get_degree(self):
        return self.degree

    """def get_coeffs(self):
        return list(reversed(self.coeffs))"""

    def has_nst(self):
        return self.guess_nst() is not None

    def get_y(self, x):
        y = 0
        for power, coeff in enumerate(self.coeffsReversed):
            y += coeff * pow(x, power)
        print(f'zugehöriger y Wert = {y}')
        return y
        # https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
        # enumerate macht liste mit indizes

    def guess_nst(self):
        divisors = functions.get_divisorsInt(self.coeffsReversed[0])
        print(divisors)
        for divisor in divisors:
            curVal = self.get_y(divisor)
            if curVal == 0:
                return divisor
        return None

# Kombi aus Teilermengen von p und q bilden NST, wenn vorhanden!
# wobei p letztes Glied ohne x, q ist coeff mit höchstem grad
# quasi p{}/q{} Kombinationen

    def guess_nstRational(self):
        p_divisors = functions.get_divisorsInt(self.coeffsReversed[0])
        q_divisors = functions.get_divisorsInt(self.coeffs[0])

        for p_divisor in p_divisors:
            for q_divisor in q_divisors:
                curVal = self.get_y(p_divisor/q_divisor)
                if curVal == 0:
                    return p_divisor/q_divisor
        return None



    def horner(self, nst):
        newCoeffs = []
        for i, co in enumerate(self.coeffs):
            if i == 0:
                newCoeffs.append(self.coeffs[0])
            else:
                newCoeffs.append(self.coeffs[i]+(nst*newCoeffs[i-1]))
            print(newCoeffs)
        return newCoeffs



        """for c in coeffs, range(1, len(coeffs)):
            before = newCoeffs[]
            newCoeffs.append(nst*)"""






p1 = Polynomial([5, -8, -27, 18])

print(p1.horner(-2))




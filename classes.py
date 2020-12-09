import functions


class Polynomial:
    def __init__(self, coeffs):
        self.degree = len(coeffs)-1
        self.coeffs = list(reversed(coeffs))
        self.coeffsNotreversed = coeffs

    def get_degree(self):
        return self.degree

    def get_coeffs(self):
        return list(reversed(self.coeffs))

    def has_nst(self):
        return self.guess_nst() is not None

    def get_y(self, x):
        y = 0
        for power, coeff in enumerate(self.coeffs):
            y += coeff * pow(x, power)
        print(f'zugehöriger y Wert = {y}')
        return y
        # https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
        # enumerate macht liste mit indizes

    def guess_nst(self):
        divisors = functions.get_divisorsInt(self.coeffs[0])
        print(divisors)
        #Satz von rationalen nullstellen einbauen
        for divisor in divisors:
            curVal = self.get_y(divisor)
            if curVal == 0:
                return divisor
           # negVal = self.get_y(divisor * -1)
           # if negVal == 0:
           #     return divisor * -1
        return None

# Kombi aus Teilermengen von p und q bilden NST, wenn vorhanden!
# wobei p letztes Glied ohne x, q ist coeff mit höchstem grad
# quasi p{}/q{} Kombinationen

    def guess_nstRational(self):
        p_divisors = functions.get_divisorsInt(self.coeffs[0])
        q_divisors = functions.get_divisorsInt(self.coeffsNotreversed[0])

        for p_divisor in p_divisors:
            for q_divisor in q_divisors:
                curVal = self.get_y(p_divisor/q_divisor)
                if curVal == 0:
                    return p_divisor/q_divisor
        return None




           # negVal = self.get_y(divisor * -1)
           # if negVal == 0:
           #     return divisor * -1

    def horner(self, nst):
        pass
        #inputvalid()

p1 = Polynomial([3, 3, 2, 1, 5, 5])
p2 = Polynomial([3, 4, 5, 6])
p3 = Polynomial([1, -2, -3])
p4 = Polynomial([1, -2.5, 1.5])
p5 = Polynomial([1, -4, -8, 13, 10])
print(p5.guess_nstRational())



#print(p1.get_degree())
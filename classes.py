import functions


class Polynomial:
    def __init__(self, coeffs):
        self.degree = len(coeffs)-1
        self.coeffs = list(reversed(coeffs))

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
        return y
        # https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
        # enumerate macht liste mit indizes

    def guess_nst(self):
        divisors = functions.get_divisors(self.coeffs[0])
        for divisor in divisors:
            posVal = self.get_y(divisor)
            if posVal == 0:
                return divisor
            negVal = self.get_y(divisor * -1)
            if negVal == 0:
                return divisor * -1
        return None

    def horner(self, nst):

        inputvalid()

p1 = Polynomial([3, 3, 2, 1, 5, 5])
p2 = Polynomial([3, 4, 5, 6])
p3 = Polynomial([1, -2, -3])
p4 = Polynomial([1, -2.5, 1.5])
print(p4.guess_nst())
print(functions.get_divisors(-3))


#print(p1.get_degree())
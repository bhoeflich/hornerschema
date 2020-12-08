class Polynomial:
    def __init__(self, degree, coeffs):
        self.degree = degree
        self.coeffs = coeffs

    def get_degree(self):
        return self.degree

    def get_coeffs(self):
        return self.coeffs

p1 = Polynomial(5, [3, 4, 3 , 2, 1])

print(p1.get_coeffs())
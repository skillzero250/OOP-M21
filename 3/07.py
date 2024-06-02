class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(coef * x**i for i, coef in enumerate(self.coefficients))

    def __add__(self, other):
        if isinstance(other, Polynomial):
            return Polynomial(coef1 + coef2 for coef1, coef2 in zip(self.coefficients, other.coefficients))
        else:
            return NotImplemented



poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))



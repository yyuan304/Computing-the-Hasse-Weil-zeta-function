from __future__ import annotations

# should we make a class for integer mod p
class modp(object):
    def __init__(self, p : int, n : int):
        self.p = p
        self.n = n

    def __add__(self, other : modp):
        if self.p != other.p :
            raise ValueError
        return modp(self.p, (self.n + other.n) % self.p)
    
    # and define add, mul, subtract etc.

class polynomial(object):
    def __init__(self, coeff : dict):
        self.coeff = {k : v for k, v in coeff.items() if v != 0} # remove coefficients that are zero
        self.deg = max(coeff.keys())

    def __repr__(self):
        return " + ".join([f"{v}*x^{k}" for k,v in self.coeff.items()])

    def __add__(self, g : polynomial):
        new_coeff  = dict()
        for i in range(self.deg + g.deg + 1):
            new_coeff[i] = self.coeff.get(i, 0) + g.coeff.get(i, 0)
        return polynomial(new_coeff)

    def __neg__(self):
        return polynomial({k : -v for k, v in self.coeff.items()})

    def __sub__(self, g : polynomial):
        return self + (-g)

    def __mul__(self, g : polynomial):
        new_coeff = dict()
        for i in range(self.deg + g.deg + 1):
            new_coeff[i] = sum(self.coeff.get(j, 0) * g.coeff.get(i - j, 0) for j in range(i))
        return polynomial(new_coeff)

    def __truediv__(self, g : polynomial):
        # long division
        return 0
               

x = polynomial({0:1,1:2})
y = polynomial({0:3,1:4})
print(x+y)
print((x+y).deg)
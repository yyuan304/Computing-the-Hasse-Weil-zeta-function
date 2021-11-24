from __future__ import annotations

class polynomial(object):
    def __init__(self, coeff : dict):
        self.coeff = coeff
        self.deg = max(coeff.keys())

    def __repr__(self):
        return " + ".join([f"{v}*x^{k}" for k,v in self.coeff.items()])

    def __mul__(self, g : polynomial):
        new_coeff = dict()
        for i in range(self.deg + g.deg + 1):
            new_coeff[i] = sum(self.coeff.get(j, 0) * g.coeff.get(i - j, 0) for j in range(i))
        return polynomial(new_coeff)
        

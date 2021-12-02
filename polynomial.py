from __future__ import annotations
from itertools import product

# should we make a class for integer mod p
class modp(object):
    def __init__(self, p : int, n : int):
        self.p = p
        self.n = n % p
        
    def __repr__(self):
        return f"{self.n} mod {self.p}"

    def __add__(self, other : modp):
        if self.p != other.p :
            raise ValueError
        return modp(self.p, (self.n + other.n) % self.p)
    
    def __neg__(self):
        return modp(self.p, (-self.n))
        
    def __sub__(self, g : modp):
        return self + (-g)
    
    def __mul__(self, g: modp):
        if self.p != g.p :
            raise ValueError
        return modp(self.p, (self.n * g.n) % self.p)
    def __truediv__(self, g: modp):
        if self.p !=g.p :
            raise ValueError
        if g.n% self.p ==0 :
            raise ZeroDivisionError
        return modp(self.p, (self.n * g.n**(self.p-2))%self.p)
      
    def __eq__(self, g : modp):
        if self.p != g.p : 
            raise ValueError
        return (self.n - g.n) % self.p == 0

    def __hash__(self):
        return hash(repr(self))

# m1 = modp(5,1)
# m2 = modp(5,2)
# m3 = modp(5,3)
# m4 = modp(5,4)
# m5 = modp(5,5)
# print(m1 / m4)

class polynomial_modp(object):
    def __init__(self, p, coeff : dict):
        self.p = p
        self.coeff = {k :coeff[k] for k in coeff.keys() if coeff[k] != modp(p, 0)} # remove coefficients that are zero
        if self.coeff == {}:
            self.deg = 0
        else :
            self.deg = max(self.coeff.keys())
    
    def lc(self) -> modp : #leading coeff
        return self.coeff.get(self.deg, modp(self.p, 0))

    def __repr__(self):
        if self.coeff == {} : return "0"
        def format(k : int, v : modp):
            if k == 0:
                return f"{v.n}"
            elif k == 1:
                if v.n == 1:
                    return "x"
                else:
                    return f"{v.n}*x"
            else:
                if v.n == 1:
                    return f"x^{k}"
                else:
                    return f"{v.n}*x^{k}"

    def __add__(self, g : polynomial_modp):
        new_coeff  = dict()
        for i in range(self.deg + g.deg + 1):
            new_coeff[i] = self.coeff.get(i, modp(self.p, 0)) + g.coeff.get(i, modp(self.p,0))
        return polynomial_modp(self.p, new_coeff)

    def __neg__(self):
        return polynomial_modp(self.p, {k : -v for k, v in self.coeff.items()})

    def __sub__(self, g : polynomial_modp):
        return self + (-g)

    def __mul__(self, g : polynomial_modp):
        new_coeff = dict()
        for i in range(self.deg + g.deg + 1):
            new_coeff[i] = sum((self.coeff.get(j, modp(self.p, 0)) * g.coeff.get(i - j, modp(self.p, 0)) for j in range(i+1)), start=modp(self.p,0))
        return polynomial_modp(self.p, new_coeff)

    def __floordiv__(self, g : polynomial_modp):
        # long division
        lc1 = self.lc()
        if lc1.n == 0 : 
            return polynomial_modp(self.p, {})
        lc2 = g.lc()
        if lc2.n == 0: 
            raise ZeroDivisionError
        lc3 = lc1 / lc2
        h = polynomial_modp(self.p, {self.deg - g.deg : lc3})
        
        if self.deg < g.deg : 
            return polynomial_modp(self.p, {})
        elif self.deg == g.deg : 
            return h 
        else : 
            return h + (self - h * g) // g

    def __mod__(self, g : polynomial_modp):
        return self - (self // g) * g

    def __eq__(self, g : polynomial_modp):
        return self.coeff == g.coeff

    
    def __hash__(self):
        return hash(repr(self))

f = g = polynomial_modp(5, { 2 : modp(5, 1) }) # x ^ 2
x = polynomial_modp(5, {0: modp(5, 1), 1: modp(5, 2)})     # 1 + 2x
h = polynomial_modp(5, {0: modp(5, 3), 1: modp(5, 4)})     # 3 + 4x
# print(f, g, x, h, f // g, f % x, x // h)

def all_polynomial_upto_deg_n(p : int, n : int) -> list[polynomial_modp] :
    return [polynomial_modp(p, {k : modp(p, c[k]) for k in range(n+1) if c[k] != 0}) for c in product(*[[i for i in range(p)] for _ in range(n+1)])]
    

def all_polynomial_upto_deg_n_with_leading_coeff_1(p : int, n : int) -> list[polynomial_modp]:
    return list(filter(lambda f : f.lc() == modp(f.p, 1), all_polynomial_upto_deg_n(p, n)))

def is_composite(p : polynomial_modp) -> bool :
    d = p.deg
    
    for f in all_polynomial_upto_deg_n(p.p, d-1):
        if f.deg > 0 and ((p % f) == polynomial_modp(p.p, {})):
            # print(f"factor is {f}")
            return True
    return False

def is_irreducible(p : polynomial_modp) -> bool : return not(is_composite(p))

               
f = g = polynomial_modp(5, { 2 : modp(5, 1) }) # x ^ 2
x = polynomial_modp(5, {0: modp(5, 1), 1: modp(5, 2)})     # 1 + 2x
h = polynomial_modp(5, {0: modp(5, 3), 1: modp(5, 4)})     # 3 + 4x


print(f, g, x, h, f // g, f % x, x // h)

u = polynomial_modp(5, {0: modp(5,1), 1: modp(5,2)})   # 1 + 2x 
v = polynomial_modp(5, {0: modp(5,1), 1: modp(5,3)})   # 1 + 3x
print((u+v).deg)
print(u+v)

t = polynomial_modp(5, {0: modp(5,0), 1:modp(5,1)})    # x
print(f%t)

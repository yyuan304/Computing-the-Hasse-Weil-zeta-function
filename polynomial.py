class polynomial(object):
    def __init__(self, coeff):
        self.coeff = coeff
        self.deg = max(coeff.keys())
    


x= polynomial({0:3, 1:4})

print(x.deg)
        
        

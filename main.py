import polynomial

f = g = polynomial_modp(5, { 2 : modp(5, 1) }) # x ^ 2
x = polynomial_modp(5, {0: modp(5, 1), 1: modp(5, 2)})     # 1 + 2x
h = polynomial_modp(5, {0: modp(5, 3), 1: modp(5, 4)})     # 3 + 4x

print(f, g, x, h, f // g, f % x, x // h)
# print(f, g, x, h, f // g, f % x, x // h)

u = polynomial_modp(5, {0: modp(5,1), 1: modp(5,2)})   # 1 + 2x 
v = polynomial_modp(5, {0: modp(5,1), 1: modp(5,3)})   # 1 + 3x
print((u+v).deg)
print(u+v)

t = polynomial_modp(5, {0: modp(5,0), 1:modp(5,1)})    # x
print(f%t)

print(is_irreducible(polynomial_modp(2 , {0: modp(2, 1), 2: modp(2,1)})))

for f in all_polynomial_upto_deg_n_with_leading_coeff_1(2,3):
    if is_irreducible(f) == 1:
        print(f)
        
print(a_monic_irreducible_modp_polynomial_of_deg_n(7,2))

print(counting_points_of_elliptic_curves(3,1,-1,4))
#  counting the number of points of the elliptic curve y^2=x^3+x-1 over F_{3^4}. It's 64.
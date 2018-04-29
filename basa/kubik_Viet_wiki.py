import math

# a*x^3 + b*x^2 + c*x + d = 0
def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def rootodd(base, root):
    if type(root) != int or root % 2 == 0:
        print('При расчёте нечётного корня была введена некорректная степень')
        return
    elif base < 0:
        # print(type(base))
        return -1 * abs(base) ** (1 / root)
    else:
        return base ** (1 / root)


def kubik_uravn(a, b, c, d):
    div_a = a
    a = b/div_a
    b = c/div_a
    c = d/div_a
    # x^3 + a*x^2 + b*x + c
    q = (a**2 - 3*b)/9
    r = (2*a**3 - 9*a*b + 27*c)/54
    s = q**3 - r**2
    if s > 0:
        fi = 1/3*math.acos(r/(q**3)**(1/2))
        x1 = -2*q**(1/2)*math.cos(fi) - a/3
        x2 = -2*q**(1/2)*math.cos(fi + 2/3*math.pi) - a/3
        x3 = -2*q**(1/2)*math.cos(fi - 2/3*math.pi) - a/3
        print('S = %s, Q = %s, R = %s, sgn(R) = %s' % (s, q, r, sgn(r)))
        return x1, x2, x3
    elif s < 0:
        if q > 0:
            fi = 1/3*math.acosh(abs(r)/((q**3)**(1/2)))
            x1 = -2*sgn(r)*q**(1/2)*math.cosh(fi) - a/3
            x2 = complex(sgn(r)*q**(1/2)*math.cosh(fi) - a/3, 3**(1/2)*q**(1/2)*math.sinh(fi))
            x3 = complex(sgn(r) * q ** (1 / 2) * math.cosh(fi) - a / 3, -3 ** (1 / 2) * q ** (1 / 2) * math.sinh(fi))
            print('S = %s, Q = %s, R = %s, sgn(R) = %s' % (s, q, r, sgn(r)))
            return x1, x2, x3
        if q < 0:
            fi = math.asinh(abs(r)/(abs(q**3)**(1/2)))
            x1 = -2*sgn(r)*abs(q)**(1/2)*math.sinh(fi) - a/3
            x2 = complex(sgn(r) * abs(q) ** (1 / 2) * math.sinh(fi) - a / 3,
                         3 ** (1 / 2) * abs(q) ** (1 / 2) * math.cosh(fi))
            x3 = complex(sgn(r) * abs(q) ** (1 / 2) * math.sinh(fi) - a / 3,
                         - 3 ** (1 / 2) * abs(q) ** (1 / 2) * math.cosh(fi))
            print('S = %s, Q = %s, R = %s, sgn(R) = %s' % (s, q, r, sgn(r)))
            return x1, x2, x3
        if q == 0:
            x1 = - rootodd(c - a**3/27, 3) - a/3
            x2 = complex(-(a + x1)/2, 1/2*abs((a-3*x1)*(a+x1) - 4*b)**(1/2))
            x3 = complex(-(a + x1) / 2, - 1 / 2 * abs((a - 3 * x1) * (a + x1) - 4 * b) ** (1 / 2))
            print('S = %s, Q = %s, R = %s, sgn(R) = %s' % (s, q, r, sgn(r)))
            return x1, x2, x3
    elif s == 0:
        x1 = -2*sgn(r)*q**(1/2) - a/3  # -2*rootodd(r, 3) - a/3
        x2 = sgn(r)*q**(1/2) - a/3  # rootodd(r, 3) - a/3
        print('S = %s, Q = %s, R = %s, sgn(R) = %s' % (s, q, r, sgn(r)))
        return x1, x2
    

# A = 120 - 11.84 ** 2 * 10 ** (-4) * 240 ** 2 / (24 * 12.1 * 10 ** (-6) * 120 ** 2) - 1.59 * (36 + 5)
# B = 3.38 ** 2 * 10 ** (-4) * 240 ** 2 / (24 * 12.1 * 10 ** (-6))
#
# a = 1
# b = -A
# c = 0
# d = -B


a = 258852500
b = 20000
c = 95464666666660
d = 988878

x = kubik_uravn(a, b, c, d)
print('a = %s, b = %s, c = %s, d = %s' % (a, b, c, d))
print(x)

print('a*x^3 + b*x^2 + c*x + d = ' + str(a * x[0] ** 3 + b * x[0] ** 2 + c * x[0] + d))
print('a*x^3 + b*x^2 + c*x + d = ' + str(a * x[1] ** 3 + b * x[1] ** 2 + c * x[1] + d))
if len(x) == 3:
    print('a*x^3 + b*x^2 + c*x + d = ' + str(a * x[2] ** 3 + b * x[2] ** 2 + c * x[2] + d))
    
    
custom = 36.052589826042585
# print('custom a*x^3 + b*x^2 + c*x + d = ' + str(a*custom**3 + b*custom**2 + c*custom + d))

# print('Левая часть уравнения  = ' + str(custom - B / custom ** 2))
# print('Правая часть уравнения = ' + str(A))

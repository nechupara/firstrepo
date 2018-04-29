import math
from decimal import Decimal


# a*x^3 + b*x^2 + c*x + d = 0
def rootodd(base, root):
    # if type(root) != int or root % 2 == 0:
    #     print('При расчёте нечётного корня была введена некорректная степень')
    #     return
    if base < 0:
        # print(type(base))
        return -1 * abs(base) ** Decimal(1 / root)
    else:
        return base ** Decimal(1 / root)


def kubik_uravn(a, b, c, d):
    # x = y - b/(3*a)
    root_2 = Decimal(1 / 2)
    mypi = Decimal(3.141592653589793238462643383279502884197169399375)
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)
    d = Decimal(d)
    
    p = (3 * a * c - b ** 2) / (3 * a ** 2)  # c/a - b**2/(3*a**2)
    print('p ====== ' + str(p))
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)  # 2*b**3/(27*a**3) - b*c/(3*a**2) + d/a
    discrim = (4 * p ** 3 + 27 * q ** 2) / 108  # (p/3)**3 + (q/2)**2
    print('тип Q ======= ' + str(type(q)))
    print('тип P ======= ' + str(type(p)))
    print('тип discrim ======= ' + str(type(discrim)))
    print("Q = %s, p = %s, q = %s" % (discrim, p, q))
    if discrim > 0:
        print('Дискриминант больше нуля')
        y1 = rootodd((-q / 2 + discrim ** root_2), 3) + rootodd((-q / 2 - discrim ** root_2), 3)
        y2 = complex(-Decimal(0.5) * (rootodd(-q / 2 + discrim ** root_2, 3) + rootodd(-q / 2 - discrim ** root_2, 3)),
                     Decimal(3) ** root_2 / 2 * (
                         rootodd(-q / 2 + discrim ** root_2, 3) - rootodd(-q / 2 - discrim ** root_2, 3)))
        y3 = complex(-Decimal(0.5) * (rootodd(-q / 2 + discrim ** root_2, 3) + rootodd(-q / 2 - discrim ** root_2, 3)),
                     -Decimal(3) ** root_2 / 2 * (
                         rootodd(-q / 2 + discrim ** root_2, 3) - rootodd(-q / 2 - discrim ** root_2, 3)))
        x1 = y1 - b / (3 * a)
        x2 = y2 - complex(b / (3 * a), Decimal(0))
        x3 = y3 - complex(b / (3 * a), Decimal(0))
        print('discrim ===== %s, децимал discrim = %s' % (math.atan(discrim), Decimal(math.atan(discrim))))
        return x1, x2, x3
    elif discrim == 0:
        y1 = 2 * rootodd(-q / 2, 3)
        y2 = -rootodd(-q / 2, 3)
        x1 = y1 - b / (3 * a)
        x2 = y2 - b / (3 * a)
        return x1, x2
    elif discrim < 0:
        if q < 0:
            fi = Decimal(math.atan((-discrim) ** root_2 / ((-q) / 2)))
        elif q == 0:
            fi = mypi / 2
        elif q > 0:
            fi = Decimal(math.atan((-discrim) ** root_2 / ((-q) / 2))) + mypi
        y1 = 2 * (-p / 3) ** root_2 * Decimal(math.cos(fi / 3))
        y2 = 2 * (-p / 3) ** root_2 * Decimal(math.cos(fi / 3 + 2 * mypi / 3))
        y3 = 2 * (-p / 3) ** root_2 * Decimal(math.cos(fi / 3 + 4 * mypi / 3))
        x1 = y1 - b / (3 * a)
        x2 = y2 - b / (3 * a)
        x3 = y3 - b / (3 * a)
        return x1, x2, x3
    
    else:
        print('Что-то пошло не так')


A = 120 - Decimal(11.84) ** 2 * Decimal(10) ** (-4) * 240 ** 2 / (24 * Decimal(12.1) * Decimal(10) ** (-6) * 120 ** 2)\
    - Decimal(1.59) * (36 + 5)
B = Decimal(3.38) ** 2 * Decimal(10) ** (-4) * 240 ** 2 / (24 * Decimal(12.1) * Decimal(10) ** (-6))

a = 1
b = -A
c = 0
d = -B

# a = 587974694
# b = -64654654
# c = 654646465555555
# d = -10

a = Decimal(a)
b = Decimal(b)
c = Decimal(c)
d = Decimal(d)

x = kubik_uravn(a, b, c, d)
print('a = %s, b = %s, c = %s, d = %s' % (a, b, c, d))
print(x)




print('a*x^3 + b*x^2 + c*x + d = ' + str(a * x[0] ** 3 + b * x[0] ** 2 + c * x[0] + d))
print('a*x^3 + b*x^2 + c*x + d = ' + str(a * x[1] ** 3 + b * x[1] ** 2 + c * x[1] + d))
if len(x) == 3:
    print('a*x^3 + b*x^2 + c*x + d = ' + str(a * x[2] ** 3 + b * x[2] ** 2 + c * x[2] + d))

custom = x[0]
print('custom a*x^3 + b*x^2 + c*x + d = ' + str(a*custom**3 + b*custom**2 + c*custom + d))

print('Левая часть уравнения  = ' + str(custom - Decimal(B) / custom ** 2))
print('Правая часть уравнения = ' + str(A))
print(type(A))


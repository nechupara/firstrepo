#import math


# a*x^3 + b*x^2 + c*x + d = 0
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
    # x = y - b/(3*a)
    p = (3 * a * c - b ** 2) / (3 * a ** 2)  # c/a - b**2/(3*a**2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)  # 2*b**3/(27*a**3) - b*c/(3*a**2) + d/a
    discrim = (4 * p ** 3 + 27 * q ** 2) / 108  # (p/3)**3 + (q/2)**2
    print("Q = %s, p = %s, q = %s" % (discrim, p, q))
    if discrim > 0:
        y1 = rootodd((-q / 2 + discrim ** (1 / 2)), 3) + rootodd((-q / 2 - discrim ** (1 / 2)), 3)
        y2 = complex(-0.5 * (rootodd(-q / 2 + discrim ** (1 / 2), 3) + rootodd(-q / 2 - discrim ** (1 / 2), 3)),
                     3 ** (1 / 2) / 2 * (
                     rootodd(-q / 2 + discrim ** (1 / 2), 3) - rootodd(-q / 2 - discrim ** (1 / 2), 3)))
        y3 = complex(-0.5 * (rootodd(-q / 2 + discrim ** (1 / 2), 3) + rootodd(-q / 2 - discrim ** (1 / 2), 3)),
                     -3 ** (1 / 2) / 2 * (
                     rootodd(-q / 2 + discrim ** (1 / 2), 3) - rootodd(-q / 2 - discrim ** (1 / 2), 3)))
        x1 = y1 - b / (3 * a)
        x2 = y2 - b / (3 * a)
        x3 = y3 - b / (3 * a)
        print('x1 = %s, x2 = %s, x3 = %s' % (x1, x2, x3))
        return x1  # , x2, x3
    elif discrim == 0:
        y1 = 2 * rootodd(-q / 2, 3)
        y2 = -rootodd(-q / 2, 3)
        x1 = y1 - b / (3 * a)
        x2 = y2 - b / (3 * a)
        print('x1 = %s, x2 = %s' % (x1, x2))
        return max(x1, x2)
    elif discrim < 0:
        if q < 0:
            fi = math.atan((-discrim) ** (1 / 2) / ((-q) / 2))
        elif q == 0:
            fi = math.pi / 2
        elif q > 0:
            fi = math.atan((-discrim) ** (1 / 2) / ((-q) / 2)) + math.pi
        y1 = 2 * (-p / 3) ** (1 / 2) * math.cos(fi / 3)
        y2 = 2 * (-p / 3) ** (1 / 2) * math.cos(fi / 3 + 2 * math.pi / 3)
        y3 = 2 * (-p / 3) ** (1 / 2) * math.cos(fi / 3 + 4 * math.pi / 3)
        x1 = y1 - b / (3 * a)
        x2 = y2 - b / (3 * a)
        x3 = y3 - b / (3 * a)
        print('x1 = %s, x2 = %s, x3 = %s' % (x1, x2, x3))
        return max(x1, x2, x3)
    
    else:
        print('Что-то пошло не так в решении кубического уравнения')


# sigma^3 - A*sigma^2 - B = 0
# A = 120 - 11.84 ** 2 * 10 ** (-4) * 240 ** 2 / (24 * 12.1 * 10 ** (-6) * 120 ** 2) - 1.59 * (36 + 5)
# B = 3.38 ** 2 * 10 ** (-4) * 240 ** 2 / (24 * 12.1 * 10 ** (-6))
# print('A = %s, B = %s' % (A, B))
#
# a = 1
# b = -A
# c = 0
# d = -B

# a = 587974694
# b = -64654654
# c = 654646465555555
# d = -10

# x = kubik_uravn(a, b, c, d)
# print('a = %s, b = %s, c = %s, d = %s' % (a, b, c, d))
# print(x)
#
# print('a*x^3 + b*x^2 + c*x + d = ' + str(a * x ** 3 + b * x ** 2 + c * x + d))

# print('a*x^3 + b*x^2 + c*x + d = ' + str(a * x[0] ** 3 + b * x[0] ** 2 + c * x[0] + d))
# print('a*x^3 + b*x^2 + c*x + d = ' + str(a * x[1] ** 3 + b * x[1] ** 2 + c * x[1] + d))
# if len(x) == 3:
#     print('a*x^3 + b*x^2 + c*x + d = ' + str(a * x[2] ** 3 + b * x[2] ** 2 + c * x[2] + d))
#
# custom = 36.0525898260426
# print('custom a*x^3 + b*x^2 + c*x + d = ' + str(a*custom**3 + b*custom**2 + c*custom + d))
#
# print('Левая часть уравнения  = ' + str(custom - B / custom ** 2))
# print('Правая часть уравнения = ' + str(A))

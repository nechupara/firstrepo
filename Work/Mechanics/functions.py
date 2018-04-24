from input_data import *
from cables import *
import math

# Для спрощенного розрахунку коефіцієнту k_L у функції find_k_L() 1 - спрощенний розрахунок, 0 - повноцінний розрахунок
simple_k_L = 1

# словник класів безвідмовності від напруг:
klass_bezv = {0.4: 1, 6: 2, 10: 2, 35: 2, 110: 3, 150: 3, 220: 3, 330: 3, 500: 4, 750: 4}

# словники коефіцієнтів для визначення експлуатаційних навантажень:
gamma_fG = {1: 0.4, 2: 0.6, 3: 0.7, 4: 0.85}  # навантаження під час ожеледі
gamma_fmax = {1: 0.6, 2: 0.7, 3: 0.8, 4: 0.87}  # вітрове навантаження
gamma_fQ = {1: 0.47, 2: 0.63, 3: 0.72, 4: 0.84}  # навантаження від вітру на провід, вкритий ожеледдю

# Експлуатаційне навантаження від ожеледі (название таблица 6.2):
g_mp = g_p * gamma_fG[klass_bezv[U]]
# Експлуатаційне навантаження від відтру  (название таблица 6.2):
W_om = W_o * gamma_fmax[klass_bezv[U]]
# Експлуатаційне навантаження від вітру на провід, вкритий ожеледдю  (название таблица 6.2):
Q_om = Q_o * gamma_fQ[klass_bezv[U]]

# Словник коефіцієнта зміни ваги ожеледі k1 в залежності від висоти для функції find_k1():
h_k1 = {0: 0, 5: 0.7, 10: 1, 20: 1.3, 30: 1.7, 50: 2.2, 70: 2.7, 100: 3.3}

# Словник для визначення коефіцієнта мю1 (miu1) зміни ваги ожеледі за діаметром проводу в залежності від навантаження
# ожеледі на провід d=10 мм для функції find_miu1():
# Теоретично діаметр менше 5 бути не може!!!!
miu1_dict = {'g_mp<10': {0: 0, 5: 0.8, 10: 1, 15: 1.15, 30: 1.4, 70: 2},
             '10<g_mp<20': {0: 0, 5: 0.85, 10: 1, 15: 1.1, 30: 1.25, 70: 1.7},
             '20<g_mp<30': {0: 0, 5: 0.9, 10: 1, 15: 1.05, 30: 1.15, 70: 1.5},
             'g_mp>30': {0: 0, 5: 0.95, 10: 1, 15: 1.05, 30: 1.1, 70: 1.4}
             }

# Словник для визначення коефіцієнта С_h зміни вітрового тиску на проводи, троси від висоти #{5:, 10:, 20:, 40:, 60:}
# Для функції find_C_h()
C_h_dict = {
            1: {5: 0.9, 10: 1.2, 20: 1.35, 40: 1.6, 60: 1.75},
            2: {5: 0.7, 10: 1, 20: 1.15, 40: 1.45, 60: 1.65},
            3: {5: 0.4, 10: 0.6, 20: 0.85, 40: 1.15, 60: 1.35},
            4: {5: 0.2, 10: 0.4, 20: 0.65, 40: 1, 60: 1.1}
            }

# Словник для визначення коефіцієнту g_tu пульсації вітру від типу місцевості:
g_tu_dict = {1: 1.3, 2: 1.5, 3: 1.6, 4: 1.7}

# Словник для визначення коефіцієнта  miu_g зміни розміру ожеледі за діаметром проводу:
# Теоретично менше 5 бути не може!!!!!
miu_g_dict = {0: 0, 5: 0.9, 10: 1.0, 20: 1.2, 30: 1.35, 50: 1.68, 70: 2.0}

# Словник для визначення коефіцієнта k_g зміни розміру ожеледі за висоти розташування проводу:
k_g_dict = {5: 0.8, 10: 1.0, 20: 1.15, 30: 1.3, 40: 1.4, 50: 1.45, 70: 1.6, 100: 1.75}

# Температура ожеледі для територій з абсолютною висотою до 1000 м над рівнем моря:
t_ozhel = -5


# Функція для розрахунку значень лінійної інтерполяції:
def interpolation(x0, y0, x1, y1, x):
    y = y0 + (y1 - y0) / (x1 - x0) * (x - x0)
    return y


'''Лінійне ожеледне навантаження G_mp'''


# інтерполяція для визначення коефіцієнта k1 для визначення лінійного експлуатаційного навантаження від ваги ожеледі Gmp
# значення h від 0 до 100
# менше 5 метрів теоретично не може бути, хоча буде розраховано, але теоретично не вірно!!!!!
def find_k1():
    if h in h_k1:
        return h_k1[h]
    elif 0 < h < 5:
        h0 = 0
        k1_0 = h_k1[h0]
        h1 = 5
        k1_1 = h_k1[h1]
    elif 5 < h < 10:
        h0 = 5
        k1_0 = h_k1[h0]
        h1 = 10
        k1_1 = h_k1[h1]
    elif 10 < h < 20:
        h0 = 10
        k1_0 = h_k1[h0]
        h1 = 20
        k1_1 = h_k1[h1]
    elif 20 < h < 30:
        h0 = 20
        k1_0 = h_k1[h0]
        h1 = 30
        k1_1 = h_k1[h1]
    elif 30 < h < 50:
        h0 = 30
        k1_0 = h_k1[h0]
        h1 = 50
        k1_1 = h_k1[h1]
    elif 50 < h < 70:
        h0 = 50
        k1_0 = h_k1[h0]
        h1 = 70
        k1_1 = h_k1[h1]
    elif 70 < h < 100:
        h0 = 70
        k1_0 = h_k1[h0]
        h1 = 100
        k1_1 = h_k1[h1]
    return k1_0 + (k1_1 - k1_0) / (h1 - h0) * (h - h0)


# Коефіцієнт мю1 зміни ваги ожеледі за діаметром проводу в залежності від навантаження ожеледі на провід d=10 мм
# Провід діаметру менше 5 мм буде розрахований не вірно!!!!!
# gmp < 10, 10<=gmp<20, 20<=gmp<=30, 30<gmp
def find_miu1():
    def interpol_miu1():  # інтерполяція в залежності від діаметру провода
        if 0 < temp_d < 5:
            d0 = 0
            miu1_0 = d_miu1[d0]
            d1 = 5
            miu1_1 = d_miu1[d1]
        elif 5 < temp_d < 10:
            d0 = 5
            miu1_0 = d_miu1[d0]
            d1 = 10
            miu1_1 = d_miu1[d1]
        elif 10 < temp_d < 15:
            d0 = 10
            miu1_0 = d_miu1[d0]
            d1 = 15
            miu1_1 = d_miu1[d1]
        elif 15 < temp_d < 30:
            d0 = 15
            miu1_0 = d_miu1[d0]
            d1 = 30
            miu1_1 = d_miu1[d1]
        elif 30 < temp_d < 70:
            d0 = 30
            miu1_0 = d_miu1[d0]
            d1 = 70
            miu1_1 = d_miu1[d1]
        return miu1_0 + (miu1_1 - miu1_0) / (d1 - d0) * (temp_d - d0)
    
    temp_d = cables[cable]['d']
    if g_mp < 10:
        d_miu1 = miu1_dict['g_mp<10']  # d_miu1 = { 0:, 5:, 10:, 15:, 30:, 70:}
        if temp_d in d_miu1:
            return d_miu1[cables[cable]['d']]
        else:
            return interpol_miu1()
    elif 10 <= g_mp < 20:
        d_miu1 = miu1_dict['10<g_mp<20']
        if temp_d in d_miu1:
            return d_miu1[cables[cable]['d']]
        else:
            return interpol_miu1()
    elif 20 <= g_mp <= 30:
        d_miu1 = miu1_dict['20<g_mp<30']
        if temp_d in d_miu1:
            return d_miu1[cables[cable]['d']]
        else:
            return interpol_miu1()
    elif g_mp > 30:
        d_miu1 = miu1_dict['g_mp>30']
        if temp_d in d_miu1:
            return d_miu1[cables[cable]['d']]
        else:
            return interpol_miu1()


# Лінійне експлуатаційне навантаження від ваги ожеледі G_mp (Н/м)
G_mp = g_mp * find_miu1() * find_k1()
'''(КОНЕЦ БЛОКА) Лінійне ожеледне навантаження G_mp'''

'''Лінійне вітрове навантаження P_m'''


# Функція для знаходження коефіцієнту C_h зміни вітрового тиску на проводи та троси:
# Рахує значення при висоті понад 60 метрів інтерполяцією від проміжку 40-60 метрів. Теоретично це не вірно


def find_C_h():
    def interpol_C_h():
        if h < 5:
            return h_C_h[5]
        elif 5 < h < 10:
            h0 = 5
            C_h_0 = h_C_h[h0]
            h1 = 10
            C_h_1 = h_C_h[h1]
        elif 10 < h < 20:
            h0 = 10
            C_h_0 = h_C_h[h0]
            h1 = 20
            C_h_1 = h_C_h[h1]
        elif 20 < h < 40:
            h0 = 20
            C_h_0 = h_C_h[h0]
            h1 = 40
            C_h_1 = h_C_h[h1]
        elif 40 < h < 60:
            h0 = 40
            C_h_0 = h_C_h[h0]
            h1 = 60
            C_h_1 = h_C_h[h1]
        elif h > 60:
            h0 = 40
            C_h_0 = h_C_h[h0]
            h1 = 60
            C_h_1 = h_C_h[h1]
        return C_h_0 + (C_h_1 - C_h_0) / (h1 - h0) * (h - h0)
    
    h_C_h = C_h_dict[type_area]
    if h in h_C_h:
        return h_C_h[h]
    else:
        return interpol_C_h()


# Коефіцієнт пульсації вітру від типу місцевості:
g_tu = g_tu_dict[type_area]


# Коефіцієнт впливу довжини прогону. Розраховується за формулою, але приймається не менш, ніж 0,85 та не більше 1,2:
def find_k_L(l, simple_k_L=0):
    if simple_k_L:
        if type_area == 1:
            return 1.2
        else:
            return 1
    else:
        k_l_pr = 1.7 - 0.12*math.log(l)
        if 0.85 <= k_l_pr <= 1.2:
            return k_l_pr
        elif k_l_pr < 0.85:
            return 0.85
        elif k_l_pr > 1.2:
            return 1.2


# Коефіцієнт нерівномірності тиску вітру вздовж прогону ПЛ, але не більше, ніж 1,0:
def find_alfa():
    alfa = 2.6 - 0.3 * math.log(W_om)
    if alfa > 1:
        return 1
    else:
        return alfa


# Коефіцієнт динамічності:
C_dc = g_tu * find_alfa() * find_k_L(l_pr, simple_k_L)


# Аеродинамічний коефіцієнт:
def find_C_aer():
    if cables[cable]['d'] < 20:
        return 1.2
    else:
        return 1.1


# Коефіцієнт рел'єфу. Приймається за 1:
C_rel = 1

# Коефіцієнт напрямку вітру. Приймається за 1:
C_dir = 1

# Коефіцієнт врахування місця розташування проводу, тросу:
C_c = find_C_h() * C_rel * C_dir

# Кут напрямку вітру до вісі лінії (приймають fi = 1, sin(fi)=1)
fi = 90

# Лінійне експлуатаційне навантаження від дії максимального вітрового тиску P_m, Н/м:
P_m = W_om * C_c * find_C_aer() * C_dc * cables[cable]['d'] * math.sin(math.radians(fi)) ** 2 * 10 ** (-3)
'''(КОНЕЦ БЛОКА) Лінійне вітрове навантаження P_m'''

'''Лінійне навантаження від дії вітру на провід, трос, вкритий ожеледдю Q_m, Н/м'''


# Функція для знаходження коефіцієнту miu_g зміни  розміру ожеледі за діаметром проводу
# методом лінійної інтерполяції (менше 5 мм теоретично розраховано буде не вірно!!!):
def find_miu_g():
    temp_d = cables[cable]['d']
    if temp_d in miu_g_dict:
        return miu_g_dict[temp_d]
    elif 0 < temp_d < 5:  # менше 5 теоретично не може бути
        return interpolation(0, miu_g_dict[0], 5, miu_g_dict[5], temp_d)
    elif 5 < temp_d < 10:
        return interpolation(0, miu_g_dict[0], 5, miu_g_dict[5], temp_d)
    elif 10 < temp_d < 20:
        return interpolation(10, miu_g_dict[10], 20, miu_g_dict[20], temp_d)
    elif 20 < temp_d < 30:
        return interpolation(20, miu_g_dict[20], 30, miu_g_dict[30], temp_d)
    elif 30 < temp_d < 50:
        return interpolation(30, miu_g_dict[30], 50, miu_g_dict[50], temp_d)
    elif 50 < temp_d < 70:
        return interpolation(50, miu_g_dict[50], 70, miu_g_dict[70], temp_d)


# Функція для знаходження коефіцієнта k_g зміни розміру ожеледі за висоти h
# Розраховує значення при h від 0 до 100, хоча менше 5 - не вірно!!!!!!
def find_k_g():
    len_k_g_dict = len(k_g_dict)
    list_k_g_dict = list(k_g_dict)
    # print(len_k_g_dict, list_k_g_dict)
    if h in k_g_dict:
        return k_g_dict[h]
    for i in range(1, len_k_g_dict):
        if list_k_g_dict[i - 1] < h < list_k_g_dict[i]:
            return interpolation(list_k_g_dict[i - 1], k_g_dict[list_k_g_dict[i - 1]], list_k_g_dict[i],
                                 k_g_dict[list_k_g_dict[i]], h)


Q_m = Q_om * find_miu_g() * find_k_g() * C_c * find_k_L(l_pr, simple_k_L) * math.sin(math.radians(fi)) ** 2
'''(КОНЕЦ БЛОКА) Лінійне навантаження від дії вітру на провід, трос, вкритий ожеледдю Q_m, Н/м'''

'''Питомі навантаження та їх значення (гамми) (МПа/м)'''
# гамма від власної ваги проводу:
# P_l - кг/км, S - мм**2
gamma_1 = cables[cable]['P_l'] / cables[cable]['S'] * 0.981 * 10 ** (-2)  # P_l/S*0.981*10**(-2) (МПа/м)

# гамма від ваги ожеледі на проводі - МПа/м (G_mp - Н/м, S - мм**2)
gamma_2 = G_mp / cables[cable]['S']

# Від ваги проводу із ожеледдю - МПа/м:
gamma_3 = gamma_1 + gamma_2

# Від дії вітру на провід без ожеледі - МПа/м (P_m - Н/м, S - мм**2):
gamma_4 = P_m / cables[cable]['S']

# Від дії вітру на провід вкритий ожеледдю - МПа/м (Q_m - Н/м, S - мм**2)
gamma_5 = Q_m / cables[cable]['S']

# Від власної ваги проводу і дії вітру на провід без ожеледі - МПа/м:
gamma_6 = math.sqrt(gamma_1 ** 2 + gamma_4 ** 2)

# Від дії вітру на провід, вкритий ожеледдю, власної ваги, ваги ожеледі під час дії вітру на провід, вкритий ожеледдю
#  МПа/м
gamma_7 = math.sqrt((gamma_1 + 0.9 * gamma_2) ** 2 + gamma_5 ** 2)
'''(КІНЕЦЬ БЛОКУ) Питомі навантаження та їх значення (гамми) (МПа/м)'''

"""Розрахунок критичних прогонів"""
# alfa берётся из характеристики провода. betta - 1/E. E - из характеристики провода.
# 'sigma_sr' и 'sigma_nb' - из характеристики провода
betta = 1 / cables[cable]['E']
sigma_sr = cables[cable]['sigma_sr']  # для спрощення вигляду формул
sigma_nb = cables[cable]['sigma_nb']  # для спрощення вигляду формул
alfa_temp = cables[cable]['alfa']  # для спрощення вигляду формул

# Найбільше питоме навантаження з ожеледних навантажень (gamma_3 gamma_7, МПа/м):
gamma_ozh_nb = max(gamma_3, gamma_7)


# Функція для розрахунку першого критичного прогону
def find_l_1k():
    if ((6 * (betta * (sigma_sr - sigma_nb) + alfa_temp * (t_ser - t_min))) /
            (1 - (sigma_sr / sigma_nb) ** 2)) < 0:
        print((6 * (betta * (sigma_sr - sigma_nb) + alfa_temp * (t_ser - t_min))) /
              (1 - (sigma_sr / sigma_nb) ** 2))
        return False
    else:
        return 2 * sigma_sr / gamma_1 * math.sqrt(
            6 * (betta * (sigma_sr - sigma_nb) + alfa_temp * (t_ser - t_min)) /
            (1 - (sigma_sr / sigma_nb) ** 2))


# Функція для розрахунку другого критичного прогону:
def find_l_2k():
    if 6*alfa_temp*(t_ozhel - t_min)/((gamma_ozh_nb/gamma_1)**2 - 1) < 0:
        return False
    else:
        return (2 * sigma_nb / gamma_1 * math.sqrt(6 * alfa_temp * (t_ozhel - t_min) /
                                                   ((gamma_ozh_nb / gamma_1) ** 2 - 1)))
    
    
# Функція для розрахунку третього критичного прогону:
def find_l_3k():
    if (6*(betta*(sigma_nb - sigma_sr) + alfa_temp*(t_ozhel - t_ser)) /
            ((gamma_ozh_nb/gamma_1)**2 - (sigma_nb/sigma_sr)**2)) < 0:
        return False
    else:
        return 2 * sigma_nb / gamma_1 * math.sqrt(
            6 * (betta * (sigma_nb - sigma_sr) + alfa_temp * (t_ozhel - t_ser)) /
            ((gamma_ozh_nb/gamma_1) ** 2 - (sigma_nb / sigma_sr) ** 2))


'''Кінець блоку розрухунку критичних прогонів'''


'''Розрахунок габаритного, вітрового, вагового прогонів'''
# Габаритна стріла провисання проводу f_gab:
f_gab = h_op - liambda - h_gab

# Попереднє значення довжини габаритного прогону при найбільшому навантаженні (gamma_ozh_nb), м:
l_gab_ozh = math.sqrt(8*f_gab*sigma_nb/gamma_ozh_nb)


# Висота. (Приведений центр ваги провода?)
h = 10

# Характеристичне значення ожеледі, Н/м (районування) 1:8, 2:12, 3:15, 4:20, 5:30, 6:40
g_p = 15

# Характеристичне значення вітрового тиску, Па (районування) 1:400, 2:450, 3:500, 4:550, 5:600
W_o = 500

# Характеристичне значення дії вітру на провід, вкритий ожеледдю 1:4, 2:6, 3:8, 4:10, 5:12, 6:14
Q_o = 6

# Середньорічна температура:
t_ser = 8

# Максимальна температура:
t_max = 36

# Мінімальна температура:
t_min = -36

# Напряжение:
# Може мати лише стандартні значення! - {0.4, 6, 10, 35, 110, 150, 220, 330, 500, 750}
# словник класів безвідмовності від напруг:
# ///1 клас - 0.4, 6;///  ///2 клас - 10, 35;/// ///3 клас - 110, 150, 220, 330;/// ///4 класс - 500, 750///
U = 110

# Провод
cable = 'АС 120/19'

# Тип місцевості (може мати лише значення 1, 2, 3 або 4):
type_area = 2

# Приведений прогін, м:
l_pr = 240


# Довжина ізоляційного підвісу (лямбда) для проміжної опори, м:
liambda = 1.4

# Висота до нижньої  траверси опори, м:
h_op = 14.5

# Габарит до землі:
h_gab = 6

"""
Висота приведеного центра ваги провода не може бути більше 100 м!!!
Діаметр провода не може бути більше 70 мм а також не може бути менше 5 мм, хоча якщо менше 5 мм, то розрахунок  буде
виконано, але, ймовірно, результат буде не вірний!!!
Напруга U може мати лише стандартні значення! - {0.4, 6, 10, 35, 110, 150, 220, 330, 500, 750}
Розібратися з цим - "Для самоутримних ізольованих проводів переріз S дорівнює сумі перерізів усіх утримних жил"
Увага, перевірити перед розрахунком метод розрахунку коефіцієнту впливу довжини прогону k_L у функції find_k_L()!!!!!!
Температура ожеледі = -5 для територій з абсолютною висотою до 1000 м над рівнем моря!!
"""

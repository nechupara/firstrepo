# Висота. (Приведений центр ваги провода?)
h = 10

# Характеристичне значення ожеледі, Н/м (районування)
g_p = 20

# Характеристичне значення вітрового тиску, Па (районування):
W_o = 600

# Напряжение:
# Може мати лише стандартні значення! - {0.4, 6, 10, 35, 110, 150, 220, 330, 500, 750}
U = 330

# Провод
cable = 'АС 120/19'

# Тип місцевості (може мати лише значення 1, 2, 3 або 4):
type_area = 2

# Приведений прогін, м:
l_pr = 300

"""
Висота приведеного центра ваги провода не може бути більше 100 м!!!
Діаметр провода не може бути більше 70 мм а також не може бути менше 5 мм, хоча якщо менше 5 мм, то розрахунок  буде
виконано, але, ймовірно, результат буде не вірний!!!
Напруга U може мати лише стандартні значення! - {0.4, 6, 10, 35, 110, 150, 220, 330, 500, 750}
"""

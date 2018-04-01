"""
Расчёт приведённого центра массы провода для для фактической максимальной НЕ габаритной стрелы провеса, рассчитанной
программой для расчёта пересечений. Пересчитывает стрелу провеса от горизонтали на стрелу до соединительной линии.
Ориентировочно неправильный метод, предпочтительно (наверно) лучше рассчитывать
для габаритного пролёта. наверно :)
"""

height_opora_A = 5
ground_A = -2

height_opora_B = 5
ground_B = 3

distance_A_B = 100

#расстояние по горизонтали до опоры с наивысшей точкой подвеса:
from_f_to_tower = 54.78

#максимальная стрела от горизонтали, проведённой от самой высшей точки подвеса:
f_max = 6.8206

#расчёт отметок (высоты) подвеса провода:
level_cable_A = ground_A + height_opora_A
level_cable_B = ground_B + height_opora_B
#инвертирование высот подвеса для случая, если высота левой опоры ниже правой:
if level_cable_A < level_cable_B:
    level_cable_A, level_cable_B = level_cable_B, level_cable_A

level_join_line = level_cable_A - from_f_to_tower/distance_A_B*(level_cable_A - level_cable_B)
print('уровень соединительной линии: ' + str(level_join_line))
delta_f = level_cable_A - level_join_line
#стрела до линии, соединяющей точки подвеса:
strela = f_max - delta_f
print('фактическая стрела: ' + str(strela))
Hpr = (height_opora_A + height_opora_B)/2 - 2/3*strela
print('Приведенная высота центра массы = '+ str(round(Hpr, 2)))

# input('enter')




#Расчёт объёма траншеи для прокладки кабеля без торцевых уклонов и с ними
from math import sqrt

#Длина траншеи:
length = 13

#Глубина  траншеи:
H = 0.9

width_bottom = 0.5 #ширина дна  траншеи

width_uklon = 0.3 #насколько верхний край
width_top = width_bottom + 2*width_uklon

#Площадь трапеции:
S_trapecii = (width_bottom + width_top)*H/2

#Объём основной призмы траншеи:
V_osn_prizmy = S_trapecii*length
print('Объём без торцевых уклонов = ' + str(V_osn_prizmy))

#Площадь основания боковой призмы:
S_bok_trapecii = H*width_uklon/2
#Объём боковой призмы:
V_bok_prizmy = S_bok_trapecii*width_bottom

#Объём угловой пирамиды:
V_ugl_piramidy = width_uklon**2*H/3

#Объём полный:
V_full = V_osn_prizmy + 2*V_bok_prizmy + 4*V_ugl_piramidy
print('Объём с торцевыми уклонами = ' + str(V_full))

# input('press Enter for exit')

#Расчёт объёма траншеи для прокладки кабеля по формуле усечённой пирамиды
# H = 0.9
# length = 8

# width_bottom = 0.5

# width_top = 1.1
# length_top = length + 0.6

# S1 = width_bottom*length
# S2 = width_top*length_top

# V = H/3*(S1 + sqrt(S1*S2)+ S2)
# print(V)
# # print(sqrt(4))

# print('S1 = '+ str(S1))
# print('S2 = '+ str(S2))
# print('объём верт концы = '+ str((0.3*0.9+0.5*0.9)*8))
# print(0.3*0.9+0.5*0.9)
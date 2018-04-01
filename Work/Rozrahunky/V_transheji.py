#Расчёт объёма траншеи для прокладки кабеля по формуле усечённой пирамиды
from math import sqrt

H = 0.9
length = 8

width_bottom = 0.5

width_top = 1.1
length_top = length + 0.6

S1 = width_bottom*length
S2 = width_top*length_top

V = H/3*(S1 + sqrt(S1*S2)+ S2)
print(V)
# print(sqrt(4))

print('S1 = '+ str(S1))
print('S2 = '+ str(S2))
print('объём верт концы = '+ str((0.3*0.9+0.5*0.9)*8))
print(0.3*0.9+0.5*0.9)
#ненаселена місцевість: до 20кВ = 6; 35-110кВ = 6; 150кВ = 6,5; 220кВ = 7; 330кВ = 7,5; 500кВ = 8; 750кВ = 12


opora_A = 18.7
opora_B = 18.7
gabarit = 7.5

fmax = (opora_A + opora_B)/2 - gabarit
print('максимально допустимая стрела = ' + str(fmax))
height_mgab = (opora_A + opora_B)/2 - 2/3*fmax
print('приведенный центр массы для габаритного пролёта = ' + str(round(height_mgab, 2)))
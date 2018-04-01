opora_A = 14.74
opora_B = 14.74
gabarit = 7

fmax = (opora_A + opora_B)/2 - gabarit
print('максимально допустимая стрела = ' + str(fmax))
height_mgab = (opora_A + opora_B)/2 - 2/3*fmax
print('приведенный центр массы для габаритного пролёта = ' + str(round(height_mgab, 2)))
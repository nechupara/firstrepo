cyfra = '0123456789.'
with open('PerRez.txt', 'r') as file:
    str1 = file.readlines()
    
    """считываем пролёт"""
    #print(str1[6])
    progon = str1[6].strip()
    n = 0
    progon_finish_list = ['']
    for i in range(len(progon)):
        if i < len(progon) - 1:
            if progon[i] in cyfra and progon[i+1] == ' ':
                progon_finish_list[n] += progon[i]
                n += 1
                progon_finish_list.append('')
            elif progon[i] in cyfra:
                progon_finish_list[n] += progon[i]
        elif progon[i] in cyfra:
            progon_finish_list[n] += progon[i]
    distance_A_B = float(progon_finish_list[len(progon_finish_list) - 1])
    # print(progon_finish_list)
    # print(distance_A_B)
    """конец считывания пролёта"""
    
    """считывание высот подвеса (над землёй)"""
    vysota = str1[7].strip()
    # print(vysota)
    n = 0
    vysota_finish_list = ['']
    for i in range(len(vysota)):
        if i < len(vysota) - 1:
            if vysota[i] in cyfra and vysota[i+1] == ' ':
                vysota_finish_list[n] += vysota[i]
                n += 1
                vysota_finish_list.append('')
            elif vysota[i] in cyfra:
                vysota_finish_list[n] += vysota[i]
        elif vysota[i] in cyfra:
            vysota_finish_list[n] += vysota[i]
    # print(vysota_finish_list)
    height_opora_A = float(vysota_finish_list[0])
    height_opora_B = float(vysota_finish_list[1])
    # print(height_opora_A)
    # print(height_opora_B)
    """конец считывания высот подвеса над землёй"""
    
    """считывание отметок земли"""
    ground = str1[8].strip()
    # print(ground)
    n = 0
    ground_finish_list = ['']
    for i in range(len(ground)):
        if i < len(ground) - 1:
            if ground[i] in cyfra and ground[i+1] == ' ':
                ground_finish_list[n] += ground[i]
                n += 1
                ground_finish_list.append('')
            elif ground[i] in cyfra:
                ground_finish_list[n] += ground[i]
        elif ground[i] in cyfra:
            ground_finish_list[n] += ground[i]
    # print(ground_finish_list)
    ground_A = float(ground_finish_list[0])
    ground_B = float(ground_finish_list[1])
    # print(ground_A)
    # print(ground_B)
    """конец считывания отметок земли"""
    
    
    """считывание стрелы провеса и расстояния от опоры"""
    vidstan = ''
    strila = ''
    flag_vidstan = True
    flag_strila = True
    for linia in str1[10:len(str1)]:
        linia_cleared = linia.strip()
        if linia_cleared[0:11] == 'НА ВIДСТАНI' and flag_vidstan:
            for i in range(1, len(linia_cleared)-1):
                if (linia_cleared[i] in cyfra and linia_cleared[i] != '.') or \
                        (linia_cleared[i] == '.' and linia_cleared[i-1] != 'M'):
                    vidstan += linia_cleared[i]
            flag_vidstan = False
        
        elif linia_cleared[0:18] == 'МАКCИМАЛЬНА CТРIЛА' and flag_strila:
            for i in range(1, len(linia_cleared) - 1):
                if (linia_cleared[i] in cyfra and linia_cleared[i] != '.') or \
                        (linia_cleared[i] == '.' and linia_cleared[i - 1] != 'M'):
                    strila += linia_cleared[i]
            flag_strila = False
    from_f_to_tower = float(vidstan)
    f_max = float(strila)
    """конец считывания стрелы провеса и расстояния от опоры"""

# расчёт отметок (высоты) подвеса провода:
level_cable_A = ground_A + height_opora_A
level_cable_B = ground_B + height_opora_B

# инвертирование высот подвеса для случая, если высота левой опоры ниже правой:
if level_cable_A < level_cable_B:
    level_cable_A, level_cable_B = level_cable_B, level_cable_A

# Уровень соединительной линии
level_join_line = level_cable_A - from_f_to_tower/distance_A_B*(level_cable_A - level_cable_B)

# Разница между стрелой от наивысшей горизонтали и стрелой от соединительной линии
delta_f = level_cable_A - level_join_line

# стрела до линии, соединяющей точки подвеса:
strela = f_max - delta_f

# Приведённый центр массы:
Hpr = (height_opora_A + height_opora_B)/2 - 2/3*strela


print('Высота подвеса опоры А = ' + str(height_opora_A))
print('Отметка земли  опоры А = ' + str(ground_A))
print('///////')
print('Высота подвеса опоры В = ' + str(height_opora_B))
print('Отметка земли  опоры В = ' + str(ground_B))
print('///////')
print('Макс. стрела от горизонтали = ' + str(f_max))
print('Расстояние до наивысшей опоры = ' + str(from_f_to_tower))
print('///////')
print('уровень соединительной линии: ' + str(level_join_line))
print('фактическая стрела: ' + str(strela))
print('')
print('========================================')
print('Приведенная высота центра массы = '+ str(round(Hpr, 2)))
print('========================================')
input('Press Enter to exit')




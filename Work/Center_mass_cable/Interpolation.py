#то, что известно:
strela_max = 12.11
strela_min = 11.74
strela_need = 12

#то, что ищем:
prolet_max = 325
prolet_min = 320


prolet_result = prolet_max - (strela_max - strela_need)/(strela_max - strela_min)*(prolet_max - prolet_min)
print('результат = ' + str(round(prolet_result, 2)))
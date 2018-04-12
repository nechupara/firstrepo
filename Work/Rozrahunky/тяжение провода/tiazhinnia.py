with open('percent.txt', 'r') as file:
    str1 = file.readlines()
    for_exec = str1[0] + str1[1]
    print(for_exec)
    exec(for_exec)
    
while 1:
    tiazh_max = float(input('Введите наибольшее напряжение в проводе: '))
    print(round(tiazh_max/sigma_max*sigm_sredn,1))   #' при наибольшем %s, среднем %s', (sigma_max, sigm_sredn))
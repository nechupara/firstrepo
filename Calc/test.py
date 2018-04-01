choice = 'y'
while choice == 'y':
    c1 = input('введите первое число: ')
    c2 = input('введите второе число: ')
    op = input('введите оператор: ')
    print('ответ равен: ' + str(eval(c1 + op + c2)))
    choice = input('хотите продолжить? (y/n): ')
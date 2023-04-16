# Написать алгоритм генератора случайных паролей из следующих символов:
# Программа должна запрашивать длину необходимого пароля,
# в случае если в поле для задания длинны вносится не числовое значение 
# пользователь должен информироваться о том, что он допустил ошибку

import random
Znaki = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' 
i=0   # Счётчик букв в пароле
Znak=''
Parolj=''    # Иницируем пароль 
DlinaParolya=0
Zelanie=''
Zelanie=input('Желаете сгенерировать новый пароль ? Д/Н :')
j=0 # Расположение случайного знака в строке Znaki для пароля
while Zelanie not in ('Н','н') :
    i, j=(0,0)
    Parolj=''
    try:
        DlinaParolya=int(input('Введите длину пароля:'))
        while i < DlinaParolya:
            j= random.randint (0,len(Znaki)-1)
            Znak=Znaki[j]
            Parolj=Parolj + Znak 
            i=i+1
        print('Пароль:', Parolj,'\n')
    except ValueError:
        # DlinaParolya=0
        print('\n Введенно нечисловое значение')
        print('Пароль несгенерирован')
        print('Попробуйте ещё раз:')
    Zelanie=input('Желаете сгенерировать новый пароль ? Д/Н :')
print('Пароль сгенерирован и выбран:', Parolj,'\n\n')



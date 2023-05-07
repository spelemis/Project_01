# Написать алгоритм генератора случайных паролей из следующих символов:
# Программа должна запрашивать длину необходимого пароля,
# в случае если в поле для задания длинны вносится не числовое значение 
# пользователь должен информироваться о том, что он допустил ошибку

import random
Chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' 
i=0   # Счётчик букв в пароле
Char=''
Password=''    # Иницируем пароль 
Chars_in_Password=0
Choice=''
Choice=input('Желаете сгенерировать новый пароль ? Д/Н :')
j=0 # Расположение случайного знака в строке Chars для пароля
while Choice not in ('Н','н') :
    i, j=(0,0)
    Password=''
    try:
        Chars_in_Password=int(input('Введите длину пароля:'))
        while i < Chars_in_Password:
            j= random.randint (0,len(Chars)-1)
            Char=Chars[j]
            Password=Password + Char 
            i=i+1
        print('Пароль:', Password,'\n')
    except ValueError:
        # Chars_in_Password=0
        print('\n Введенно нечисловое значение')
        print('Пароль несгенерирован')
        print('Попробуйте ещё раз:')
    Choice=input('Желаете сгенерировать новый пароль ? Д/Н :')
print('Пароль сгенерирован и выбран:', Password,'\n\n')



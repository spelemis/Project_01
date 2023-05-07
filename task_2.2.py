# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    
    if month >0 and month <= 3 :
        Quarter=1
    else : 
        if month >3 and month <= 6:
            Quarter=2
        else:
            if month >6 and month <= 9:
                Quarter=3
            else:
                Quarter=4
    return Quarter

Mnt = 0 

while Mnt not in range (1,13) :
    
    try:
        Mnt=int(input('Введите номер месяца:'))
        if Mnt not in range(1,13):
           print('\n Такого месяца нет!')
        else :
           print ('Mesec:', Mnt, 'Это квартал № :', quarter_of(Mnt))          
    except ValueError:
        print('\n Введены неправильные данные.')
        print('Попробуйте ещё раз:')

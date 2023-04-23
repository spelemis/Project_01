# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    
    if month >0 and month <= 3 :
        Kvartal=1
    else : 
        if month >3 and month <= 6:
            Kvartal=2
        else:
            if month >6 and month <= 9:
                Kvartal=3
            else:
                Kvartal=4
    return Kvartal

Msc = 0 

while Msc not in range (1,13) :
    
    try:
        Msc=int(input('Введите номер месяца:'))
        if Msc not in range(1,13):
           print('\n Такого месяца нет!')
        else :
           print ('Mesec:', Msc, 'Это квартал № :', quarter_of(Msc))          
    except ValueError:
        print('\n Введены неправильные данные.')
        print('Попробуйте ещё раз:')

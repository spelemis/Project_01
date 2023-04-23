# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!


def minimum(arr):
    Min=arr[0]
    for i in range(0, len(arr)):
        if arr[i] < Min:
             Min=arr[i]
    return Min

def maximum(arr):
    Maks=arr[0]
    for i in range(0, len(arr)):
        if arr[i] > Maks:
             Maks=arr[i]
    return Maks

Osibka=False
Zelanie=input ('Желаете ввнести новый список (Д/Н) ? ')
# Ввод данных : колличество эл. списка и элементы списка.
#********************************************************
while Zelanie != 'Н':
    try:
        ElementovSpiska =int(input('  Введите кол. элементов списка:'))
        i=0
        Spisok=[]
        while i in range (0, ElementovSpiska):
              try:
                ElementSpiska=int(input('Внесите целое число, эл.списка: '))
                Spisok.insert(i,ElementSpiska)
                print (i, 'Spisok[i]=', Spisok[i])
                i +=1
              except ValueError:

                print('\n Введены неправильные данные.')
                print(' Пробуйте ещё раз:')

    except ValueError:
        print('\n Введены неправильные данные.')
        print(' Пробуйте ещё раз:')
        Osibka=True
        Zelanie='Д'
    if not(Osibka) :
        print(Spisok)
        print ('Минимум=', minimum(Spisok))
        print ('Максимум=', maximum(Spisok))
    Osibka= False
    Zelanie=input ('Желаете ввнести новый список (Д/Н) ? ')
#****************************************************************************

print ('\n До новых встреч !')


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

Error=False
Choice=input ('Желаете внести новый список (Д/Н) ? ')
# Ввод данных : колличество эл. списка и элементы списка.
#********************************************************
while Choice != 'Н':
    try:
        Items_in_listing =int(input('  Введите кол. элементов списка:'))
        i=0
        Listing=[]
        while i in range (0, Items_in_listing):
              try:
                Item=int(input('Внесите целое число, эл.списка: '))
                Listing.insert(i,Item)
                print (i+1, 'Список[',i+1,']=', Listing[i])
                i +=1
              except ValueError:

                print('\n Введены неправильные данные.')
                print(' Пробуйте ещё раз:')

    except ValueError:
        print('\n Введены неправильные данные.')
        print(' Пробуйте ещё раз:')
        Error=True
        Choice='Д'
    if not(Error) :
        print(Listing)
        print ('Минимум=', minimum(Listing))
        print ('Максимум=', maximum(Listing))
    Error= False
    Choice=input ('Желаете внести новый список (Д/Н) ? ')
#****************************************************************************

print ('\n До новых встреч !')
print('\n')


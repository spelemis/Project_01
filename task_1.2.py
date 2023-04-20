# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random

DlinaMassiva= len(my_favorite_songs)
print ('\n Длина списка: ', DlinaMassiva,'\n')
print ('Список песень: \n')
i=0
while i<DlinaMassiva:
    print ('          №',i+1, my_favorite_songs[i][0], my_favorite_songs[i][1] )
    i +=1
i=0
X=0   # Ощее время звучания
print('\n Случайно выбраные песни (сонги): \n')
while i<3:
    VibraniySong= random.randint (0, DlinaMassiva-1)
    X=X + my_favorite_songs[VibraniySong][1]       # Считаем общее время звучания

    print('           i=', VibraniySong+1,'/Название:', my_favorite_songs[VibraniySong][0], 
          '/Длина звучания сонга:', my_favorite_songs[VibraniySong][1])
    i +=1
print ('\n Три песни звучат', X,'мин',
       '\n*****************************************\n')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
DlinaMassiva= len(my_favorite_songs_dict)

print ('\n Длина словаря: ', DlinaMassiva,'\n')
i=0
X=0   # Ощее время звучания
print('         Случайно выбраные песни (сонги): \n')
while i<3:
    VibraniySong= random.randint (0, DlinaMassiva-1)
    j=0
    for key in my_favorite_songs_dict:
        if j==VibraniySong :
            print('          j=',j+1, key, my_favorite_songs_dict[key])
            X +=my_favorite_songs_dict[key]
        j +=1
    i +=1
print ('\n Три песни звучат ', X,'мин',
       '\n------------------------------------------\n')

       


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# УЖЕ СДЕЛАНО В ПУНКТАХ А и В !!!


# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

import datetime

Zvucanie= datetime.timedelta()

print ('\n Длина списка: ', DlinaMassiva,'\n')
print ('Список песень: \n')
i=0
while i<DlinaMassiva:
    Zv=round(my_favorite_songs[i][1]*60)
    Zvucanie=datetime.timedelta( seconds=Zv)
    print ('       №',i+1, my_favorite_songs[i][0], Zvucanie)
    i +=1




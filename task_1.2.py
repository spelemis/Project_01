# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

print(' ----------- A -----------------\n')

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

Array_length= len(my_favorite_songs)
print ('\n Длина списка: ', Array_length,'\n')
print ('Список песень: \n')
i=0
while i<Array_length:
    print ('          №',i+1, my_favorite_songs[i][0], my_favorite_songs[i][1] )
    i +=1
i=0
X=0   # Ощее время звучания
print('\n Случайно выбраные песни (сонги): \n')
while i<3:
    Selected_song= random.randint (0, Array_length-1)
    X=X + my_favorite_songs[Selected_song][1]       # Считаем общее время звучания

    print('           i=', Selected_song+1,'/Название:', my_favorite_songs[Selected_song][0], 
          '/Длина звучания сонга:', my_favorite_songs[Selected_song][1])
    i +=1
print ('\n Три песни звучат', X,'мин',
       '\n*****************************************\n')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

print(' ----------- B -----------------\n')

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
Array_length= len(my_favorite_songs_dict)

print ('\n Длина словаря: ', Array_length,'\n')
i=0
X=0   # Общее время звучания
print('         Случайно выбраные песни (сонги): \n')
while i<3:
    Selected_song= random.randint (0, Array_length-1)
    j=0
    for key in my_favorite_songs_dict:
        if j==Selected_song :
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

print(' -----------C.A-----------------\n')

print('         Случайно выбранная песня : \n')
Selected_song= random.randint (0, Array_length-1)
print (Selected_song+1,'.', my_favorite_songs[Selected_song])


print(' -----------C.B-----------------\n')

print('случайно выбранная песня:', random.sample(my_favorite_songs, 1) )



# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

print(' ----------- D -----------------\n')

import datetime

Duration= datetime.timedelta()

print ('\n Длина списка: ', Array_length,'\n')
print ('Список песень: \n')
i=0
while i<Array_length:
    Dur=round(my_favorite_songs[i][1]*60)
    Duration=datetime.timedelta( seconds=Dur)
    print ('       №',i+1, my_favorite_songs[i][0], Duration)
    i +=1




# Задача 1.1.
# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй,
#  второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

ItogoBukv = len(my_favorite_songs) # Определение длины входной строки
i=0   # Счётчик букв в входной строке
j=0   # Счётчик треков
Pesnya=['','','','']      # Множество треков выделенных из входной строки
Song=''   # Промежуточное название трека
while i < ItogoBukv:
    if my_favorite_songs[i] == ',': 
        Pesnya[j]=Song # Выделили запятую, значит название трека собрано .
        j=j+1
        i=i+1     #Пробел после запятой в входной строке перескочить.
        Song =''
    Song = Song + my_favorite_songs[i] # Собираем название трека № j из букв.
    i=i+1
# Выводим данные в заданной очереди :
    
print('\n','\n', Pesnya[0], Pesnya[3], Pesnya[1], Pesnya[2])
print('\n',Pesnya[0],'\n', Pesnya[3],'\n', Pesnya[1],'\n', Pesnya[2])


    










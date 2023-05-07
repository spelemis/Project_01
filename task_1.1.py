# Задача 1.1.
# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй,
#  второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

Number_of_letters = len(my_favorite_songs) # Определение длины входной строки
i=0   # Счётчик букв в входной строке
j=0   # Счётчик треков
Song=['','','','']      # Множество треков выделенных из входной строки
Temp_Song=''   # Промежуточное название трека
while i < Number_of_letters:
    if my_favorite_songs[i] == ',': 
        Song[j]=Temp_Song # Выделили запятую, значит название трека собрано .
        j=j+1
        i=i+1     #Пробел после запятой в входной строке перескочить.
        Temp_Song =''
    Temp_Song = Temp_Song + my_favorite_songs[i] # Собираем название трека № j из букв.
    i=i+1
# Выводим данные в заданной очереди :
    
print('\n','\n', Song[0], Song[3], Song[1], Song[2])
print('\n',Song[0],'\n', Song[3],'\n', Song[1],'\n', Song[2])
print('\n')


    










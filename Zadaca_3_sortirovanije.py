# Задача №3
# Отсортировать массив
# [12, 4, 54, 29, 46, 36, 72, 99, 85] 
# Вывести итог на экран

Massiv = [12, 4, 54, 29, 46, 36, 72, 99, 85]

i, j = (0, 0)
DlinaMassiva = len (Massiv)

print ('Dlina massiva :', DlinaMassiva)
print('Несортированный массив:', Massiv,)
while i<DlinaMassiva:
    Min=Massiv[i]
    IndexMin=i
    for j in range(i,DlinaMassiva):
        if Massiv[j]<Min:
            Min= Massiv[j]
            IndexMin=j
    Massiv[IndexMin]=Massiv[i]
    Massiv[i]=Min
    i=i+1
print('Сортированный массив:', Massiv,)
  

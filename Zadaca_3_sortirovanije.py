# Задача №3
# Отсортировать массив
# [12, 4, 54, 29, 46, 36, 72, 99, 85] 
# Вывести итог на экран

Arr = [12, 4, 54, 29, 46, 36, 72, 99, 85]

i, j = (0, 0)
Number_of_Items = len (Arr)

print ('Dlina massiva :', Number_of_Items)
print('Несортированный массив:', Arr,)
while i<Number_of_Items:
    Min=Arr[i]
    IndexMin=i
    for j in range(i,Number_of_Items):
        if Arr[j]<Min:
            Min= Arr[j]
            IndexMin=j
    Arr[IndexMin]=Arr[i]
    Arr[i]=Min
    i=i+1
print('Сортированный массив:', Arr,)
  

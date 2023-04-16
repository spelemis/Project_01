#Отсортировать рандомный целочисленный массив из 10 чисел в интервале от (1; 100) 
#Любым из пройденных способов
import random
i=0
Massiv=[0,0,0,0,0,0,0,0,0,0]
for i in range (0,9):
    Massiv[i]= random.randint(1,100)
print ('Несортированный массив:', Massiv) 
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
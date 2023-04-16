#Отсортировать рандомный целочисленный массив из 10 чисел в интервале от (1; 100) 
#Любым из пройденных способов
# Это программа будет переделана на сорт. пузырком .
import random

Massiv=[0,0,0,0,0,0,0,0,0,0]
i, j = (0, 0)
# DlinaMassiva = 0
DlinaMassiva = len (Massiv)
for i in range (0, len (Massiv)):
    Massiv[i]= random.randint(1,100)
print ('Несортированный массив:', Massiv) 
i=0
while i<DlinaMassiva:
    Min=Massiv[i]
    IndexMin=i
    for j in range(0,DlinaMassiva):
        if Massiv[j]<Min:
            Min= Massiv[j]
            IndexMin=j
    Massiv[IndexMin]=Massiv[i]
    Massiv[i]=Min
    i=i+1
print('Сортированный массив:', Massiv,)
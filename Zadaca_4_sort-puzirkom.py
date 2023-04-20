#Отсортировать рандомный целочисленный массив из 10 чисел в интервале от (1; 100) 
#Любым из пройденных способов
# Это программа сортирует по алгоритму "пузырок".
import random

Massiv=[0,0,0,0,0,0,0,0,0,0]
i, j = (0, 0)

DlinaMassiva = len (Massiv)

for i in range (0, DlinaMassiva):
    Massiv[i]= random.randint(1,100)
print ('Несортированный массив:', Massiv) 

while DlinaMassiva>0:
    for j in range(0,DlinaMassiva-1):
        if Massiv[j]>Massiv[j+1]:
            Pom=Massiv[j+1]
            Massiv[j+1]=Massiv[j]
            Massiv[j]=Pom
    DlinaMassiva -=1

print('Сортированный массив:', Massiv,)
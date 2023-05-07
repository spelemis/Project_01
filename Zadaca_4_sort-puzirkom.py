#Отсортировать рандомный целочисленный массив из 10 чисел в интервале от (1; 100) 
#Любым из пройденных способов
# Это программа сортирует по алгоритму "пузырок".
import random

Arr=[0,0,0,0,0,0,0,0,0,0]
i, j = (0, 0)

Number_of_Items = len (Arr)

for i in range (0, Number_of_Items):
    Arr[i]= random.randint(1,100)
print ('\n Несортированный массив:', Arr) 

while Number_of_Items>0:
    for j in range(0,Number_of_Items-1):
        if Arr[j]>Arr[j+1]:
            Pom=Arr[j+1]
            Arr[j+1]=Arr[j]
            Arr[j]=Pom
    Number_of_Items -=1

print('\n Сортированный массив:', Arr,)
print('\n')
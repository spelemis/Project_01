# Решение задачи 1 - с кубиком

import random
Itogo=0
for i in range (0,4):
    x=random.randint(1,6)
    print( 'Выпавшее число:', x, '\n')
    Itogo= Itogo + x
print ('Сумма выпавших чисел:', Itogo,'\n\n')

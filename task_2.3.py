# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!



def switch_it_up(number):
    if number not in range (0,9):
        return None
    else:
        CifriPropisyu={1:'один',2:'два', 3:'три', 4:'четыри', 5:'пять', 6:'шесть', 7:'семь',8:'восемь', 9:'девять', 0:'нуль'}
        return CifriPropisyu[number]

Cifra=int(input('Введите цифру от 1 по 9 :'))

print ('Вы ввели цифру:',switch_it_up(Cifra) )


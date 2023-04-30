# Зарплата сотрудника составляет salary руб.,
# Расходы на проживание не превышают зарплату и составляют expenses руб. в месяц.
# Зарплата растет каждый месяц , кроме 1 на 5% в месяц.
# Напишите скрипт расчета суммы денег, которую сотрудник накопит за ближайший год, (12
# месяцев).
# Формат вывода:
# Сотрудник накопит: ХХХ.ХХ рублей

salary=float(input('Внесите сумму зарплаты:'))
expenses = float(input('Внесите сумму расходов:'))
money_acc=float(0)
salary_1 = salary
salary_2 = salary

# 1. Вариант
# Зарплата увеличивается 5% по отношению с предыдущим месяцом 
for i in range(12) :
    money_acc += salary - expenses
    print (i,'  Zarplata:', round(salary,2), 'Rashodi:', expenses, 'Nakopljenjije:', round(money_acc,2))
    salary *= 1.05
print ('Сотрудник накопит:', round(money_acc,2),'руб')


# 2. Вариант
# Зарплата увеличивается 5% по отношению с первым месяцом
money_acc = 0 
Inc_salary= salary_1 * 0.05
for i in range(12) :
    money_acc += salary_2 - expenses
    salary_2 += Inc_salary
print ('\n Сотрудник накопит:', round(money_acc,2),'руб')
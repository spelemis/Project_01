# Зарплата сотрудника составляет salary руб.,
# Расходы на проживание не превышают зарплату и составляют expenses руб. в месяц.
# Зарплата растет каждый месяц , кроме 1 на 5% в месяц.
# Напишите скрипт расчета суммы денег, которую сотрудник накопит за ближайший год, (12
# месяцев).
# Формат вывода:
# Сотрудник накопит: ХХХ.ХХ рублей

salary=float(input('\n     Внесите сумму зарплаты:'))
expenses = float(input('     Внесите сумму расходов:'))
money_acc=float(0)
salary_1 = salary
salary_2 = salary

# 1. Вариант
# Зарплата увеличивается 5% по отношению с предыдущим месяцом 
print('\n----------- 1.Вариант----------')
print('Зарплата увеличивается 5% по отношению с предыдущим месяцом\n')
for i in range(12) :
    money_acc += salary - expenses
    print (i,'  Зарплата:', round(salary,2), 'Расходы:', expenses, 'Накопление:', round(money_acc,2))
    salary *= 1.05
print ('Сотрудник накопит:', round(money_acc,2),'руб')


# 2. Вариант
# Зарплата увеличивается 5% по отношению с первым месяцом

print('\n------- 2. Вариант-----------')
print('Зарплата увеличивается 5% по отношению с первым месяцом\n')
money_acc = 0 
Inc_salary= salary_1 * 0.05
for i in range(12) :
    money_acc += salary_2 - expenses
    print (i,'  Зарплата:', round(salary_2,2), 'Расходы:', expenses, 'Накопление:', round(money_acc,2))
    salary_2 += Inc_salary
print ('\n Сотрудник накопит:', round(money_acc,2),'руб')
print('\n')
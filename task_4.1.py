# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

con = sqlite3.connect('teatchers.db')
cur=con.cursor()

def ConnectDB():
    con = sqlite3.connect('teatchers.db')
    cur=con.cursor()
    return

def CreateTable():
    sql= '''CREATE TABLE Students (
                 Student_Id INTEGER,
                 Student_Name STRING,
                 School_Id INTEGER PRIMARY KEY)'''
    cur.execute(sql)
    return

def InsertInTable():
    sql= '''INSERT INTO Students
        VALUES 
            (? ,? ,?)'''
    arr = [(201, 'Иван', 1),
           (202, 'Петр', 2),
           (203, 'Анастасия', 3),
           (204, 'Игорь', 4)]
    cur.executemany(sql, arr)
    return

def SelectFrom ():
    IdStudent= int(input('ИД студента (201-204)='))
    sql= '''SELECT * FROM Students'''
    cur.execute(sql)
    arr = cur.fetchall()
    for i in range(len(arr)):
        if arr[i][0]==IdStudent: 
            print('\n')
            print('ID Студента:', arr[i][0])
            print('Имя студента:', arr[i][1])
            print('ID школы:', arr[i][2])
            #print('Название школы:',arr[3][i])
    return


# CreateTable()
InsertInTable()

SelectFrom()

cur.close()
con.close()




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
    
    sql= '''CREATE TABLE School (
            School_Id INTEGER NOT NULL PRIMARY KEY, 
            School_Name TEXT NOT NULL,
            Place_Count INTEGER NOT NULL
            )'''

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

    sql= '''INSERT INTO School
            VALUES
                  (?,?,?)'''
    arr=[('1', 'Протон', 200),
         ('2', 'Преспектива', 300),
         ('3', 'Спектр', 400),
        ('4', 'Содружество', 500)]
    cur.executemany(sql, arr)
    return

def SelectFrom ():
    IdStudent= int(input('\n ИД студента (201-204)='))
    sql= '''SELECT 
                Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name
            FROM Students, School
            WHERE (Students.School_ID = School.School_Id AND Student_Id=''' 
    sql = sql + ' '+ str(IdStudent)+');'
    cur.execute(sql)
    arr = cur.fetchall()
    for i in range(len(arr)):
            print('\n')
            print('ID Студента:', arr[i][0])
            print('Имя студента:', arr[i][1])
            print('ID школы:', arr[i][2])
            print('Название школы:',arr[i][3])
    print('\n\n')
    return

def DeleteTable():
    sql= '''DELETE FROM Students'''
    cur.execute(sql)
    sql= '''DELETE FROM School'''
    cur.execute(sql)
    return

def DropTable():
    cur.execute('DROP TABLE Students')
    cur.execute('DROP TABLE School')
    return

DropTable()
CreateTable()   
DeleteTable()
InsertInTable()
SelectFrom()

cur.close()
con.close()




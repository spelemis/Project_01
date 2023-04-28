# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no" 

def remove_exclamation_marks(s):
    return s.replace('!','')


print(remove_exclamation_marks('Hi! Hello!'))
print(remove_exclamation_marks(''))
print(remove_exclamation_marks('Oh, no!!!'))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[-1]=='!':
       s=s[:len (s)-1]
    return s

print (remove_last_em('Hi!'))
print (remove_last_em('Hi!!!'))
print (remove_last_em('!Hi'))  

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    i, j=0, 0
    s1=''
    
    Splited_s = s.split(' ')
    Length_Sp_s= len(Splited_s)
    for i in range (0,Length_Sp_s):  # Цикл собирает нове слово
        k=0                          # Количество знаков ! в слове
        for j in range (0, len(Splited_s[i])):
            if Splited_s[i][j]== '!':
                k += 1
        if k != 1 :                 # Если к=1 то часть строки не добавляем в новую строку
            s1=s1 + Splited_s[i]+' '
    print ('Строка для обработки =', s)
    s1 = s1[0:len(s1)-1]    # Удаляем последний ,добавленый в цикле, знак пробела ' '.
    return (s1)

print ('Новая строка =',remove_word_with_one_em('Hi!'))
print ('Новая строка =',remove_word_with_one_em('Hi! Hi!'))
print ('Новая строка =',remove_word_with_one_em('Hi! Hi! Hi!'))
print ('Новая строка =',remove_word_with_one_em('Hi Hi! Hi!'))
print ('Новая строка =',remove_word_with_one_em('Hi! !Hi Hi!'))
print ('Новая строка =',remove_word_with_one_em('Hi! Hi!! Hi!'))
print ('Новая строка =',remove_word_with_one_em('Hi! !Hi! Hi!'))


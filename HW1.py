# 1 определить являеться ли строка записью числа
a = 'hello my darling'
print(a.isdigit())
a = '12223'
print(a.isdigit())
a = ''
print(a.isdigit())
a = '123hey'
print(a.isdigit())
print("end -----------------next exercise")

# 2 посчитать количество пробелов в строке
a = 'how is the day today'
print(a.count(' '))

print("end -----------------next exercise")
# 3 посчитать количество '.' в строке
a='Hi. Today. How. do. you. do. FINE.'
print(a.count('.'))

print("end -----------------next exercise")
#4 Создать строку Homework, преобразовать в строку с 100 символами, посередени-Homework, по сторонам - пробелы.
# Посчитать общую длинну.
a='Homework'
b=' '
print(len(a))
print((100-len(a))/2)
x=(46*b+a+b*46)
print(x)
print(len(x))

print("end -----------------next exercise")

# 5 Сделать первые буквы слов строки большими (upper case)
a='hi, infopulse, i am studing python with you'
print(a.title())
print("end -----------------next exercise")

# 6 Определить заканчивается ли строка подстрокой "ing"
print('ing' in 'hi, infopulse, i am studing python with you')
print("end -----------------next exercise")

# 7 Определить индекс первого вхождения символа "а" в сттроке
a='Hi, today. How do you do? FINE!'
print(a.index('a', 0, -1))
a='Hi, today. How do you do? FINEaa!'
print(a.rindex('a', 0, -1))
print("end -----------------next exercise")

# 8 Разбиение строки на список подстрок по символу пробела.
a='Hi, today. How are you'
print(a.split())
print("end -----------------next exercise")

# 9 Строка с пробелами. Найти метод,который удаляет пробельные символи в начале и в конце, но не посередине.
a='  Hi, today. How are you  '
print(a.strip())
print(a.replace(' ', ''))
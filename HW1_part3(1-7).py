# 1. Вывести третье с конца слово из списка
import fileinput

a = ['List', 'are', 'used', 'in Python', '3.9', '__']
print(a[-3])
print('--------------- next exercise 2')
# 2. Вывести 1-й символ второго слова из списка.
b = (a[1])
print(list(b[0]))

print('--------------- next exercise 3')
# 3. Вывести последний символ последнего слова из списка.
b = (a[-1])
print(list(b[-1]))
print('--------------- next exercise 4')
# 4. Добавить в конец списка еще одно слово.
a.append("often")
print(a)
print('--------------- next exercise 5')
# 5. Добавить в середину списка еще одно слово.
a.insert((len(a)-1)//2, 'OHHH')
print(a)
print('--------------- next exercise 6')
# 6. Удалить первое слово со списка.
del(a[0])
print(a)
print('--------------- next exercise 7')
# 7. Удалить слово 3.9 из списка
a.remove('3.9')
print(a)


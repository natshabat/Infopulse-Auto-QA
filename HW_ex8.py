# 1 У вас есть список чисел.
# Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым
a = [23, 18, 78, 99, 28, 39, 64]
while a:
    print(a.pop(0))
print(a)

# 2 Напишите цикл, который выводит на экран и удаляет элементы списка от самого маленького
# до самого большого, пока он не останется пустым.
a = [23, 18, 78, 99, 28, 39, 64]
while a:
    print(a)
    a.remove(min(a))

# 3 Дана последовательность натуральных ненулевых чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу
b = [9, 9, 9, 9, 11, 12, 12, 12, 12, 12, 0]
result = dict((i, b.count(i)) for i in b)
print(result)
print(max(result.values()), 'times the number:', max(result, key=result.get))
# придумала разом з google :)

# 4 Напишите цикл, который выводит на экран и «удаляет» первый символ строки, пока она не станет пустой?

c = 'goodbye'
print(c)
i = 0
while c:
    c = c[1:]
    print(c)
    i = + 1
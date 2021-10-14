# Задание 4
# Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов (неопределенное количество).
# Учитываем, что может быть повторяющиеся значения аргументов.

# def second_biggest_digit(*digits):
#     x = list(digits)
#     print(list(set(x)))
#     x.remove(min(x))
#     print(min(x))
#
#
# second_biggest_digit(5, 5, 6, 8, 3, 3, 3, 9)

def second_biggest_digit(*x):
    x = dict((i, x.count(i)) for i in x)
    x = (list(x.keys()))
    print(x)
    x.remove(min(x))
    print(x)
    print(min(x))


second_biggest_digit(56,89,90,65,56)

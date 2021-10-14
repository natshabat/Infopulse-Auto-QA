# Задание 2. (на функции)
# Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите его ввести.
# Функция возвращает введённое число.
# Теперь далее для других задач с числами, вы можете пользоваться этой функцией, а не простым input!

def check_number():
    while True:
        num = input('Enter number: ')
        if num.isdigit():
            return num
        else:
            print('Wrong number, please try again. ')


check_number()

# Пишем функцию, которая попросит пользователя ввести слово (строка без пробелов в середине,
#  а вначале и в конце пробелы могут быть – их стоит удалить перед проверкой). Пока он не введёт
# правильно, просите его ввести. Функция возвращает введённое слово.

def check_sentence():
    while True:
        sen = input('Enter the sentence: ')
        sen = (sen.strip())
        if ' ' not in sen:
            return sen
        else:
            print('Wrong sentence, please try again. ')


check_sentence()

# Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами
# и если существует, то возвращает тип треугольника Equilateral triangle (равносторонний),
# Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle)

def check_triangle(*args):
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    if a == b == c:
        print('Equilateral triangle ')
    elif a == b or b == c or c == a:
        print('Isosceles triangle')
    elif a + b > c and a + c > b and b + c > a:
        print('Versatile triangle ')
    elif a == str(a) or a == str(b) or c == str(c):
        print('Please, enter the numbers')
    else:
        print('Triangle does not exist')
    print('end')


check_triangle()

# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точками с координатами (x1, y1) и (x2, y2).
# Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.



def find_distance_coordinates(*args):
    from math import sqrt
    x1 = int(input('Enter coordinates for A x1: '))
    y1 = int(input('Enter coordinates for A y1: '))
    x2 = int(input('Enter coordinates for B x2: '))
    y2 = int(input('Enter coordinates for B y2: '))
    print('Distance is: ', sqrt(((x2 - x1) ** 2)+((y2 - y1) ** 2)))


find_distance_coordinates()

# Напишите функцию, которая удаляет все небуквенные символы внутри строки
# (ограничимся латинским алфавитом).

def leaving_only_letters(*args):
    import re
    b = input('Enter the sentence: ')
    print(re.sub("[^a-zA-Z-а-ьА-Ь- ]", "", b))
    # якщо раптом запитаєте, як це працює, то все, що в квадратових дужках - залишається,
    # решту видаляється. Тут я залишила латиницю, кирилицю і пробіл., решта - заміна на ''
    # Частина (re.sub("[^a-zA-Z]- чесно загуглена


leaving_only_letters()

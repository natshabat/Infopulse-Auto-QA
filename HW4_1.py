# Задание 1 (на исключения)
# Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом (любым),
# то должна выполняться конкатенация, т. е. соединение, строк. В остальных случаях введённые числа суммируются.

a = input('enter a: ')
b = input('enter b: ')
try:
    a = int(a)
    b = int(b)
except (ValueError, TypeError):
    print(str(a)+str(b))
else:
    print(a+b)

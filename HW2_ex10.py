import string
# Создайте строку, в которой написан, какой-то текст.
# Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
# Удалите знаки препинания в списке слов (пройдитесь циклом все слова и удалите методом strip знаки препинания)
# Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
# Посчитать, сколько раз встречается каждое слово:

a = "We are not what we should be!\n We are not what we need to be.\n But at least we are not what we used to be"
print(a)
a = a.lower()
a = a.lstrip()
b = a.split()
print(len(b))


for word in string.punctuation:
    if word in a:
        a = a.replace(word, '')
print(a)
# y = (sorted(a.split()))
# print(y)

x = dict((i, (sorted(a.split())).count(i)) for i in (sorted(a.split())))

for key, value in x.items():
    print(key, ':', value)

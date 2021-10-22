# Задание 1 (на создание классов)
# Переделываем (а что-то повторяем и закрепляем) наши классы таким образом:
# 1) Person (два свойства: 1. теперь full_name пусть будет свойством, а не функцией (одно поле, мы ожидаем - тип строка
# и состоит из двух слов «имя фамилия»), а свойств name и surname нету, 2. год рождения).
# Реализовать методы, которые:
# 	•	выделяет только имя из full_name
# 	•	выделяет только фамилию из full_name;
# 	•	вычисляет сколько лет было/есть/исполнится в году, который передаётся параметром (obj.age_in(year));
# 	если не передавать параметр, по умолчанию, сколько лет в этом году;
# * (дополнительное) Можете в конструкторе проверить, что в full_name передаётся строка, состоящая из двух слов,
# если нет, вызывайте исключение 😊
# * (дополнительное) Можете в конструкторе проверить, что в год рождения меньше или равно 2020
# (текущий год – для продвинутых), но больше или равно 1900. Если нет, вызывайте исключение


class Person:
    def __init__(self, fullname, birthday):
        self.fullname = fullname
        self.birthday = birthday
    def name_from_fullname(self):
        ''' выделяем только имя из full_name '''
        return p1.fullname.split()[0]
    def surname_from_fullname(self):
        ''' выделяем только фамилию из full_name '''
        return p1.fullname.split()[-1]
    def age_in_year(self, year = 2021):
        if year is None:
            age = 2021 - self.birthday
        else:
            age = year - self.birthday
        print('In', year, '=', age)


p1 = Person('Vasya Shabat', 1957)
print(p1.fullname, p1.birthday)

# print(p1.fullname.split()[0])
# print(p1.fullname.split()[-1])
# print(2021-p1.birthday)
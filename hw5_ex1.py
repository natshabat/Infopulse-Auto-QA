# Задание 1 (на создание классов)
# Переделываем (а что-то повторяем и закрепляем) наши классы таким образом:
# 1) Person (два свойства: 1. теперь full_name пусть будет свойством, а не функцией (одно поле, мы ожидаем - тип строка
# и состоит из двух слов «имя фамилия»), а свойств name и surname нету, 2. год рождения).
# Реализовать методы, которые:
# 	•выделяет только имя из full_name
# 	•выделяет только фамилию из full_name;
# 	•вычисляет сколько лет было/есть/исполнится в году, который передаётся параметром (obj.age_in(year));
# 	если не передавать параметр, по умолчанию, сколько лет в этом году;
# * (дополнительное) Можете в конструкторе проверить, что в full_name передаётся строка, состоящая из двух слов,
# если нет, вызывайте исключение 😊
# * (дополнительное) Можете в конструкторе проверить, что в год рождения меньше или равно 2020
# (текущий год – для продвинутых), но больше или равно 1900. Если нет, вызывайте исключение


class Person:
    """ The fullname and  birthday of persons"""
    def __init__(self, fullname, birthday):
        self.fullname = fullname
        if len(fullname.split()) != 2:
            raise print('The fullname should consist two words, ValueError')
        self.birthday = birthday
        if not(1900 <= birthday <= 2021):
            raise print("Please,enter the correct birthday, ValueError")
    def name_from_fullname(self):
        ''' выделяем только имя из full_name '''
        return self.fullname.split()[0]
    def surname_from_fullname(self):
        ''' выделяем только фамилию из full_name '''
        return self.fullname.split()[-1]
    def age_in_year(self, year = 2021):
        if year is None:
            age = 2021 - self.birthday
        else:
            age = year - self.birthday
        return age


p = Person('Nataliya Shabat', 1990)
print(p.fullname, p.birthday)
print(p.surname_from_fullname(), p.name_from_fullname())
print(p.age_in_year())
print(len(p.fullname.split()))

# 2) Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы, зарплата)
# * (дополнительное) Можете в конструкторе проверить, что в опыт работы и зарплата не отрицательные 😊
# Реализовать новые методы:
# •возвращает должность с приставкой, которая зависит от опыта работы: Junior — менее 3 лет, Middle — от 3 до 6 лет,
# Senior — больше 6 лет.Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior <position>.
# Если, например, у вас объект имел должность “programmer” с опытом 2 года, метод должен вернуть “Junior programmer”
# •метод, который увеличивает зарплату на сумму, которую вы передаёте аргументом.
class Employee(Person):
    """ The Persons with their job: position, experience and salary """
    def __init__(self, fullname = '', birthday = '', position= '', experience=0, salary=0):
        Person.__init__(self, fullname, birthday)
        self.position = position
        self.experience = experience
        if experience < 0:
            raise print('The experience should be more then 1 day')
        self.salary = salary
        if salary < 0:
            raise print("The salary should be more then 10")
    def level_position (self):
        """ Definition of position according to experience"""
        if self.experience <= 3:
            return 'Junior ' f'{self.position}'
        elif 3 <= self.experience <= 6:
            return 'Middle ' f'{self.position}'
        else:
            return 'Senior 'f'{self.position}'
    def salary_increasing(self, increasing = 0):
        """ Increasing of salary"""
        return self.salary + increasing

p1 = Employee('Nataliya Lesya', 1989, 'programmer', 9, 100)
print(p1.fullname, p.birthday, p1.experience, p1.salary)
print(p1.level_position())
print(p1.salary_increasing(800))

# 3) ITEmployee (наследуемся от Employee)
# 1. Реализовать метод добавления одного навыка в новое свойство skills (список) новым методом add_skill
# (см. презентацию).
# 2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список) новым методом add_skills.
# Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы расширяете список-свойство skill,
# или вы принимаете неопределённое количество аргументов, и все их добавляете в список-свойство skill

class ITEmployee(Employee):
    ''''The Employee in IT-area including Person and Employee features '''
    def __init__(self, *args, **kwargs):
        Employee.__init__(self, *args, **kwargs)
        self.skills = []
    def add_skills (self, *new_skill):
        """Adding new skills for ITEmployee"""
        self.skills.append(new_skill)
        return str(self.skills)

p2 = ITEmployee('Nataliya Lesya', 1989, 'programmer', 9, 100)
print(p2.add_skills('python 2,7', 'python 3,9'), p2.level_position(), p2.experience)
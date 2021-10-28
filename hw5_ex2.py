# Задание 2 (на создание новых классов)
# Создать классы
# 1) Прямоугольная площадка (пример: комната) (свойства: две стороны).
# Методы:
# 	•	вычисляем площадь,
# 	•	вычисляем периметр.

class ROOM:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area_calculating(self):
        ''' вычисляем площадь '''
        return'Area is of room ' f'{self.side1 * self.side2}'

    def perimeter_calculating(self):
        ''' вычисляем периметр '''
        return'Perimeter is of room ' f'{(self.side1 + self.side2)*2}'

x = ROOM(5,5)
print(x.area_calculating())
print(x.perimeter_calculating())

# 2) Студент (свойства: имя-фамилия, специальность, год начала обучения, список оценок – при создании объекта,
# по умолчанию, пустой список).
# Методы:
# 	•	Добавить новую оценку в свойство списка оценок
# 	•	Посчитать средний балл,
# 	•	Посчитать сколько лет учится уже студент.


class Student:

    """All information about student"""
    def __init__(self, fullname, speciality, start_date, marks = []):
        self.fullname = fullname
        self.speciality = speciality
        self.start_date = start_date
        self.marks = marks

    def add_mark(self, new_mark):
        """Adding new marks of students"""
        self.marks.append(new_mark)
        return str(self.marks)

    def average_mark(self):
        """Calculation of mark's average"""
        return sum(self.marks)/len(self.marks)

    def study_term(self, x=2021):
        """How long the student is learning"""
        return 'The term of learning ist: ' f'{x-self.start_date} ' 'years'


x = Student('Nataliya Shabat', 'IT', 2019, [9, 12, 10, 11])
print(x.add_mark(4))
print(x.average_mark())
print(x.study_term())


# 3) Точка на карте (свойства: X, Y).
# Методы:
# 	•	Нужно вычислить расстояние до начала координат,
# 	•	* вычисляется расстояние между точкой и другой точкой экземпляром этого же класса

class Point:

    """The point with X and Y on the coordinate system """

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def distance_to_origin(self):
        """ Нужно вычислить расстояние до начала координат"""
        from math import sqrt
        return sqrt(self.X**2+self.Y**2)

    def distance_to_second_point(self, A = 0, B = 0):
        """вычисляется расстояние между точкой и другой точкой экземпляром этого же класса"""
        from math import sqrt
        return sqrt(((A - self.X) ** 2)+((B- self.Y) ** 2))



z = Point (5, 5)
print(z.distance_to_origin())
print(z.distance_to_second_point(4, 8))


def printing_deleting_from_min_to_max(a):
    while a:
        print(a)
        a.remove(min(a))


printing_deleting_from_min_to_max(a=[9, 4, 7, 9])


def is_year_leap(a):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        return'True'
    else:
        return'False'


print(is_year_leap(2004))


def existing_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return'True'
    else:
        return'False'


print(existing_triangle(5, 2, 4))

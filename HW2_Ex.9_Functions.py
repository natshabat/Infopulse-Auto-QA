
def printing_deliting_from_min_to_max(a):
    while(a):
        print(a)
        a.remove(min(a))

printing_deliting_from_min_to_max(a=[9,4,77,9])


def is_year_leap(a):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print('True')
    else:
        print('False')
is_year_leap(2004)


def existing_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print('True')
    else:
        print('False')
existing_triangle(2,1,4)
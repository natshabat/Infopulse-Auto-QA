a = float(input("Please, enter number a:"))
b = float(input("Please, enter number b:"))
c = float(input("Please, enter number c:"))
if a == b == c:
    print('3 numbers are equal')
elif b == c or b == a or a == c:
    print('2 numbers are equal')
else:
    print('0 numbers are equal')

a = float(input("Please, enter a:"))
b = float(input("Please, enter b:"))
c = float(input("Please, enter c:"))

if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')

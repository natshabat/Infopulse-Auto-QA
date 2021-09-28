a = int(input("Please, enter the year:"))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('YES')
else:
    print('NO')
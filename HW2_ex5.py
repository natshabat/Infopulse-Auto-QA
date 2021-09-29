a = float(input("Please, enter a:"))
b = float(input("Please, enter b:"))
c = float(input("Please, enter c:"))

if a >= b >= c:
    print(a, b, c)
elif b >= c >= a:
    print(b, c, a)
elif c >= b >= a:
    print(c, b, a)
elif c >= a >= b:
    print(c, a, b)
elif b >= a >= c:
    print(b, a, c)
else:
    print(a, c, b)

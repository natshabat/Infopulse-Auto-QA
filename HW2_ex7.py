# 1)
x = 0
while x <= 10:
    print(x)
    x += 1
# 2)

y = 20
while y >= 0:
    print(y, end=' ')
    y -= 1

# 3)
a = 80
count = 0
while a % 2 == 0:
    a = a/2
    count = count + 1
    print('remainder is:', str(a))
print('the quantity of divisions:', str(count))

a = [23, 18, 78, 99, 28, 39, 64]
while a:
    print(a.pop())
print(a)

a = [23, 18, 78, 99, 28, 39, 64]
while a:
    print(a)
    a.remove(min(a))

b = [9, 9, 9, 9, 11, 12, 12, 12, 0]
result = dict((i, b.count(i)) for i in b)
print(result)

# c = 'hello'
# c1=(c[:0]+''+c[1:])
# print(c1)
# c2=(c1[:0]+''+c1[1:])
# print(c2)
# c3=(c2[:0]+''+c2[1:])
# print(c3)

c = 'goodbye'
i = 0
while i <= len(c):
    c = (c[:0] + '' + c[1:])
    print(c)
    i =+ 1
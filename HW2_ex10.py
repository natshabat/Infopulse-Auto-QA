import string

a = 'We are not what we should be! We are not what we need to be. But at least we are not what we used to be'
a = a.lower()
b = a.split()
print(len(a.split()))
print(b)

for word in string.punctuation:
    if word in a:
        c = a = a.replace(word, '')
print(c)
y = c.split()
print(y)

print(sorted(y))

x = dict((i, y.count(i)) for i in y)
print(x)


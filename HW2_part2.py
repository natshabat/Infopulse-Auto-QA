a = input("Enter the sentence:")

if len(a) % 2 == 0:
    print(a[len(a)//2:], a[:len(a)//2], sep='')
else:
    print(a[len(a)//2:],  a[:len(a)//2], sep='')
b = ['T-shirt', 'Sweater']
while True:
    a = str(input('Welcome to our shop, what do you want (C, R, U, D)? '))
    if a in ('R','r'):
        print(b)
    elif a in ('C','c'):
        b.append(input('Enter new item: '))
        print(b)
    elif a in ('U','u'):
        c = int(input('Update position? '))
        if c > len(b):
            print("Out of range!")
            continue
        b.insert(c-1,input('New item?: '))
        print(b)
    elif a in ('D','d'):
        d = int(input('Delete position: '))
        if d > len(b):
            print('No item in that position!')
            continue
        b.pop(d-1)
        print(b)
    else:
        print('No such command!')
        continue

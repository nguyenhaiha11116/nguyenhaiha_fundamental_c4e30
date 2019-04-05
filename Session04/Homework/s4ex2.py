prices = {
    'banana' : 4,
    'apple' : 2,
    'orange' : 1.5,
    'pear' : 3
}

stock = {
    'banana' : 6,
    'apple' : 0,
    'orange' : 32,
    'pear' : 15
}

for v in prices:
    print(v)
    print('price:',prices[v])
    print('stock:',stock[v])
    print('')

total = 0
for v in prices:
    k = prices[v] * stock[v]
    total+=k
print(total)
    
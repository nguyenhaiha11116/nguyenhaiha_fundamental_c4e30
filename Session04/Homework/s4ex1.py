inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['poccket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].remove('dagger')
inventory['gold']+=50
print(inventory)
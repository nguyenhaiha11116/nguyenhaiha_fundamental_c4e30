listcauhoi = [
    {
        'cauhoi': 'Answer the following algebra question: ',
        'dapan': '1. 35 \n2. 36 \n3. 40 \n4. 44',
        'dapandung': 4
    },
    {
        'cauhoi': 'Estimate this answer(Exact calculation not needed): \nJack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean? ',
        'dapan': '1. about 55 \n2. about 65 \n3. about 75 \n4. about 85',
        'dapandung': 2
    }
]
v = 0
for i in listcauhoi:
    print(i['cauhoi'])
    print(i['dapan'])
    a = int(input('Your choice: '))
    if a == i['dapandung']:
        print('Bingo')
        v+=1
        continue
    else:
        print(':(')
        v+=0
        continue
print('You correctly answer',v,'out of 2 questions')
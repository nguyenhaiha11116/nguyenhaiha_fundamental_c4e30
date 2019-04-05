answer = [35, 36, 40, 44]
while True:
    print('If x = 8, then what is the value of 4(x + 3) ?')
    for b in answer:
        print(answer.index(b)+1,'\b.',b)
    a = int(input('Your choice: '))
    if a == answer.index(b)+1:
        b == 4*(8*3)
        print('Bingo')
        print('')
    else:
        print(':(')
        print('')
        continue
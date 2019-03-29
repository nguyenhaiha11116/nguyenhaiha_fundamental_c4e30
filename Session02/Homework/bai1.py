h = float(input('input height(cm):'))
w = float(input('inputweight(kg):'))
bmi = w/((h/100) * (h/100))
if bmi<16:
    print('severely underweigh')
elif bmi<18.5:
    print('Underweight')
elif bmi<25:
    print('Normal')
elif bmi<30:
    print('Overweight')
else:
    print('Obese')
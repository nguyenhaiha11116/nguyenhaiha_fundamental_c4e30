# def print_hello_word():
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')

# def sum_two_number(a,b):
#     print(a+b)

from turtle import *
def draw_square(length,mcolor):
    color(mcolor)
    for i in range(4):
        forward(length)
        right(90)
    

for i in range(30):
    draw_square(i * 5,'red')
    left(17)
    penup()
    forward(i*2)
    pendown()
        
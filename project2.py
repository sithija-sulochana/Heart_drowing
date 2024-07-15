import math
from turtle import *

def heart(k):
    return 15*math.sin(k)**3

def heart1(k):
    return 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)

speed(1000)
bgcolor('black')
color('red')

up()
goto(heart(0)*20, heart1(0)*20)
down()

for i in range(1, 6000):
    goto(heart(i)*20, heart1(i)*20)

done()

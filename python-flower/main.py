import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")  
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
h = 0 

for i in range(16):
    for j in range(18):   
        c = colorsys.hsv_to_rgb(h, 1, 1)
        rgb = tuple(int(i * 255) for i in c)  
        t.pencolor(rgb)      
        h += 0.005         
        t.right(90)
        t.circle(150 - j * 6, 90)
        t.left(90)
        t.circle(150 - j * 6, 90)
        t.left(180)
    t.circle(40, 24)  

turtle.done()
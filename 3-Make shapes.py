import turtle
import time

t = turtle.Pen()

side = [3, 4, 5, 6, 7, 8, 9, 10]
angles = [120, 90, 72, 60, 51.42, 45, 40, 36]

for i in range(8):
    
    for j in range(i+3):
        t.forward(50+(i*6))
        t.left(angles[i])
    
    t.penup()
    t.setpos(-3 , -10-(10 * i))
    t.pendown()

time.sleep(2)
from inspect import trace
import turtle as t

width = 500
t.speed(8)
sc = t.Screen()
sc.setup(width, width)
distance = 10

def hilbert_curve(order, angle):
    if order == 0:
        return
    
    t.left(angle)
    hilbert_curve(order-1, -angle)
    t.forward(distance)
    t.right(angle)
    hilbert_curve(order-1, angle)
    t.forward(distance)
    hilbert_curve(order-1, angle)
    t.right(angle)
    t.forward(distance)
    hilbert_curve(order-1, -angle)
    t.left(angle)

hilbert_curve(2,90)


t.exitonclick()


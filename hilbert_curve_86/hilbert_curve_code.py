import turtle as t

#value for the width of turtle window
width = 500
#takes care of turtle window margin
window_width = width + width/100
#value for order, is equal to recursion depth
order = 0

#function that asks for user input and catches wrong input
def user_input():
    while True:
        try:
            order_input = int(input("Enter order of Hilbert curve: "))
            if order_input > 0:
                break
            else:
                print("Please input positive integer.")
        except ValueError:
            print("Please enter number.")
    return order_input

#function uses recursion to draw Hilbert curve based on angle and order
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

#sets speed of turtle
t.speed(0)

#sets up turtle window to chosen width
sc = t.Screen()
sc.setup(window_width, window_width)

#sets order of hilbert curve
order = user_input()

#calculates the distance for one instance
try:
    distance = width/(2**order-1)
#quits if number is outside the scope of programs computing abilities
except OverflowError:
    print("Error: you entered too big number for order")
    quit()

#sets coordinates of right corner to 0
t.setworldcoordinates(0,0,window_width,window_width)

#can set off turtle animation
#t.tracer(0, 0)

#calls the hilbert function with chosen order
hilbert_curve(order,90)

#can update turtle
#t.update()

t.exitonclick()
import turtle as t

width = 500 #value for the width of turtle window
window_width = width + width/100 #takes care of turtle window margin
order = 0 #value for order, is equal to recursion depth

#function that asks for user input
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

#function draws hilbert curve
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

t.speed(0) #sets speed of turtle
sc = t.Screen()
sc.setup(window_width, window_width) #sets up turtle window to chosen width

order = user_input() #sets order of hilbert curve

try:
    distance = width/(2**order-1) #calculates the distance for one instance
except OverflowError:
    print("Error: you entered too big number for order")
    quit()

t.setworldcoordinates(0,0,window_width,window_width) #sets coordinates of right corner to 0

#t.tracer(0, 0) #can set off turtle animation

hilbert_curve(order,90) #calls the hilbert function with chosen order

#t.update() #can update turtle
t.exitonclick()
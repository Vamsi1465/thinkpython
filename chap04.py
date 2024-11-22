#Write a function called rectangle that draws a rectangle with given side lengths. For example, here's a rectangle that's 80 units wide and 40 units tall.
# import turtle
# def function(width, height):
#     for i in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)
# turtle.speed(1) 
# function(80,40)
#2
# import turtle
# def parallelogram(base,side,angle):
#     for i in range(2):
#         turtle.forward(base)
#         turtle.left(180 - side)
#         turtle.forward(base)
#         turtle.left(angle)
# turtle.speed(1)
# parallelogram(100, 60, 60)
# #3
# import turtle

# def parallelogram(base, side, angle):
#     for _ in range(2):
#         turtle.forward(base)
#         turtle.left(180 - angle)
#         turtle.forward(side)
#         turtle.left(angle)

# def rectangle(width, height):
#     parallelogram(width, height, 90)

# def rhombus(side, angle):
#     parallelogram(side, side, angle)

# # Example usage
# turtle.speed(1)
# rectangle(80, 40)
# parallelogram(90,90,90)
# turtle.done()

# For rhombus, you can call:
# rhombus(60, 60)

#4
import turtle
def traingle(side):
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)
def draw_pie(num_segments,side):
    angle = 360 / num_segments
    for i in range(num_segments):
        traingle(side)
        turtle.left(angle)

turtle.speed(1)
draw_pie(6, 100)



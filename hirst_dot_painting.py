import turtle as turtle_mod
import random


turtle_mod.colormode(255)
tim = turtle_mod.Turtle()
tim.speed('fastest')
tim.hideturtle()


color_list = [(235, 241, 246), (1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39)]

tim.penup()
tim.setheading(220)
tim.forward(350)
tim.setheading(0)


# print(rgb_colors)
dot_count = 100


for dot in range(1, dot_count+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.left(180)
# tim.forward(50)
# for _ in range(10):
# draw()

screen = turtle_mod.Screen()
screen.exitonclick()
